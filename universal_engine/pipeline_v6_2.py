import os
import json
import argparse
import re
from pathlib import Path
import xml.etree.ElementTree as ET
import sys
import openai
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Set
from enum import Enum

class TokenTelemetry:
    @staticmethod
    def estimate(text: str) -> int:
        return len(str(text)) // 4

class BasePracticeDef(BaseModel):
    id: str
    title: str
    description: str

class ExtractedProcess(BaseModel):
    process_name: str
    outcomes: List[str]
    base_practices: List[BasePracticeDef]

class EvidenceSourceType(str, Enum):
    IMPLEMENTATION = "implementation"
    CONFIGURATION = "configuration"
    ARCHITECTURE_MODEL = "architecture_model"
    TEST = "test"
    RESEARCH_ARTIFACT = "research_artifact"

class EvidenceUnit(BaseModel):
    id: str
    file: str
    symbol: Optional[str]
    evidence_type: str
    source_type: EvidenceSourceType
    language: Optional[str]
    content: str
    relationships: List[str]
    start_line: Optional[int]
    end_line: Optional[int]
    confidence: Optional[str]

class RepositoryFact(BaseModel):
    id: str
    fact_type: str
    subject: str
    predicate: str
    object: Optional[str]
    evidence_ids: List[str]
    source_scope: str
    epistemic_type: str
    confidence: str
    engineering_significance: Optional[str]

class RepositoryModel(BaseModel):
    facts: List[RepositoryFact]

class EngineeringClaim(BaseModel):
    id: str
    claim_type: str
    statement: str
    explanation: str
    supporting_fact_ids: List[str]
    supporting_evidence_ids: List[str]
    epistemic_type: str
    confidence: str

class EngineeringSynthesis(BaseModel):
    claims: List[EngineeringClaim]

class DocumentSection(BaseModel):
    title: str
    intent: str
    required_topics: List[str]
    relevant_outcomes: List[str]
    supporting_claim_ids: List[str]

class DocumentPlan(BaseModel):
    title: str
    purpose: str
    sections: List[DocumentSection]

class EvidenceStatus(str, Enum):
    STRONG_EVIDENCE = "STRONG EVIDENCE"
    PARTIAL_EVIDENCE = "PARTIAL EVIDENCE"
    NO_EVIDENCE_IDENTIFIED = "NO EVIDENCE IDENTIFIED"
    NOT_ASSESSABLE_FROM_REPOSITORY = "NOT ASSESSABLE FROM REPOSITORY"

class EvidenceItem(BaseModel):
    file: str
    symbol: str
    evidence_type: str
    observation: str

class PracticeAssessment(BaseModel):
    id: str
    title: str
    status: EvidenceStatus
    evidence_rationale: str
    structured_evidence: List[EvidenceItem]

class ProcessAudit(BaseModel):
    process_name: str
    audited_practices: List[PracticeAssessment]

class FinalReports(BaseModel):
    process_document: str
    audit_report: str

CURRENT_DIR = Path(__file__).parent
AUTODOC_ROOT = CURRENT_DIR.parent
AUTODOC_SRC = AUTODOC_ROOT / "src"
sys.path.insert(0, str(AUTODOC_SRC))
load_dotenv(AUTODOC_ROOT / ".env")

class IngestionAgent:
    def __init__(self, model="gpt-4o", temperature=0.1):
        self.client = openai.OpenAI()
        self.model = model; self.temperature = temperature

    def extract_base_practices(self, markdown_path: Path, process_name: str) -> ExtractedProcess:
        full_text = markdown_path.read_text(encoding="utf-8", errors="ignore")
        prompt = f"Extract ALL Base practices and Process outcomes for '{process_name}' from this ISO text:\n\n{full_text[:15000]}"
        response = self.client.beta.chat.completions.parse(
            model=self.model, messages=[{"role": "user", "content": prompt}],
            response_format=ExtractedProcess, temperature=self.temperature,
        )
        return response.choices[0].message.parsed

class LightweightASTExtractor:
    @staticmethod
    def extract_blocks(file_content: str, language: str) -> List[dict]:
        blocks = []
        lines = file_content.split('\n')
        pattern = re.compile(r'^\s*(def|class)\s+([a-zA-Z0-9_]+)') if language == 'python' else re.compile(r'^\s*(function|struct|module|macro)\s+([a-zA-Z0-9_!]+)')
        if language not in ['python', 'julia']: return [{"symbol": None, "start_line": 1, "end_line": len(lines), "content": file_content[:2000]}]
        
        capturing, current_block, symbol, base_indent, start_line = False, [], "", 0, 0
        for i, line in enumerate(lines):
            match = pattern.match(line)
            indent = len(line) - len(line.lstrip())
            if match and not capturing:
                capturing, base_indent, symbol, start_line = True, indent, match.group(2), i + 1
                current_block.append(line)
            elif capturing:
                if line.strip() == "": current_block.append(line)
                elif indent <= base_indent and language == 'python':
                    blocks.append({"symbol": symbol, "start_line": start_line, "end_line": i, "content": "\n".join(current_block)})
                    if match: base_indent, symbol, start_line, current_block = indent, match.group(2), i + 1, [line]
                    else: capturing, current_block = False, []
                elif re.match(r'^\s*end\b', line) and language == 'julia' and indent == base_indent:
                    current_block.append(line)
                    blocks.append({"symbol": symbol, "start_line": start_line, "end_line": i + 1, "content": "\n".join(current_block)})
                    capturing, current_block = False, []
                else: current_block.append(line)
        if capturing: blocks.append({"symbol": symbol, "start_line": start_line, "end_line": len(lines), "content": "\n".join(current_block)})
        if not blocks: blocks.append({"symbol": None, "start_line": 1, "end_line": len(lines), "content": file_content[:2000]})
        return blocks

class CleanContextExtractor:
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path
        self.extensions = {'.py': 'python', '.jl': 'julia', '.ts': 'typescript', '.js': 'javascript'}
        self.skip_dirs = {'.git', '.venv', 'scripts', '__pycache__', 'node_modules', 'universal_engine', 'scratch', 'docs', 'tests', 'output'}

    def determine_source_type(self, path: Path) -> EvidenceSourceType:
        parts = path.parts
        if 'tests' in parts or path.name.startswith('test_'): return EvidenceSourceType.TEST
        if 'universal_engine' in parts or 'generate' in path.name or 'scratch' in parts: return EvidenceSourceType.RESEARCH_ARTIFACT
        if path.suffix in ['.json', '.yaml', '.yml', '.toml', '.txt']: return EvidenceSourceType.CONFIGURATION
        if path.suffix == '.drawio': return EvidenceSourceType.ARCHITECTURE_MODEL
        return EvidenceSourceType.IMPLEMENTATION

    def extract_units(self) -> List[EvidenceUnit]:
        units = []
        files = [p for p in self.repo_path.rglob("*") if p.is_file() and not any(skip in p.parts for skip in self.skip_dirs)]
        unit_id = 0
        for f in files:
            src_type = self.determine_source_type(f)
            if src_type == EvidenceSourceType.RESEARCH_ARTIFACT: continue # Exclude contaminated corpus
            rel_path = str(f.relative_to(self.repo_path))
            lang = self.extensions.get(f.suffix)
            try:
                content = f.read_text(encoding="utf-8", errors="ignore")
                if lang in ['python', 'julia']:
                    blocks = LightweightASTExtractor.extract_blocks(content, lang)
                    for b in blocks:
                        unit_id += 1
                        units.append(EvidenceUnit(id=f"EV-{unit_id}", file=rel_path, symbol=b['symbol'], evidence_type="code_block", source_type=src_type, language=lang, content=b['content'], relationships=[], start_line=b['start_line'], end_line=b['end_line'], confidence="HIGH"))
                else:
                    unit_id += 1
                    units.append(EvidenceUnit(id=f"EV-{unit_id}", file=rel_path, symbol=None, evidence_type="file_content", source_type=src_type, language=lang or 'text', content=content[:2000], relationships=[], start_line=1, end_line=None, confidence="MEDIUM"))
            except: pass
        return units

class AgentCore:
    def __init__(self): self.client = openai.OpenAI()

    def build_repository_model(self, units: List[EvidenceUnit]) -> RepositoryModel:
        json_units = json.dumps([u.model_dump() for u in units])
        prompt = f"Analyze these raw evidence units. Extract engineering facts. Distinguish between PRODUCT, PROCESS, and DOCUMENTATION requirements.\n{json_units}"
        return self.client.beta.chat.completions.parse(model="gpt-4o", messages=[{"role": "user", "content": prompt}], response_format=RepositoryModel).choices[0].message.parsed

    def synthesize_engineering_claims(self, repo_model: RepositoryModel) -> EngineeringSynthesis:
        prompt = f"""Synthesize the Repository Facts into higher-level Engineering Claims (e.g. architectural boundaries, routing mechanisms, validation strategies). 
        Only use OBSERVED or INFERRED. Do not invent speculative claims.\n{repo_model.model_dump_json()}"""
        return self.client.beta.chat.completions.parse(model="gpt-4o", messages=[{"role": "user", "content": prompt}], response_format=EngineeringSynthesis).choices[0].message.parsed

    def plan_document(self, process: ExtractedProcess, claims: EngineeringSynthesis, previous_docs: str = "") -> DocumentPlan:
        prompt = f"""You are the Document Planner (Agent 3A).
        PROCESS TO DEMONSTRATE: {process.process_name}
        OUTCOMES: {process.outcomes}
        PREVIOUS LIFECYCLE DOCS: {previous_docs if previous_docs else 'None'}
        
        Given the engineering claims below, determine a professional engineering document structure that demonstrates the outcomes WITHOUT referencing the standard, ISO, or Base Practices.
        Create proper semantic headings (e.g., 'Logical Architecture', 'Interface Requirements').
        ENGINEERING CLAIMS:\n{claims.model_dump_json()}"""
        return self.client.beta.chat.completions.parse(model="gpt-4o", messages=[{"role": "user", "content": prompt}], response_format=DocumentPlan).choices[0].message.parsed

    def write_engineering_document(self, plan: DocumentPlan, claims: EngineeringSynthesis, previous_docs: str = "") -> str:
        prompt = f"""You are the Engineering Writer (Agent 3B). Write a professional software specification document based on the Document Plan.
        
        CRITICAL INSTRUCTIONS (NO ISO LEAKAGE):
        1. DO NOT mention ISO 33061, Base Practices, compliance, or assessment terminology.
        2. DO NOT expose evidence mechanics. Do not write "(Source: file.py)" or "Requirement: ...". Write flowing, professional engineering prose that explains the system.
        3. Use the Engineering Claims to provide deep technical rationale.
        4. Write it for another engineer to understand the system.
        
        DOCUMENT PLAN:\n{plan.model_dump_json(indent=2)}
        
        ENGINEERING CLAIMS:\n{claims.model_dump_json(indent=2)}
        
        PREVIOUS DOCS FOR TRACEABILITY:\n{previous_docs}
        """
        response = self.client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt}], max_tokens=15000)
        return response.choices[0].message.content

    def generate_audit_report(self, process: ExtractedProcess, claims: EngineeringSynthesis, units: List[EvidenceUnit]) -> str:
        prompt = f"""Evaluate the Base Practices for {process.process_name} against the Engineering Claims.
        Create a detailed Markdown GAP ANALYSIS table.
        Columns: Base Practice ID | Title | Status (STRONG EVIDENCE, PARTIAL EVIDENCE, NO EVIDENCE IDENTIFIED, NOT ASSESSABLE) | Evidence Rationale & Source Citations.
        
        BASE PRACTICES:\n{json.dumps([bp.model_dump() for bp in process.base_practices])}
        
        ENGINEERING CLAIMS:\n{claims.model_dump_json()}
        """
        response = self.client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt}], max_tokens=15000)
        return response.choices[0].message.content

def run_v6_2_pipeline(process_name: str, standard_path: Path, repo_path: Path, global_units: List[EvidenceUnit], previous_doc: str = "") -> FinalReports:
    print(f"\n--- RUNNING V6.2 PIPELINE: {process_name} ---")
    core = AgentCore()
    
    print("1. Ingesting Process Definition...")
    process = IngestionAgent().extract_base_practices(standard_path, process_name)
    
    print("2. Repository Understanding (Facts)...")
    repo_model = core.build_repository_model(global_units[:30]) # Using top 30 for budget constraint (simplified generic retriever)
    
    print("3. Engineering Synthesis (Claims)...")
    claims = core.synthesize_engineering_claims(repo_model)
    
    print("4. Document Planner (Agent 3A)...")
    plan = core.plan_document(process, claims, previous_doc)
    
    print("5. Engineering Writer (Agent 3B)...")
    doc_1 = core.write_engineering_document(plan, claims, previous_doc)
    
    print("6. Audit Reporter (Agent 4)...")
    doc_2 = core.generate_audit_report(process, claims, global_units[:30])
    
    return FinalReports(process_document=doc_1, audit_report=doc_2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=str, default=str(Path("C:/Users/oladi/Desktop/Thesis/OPTARROW GIT/optArrow")))
    parser.add_argument("--standard", type=str, default=str(Path(__file__).parent / "iso_33061_standard.md"))
    parser.add_argument("--output", type=str, default=str(Path(__file__).parent / "output"))
    args = parser.parse_args()
    
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Extracting Clean Corpus (Filtering out Research Artifacts)...")
    extractor = CleanContextExtractor(Path(args.repo))
    global_units = extractor.extract_units()
    print(f"Clean extraction complete: {len(global_units)} VALID evidence units found.")

    try:
        # Step 1: Requirements Definition
        req_reports = run_v6_2_pipeline("System/software requirements definition process", Path(args.standard), Path(args.repo), global_units)
        (output_dir / "V6.2_01_Requirements_Document.md").write_text(req_reports.process_document, encoding="utf-8")
        (output_dir / "V6.2_01_Requirements_Audit.md").write_text(req_reports.audit_report, encoding="utf-8")
        
        # Step 2: Architecture Definition (Chained)
        arch_reports = run_v6_2_pipeline("Architecture definition process", Path(args.standard), Path(args.repo), global_units, req_reports.process_document)
        (output_dir / "V6.2_02_Architecture_Document.md").write_text(arch_reports.process_document, encoding="utf-8")
        (output_dir / "V6.2_02_Architecture_Audit.md").write_text(arch_reports.audit_report, encoding="utf-8")
        
        print("\n[SUCCESS] V6.2 Chained Pipeline Completed!")
    except Exception as e:
        import traceback
        traceback.print_exc()
