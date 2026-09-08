import os
import sys
import json
import base64
import argparse
import re
from pathlib import Path
import openai
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
import pymupdf as fitz  # PyMuPDF for Vision

class TokenTelemetry:
    @staticmethod
    def estimate(text: str) -> int: return len(str(text)) // 4

# --- SCHEMAS ---
class BasePracticeDef(BaseModel):
    id: str; title: str; description: str

class ExtractedProcess(BaseModel):
    process_name: str; outcomes: List[str]; base_practices: List[BasePracticeDef]

class EvidenceSourceType(str, Enum):
    IMPLEMENTATION = "implementation"
    CONFIGURATION = "configuration"
    ARCHITECTURE_MODEL = "architecture_model"
    TEST = "test"
    RESEARCH_ARTIFACT = "research_artifact"

class EvidenceUnit(BaseModel):
    id: str; file: str; symbol: Optional[str]; evidence_type: str
    source_type: EvidenceSourceType; epistemic_type: str
    language: Optional[str]; content: str
    relationships: List[str]; confidence: str

class ArchComponent(BaseModel):
    name: str; component_type: str; technology: str; responsibilities: List[str]

class ArchInterface(BaseModel):
    source: str; target: str; protocol: str; payload: List[str]

class DataTransformation(BaseModel):
    producer: str; input: str; output: str; consumer: str

class VisualArchitecture(BaseModel):
    components: List[ArchComponent]
    interfaces: List[ArchInterface]
    data_transformations: List[DataTransformation]

class RepositoryFact(BaseModel):
    id: str; fact_type: str; subject: str; predicate: str; object: Optional[str]
    evidence_ids: List[str]; source_scope: str; epistemic_type: str; confidence: str

class RepositoryModel(BaseModel):
    facts: List[RepositoryFact]

class EngineeringClaim(BaseModel):
    id: str; claim_type: str; statement: str; explanation: str
    supporting_fact_ids: List[str]; supporting_evidence_ids: List[str]
    epistemic_type: str; confidence: str

class EngineeringSynthesis(BaseModel):
    claims: List[EngineeringClaim]

class DocumentSection(BaseModel):
    title: str; intent: str; required_topics: List[str]; supporting_claim_ids: List[str]

class DocumentPlan(BaseModel):
    title: str; purpose: str; sections: List[DocumentSection]

class EvidenceStatus(str, Enum):
    STRONG_EVIDENCE = "STRONG EVIDENCE"
    PARTIAL_EVIDENCE = "PARTIAL EVIDENCE"
    NO_EVIDENCE_IDENTIFIED = "NO EVIDENCE IDENTIFIED"
    NOT_ASSESSABLE = "NOT ASSESSABLE FROM REPOSITORY"

class PracticeAssessment(BaseModel):
    id: str; title: str; status: EvidenceStatus; evidence_rationale: str

class ProcessAudit(BaseModel):
    process_name: str; audited_practices: List[PracticeAssessment]

class FinalReports(BaseModel):
    process_document: str; audit_report: str

CURRENT_DIR = Path(__file__).parent
AUTODOC_ROOT = CURRENT_DIR.parent
load_dotenv(AUTODOC_ROOT / ".env")
client = openai.OpenAI()

# --- AGENTS ---
class MultimodalIngestionAgent:
    def parse_pdf(self, pdf_path: Path) -> VisualArchitecture:
        doc = fitz.open(pdf_path)
        img_bytes = doc.load_page(0).get_pixmap(dpi=200).tobytes("png")
        b64_img = base64.b64encode(img_bytes).decode('utf-8')
        
        prompt = """Extract the intended architecture from this diagram into strict JSON.
        Identify Components (Gateways, Engines, Solvers), Interfaces (gRPC, TCP, APIs), and Data Transformations (Arrow IPC, JSON)."""
        
        response = client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[{"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_img}"}}
            ]}],
            response_format=VisualArchitecture, temperature=0.1
        )
        return response.choices[0].message.parsed

    def convert_to_evidence(self, visual_arch: VisualArchitecture) -> List[EvidenceUnit]:
        units = []
        uid = 9000
        for comp in visual_arch.components:
            uid += 1
            content = f"Component: {comp.name} | Type: {comp.component_type} | Tech: {comp.technology} | Responsibilities: {', '.join(comp.responsibilities)}"
            units.append(EvidenceUnit(id=f"EV-{uid}", file="OptArrow_Architecture.pdf", symbol=comp.name, evidence_type="visual_component", source_type=EvidenceSourceType.ARCHITECTURE_MODEL, epistemic_type="INTENDED", language="visual", content=content, relationships=[], confidence="AUTHORITATIVE"))
        for iface in visual_arch.interfaces:
            uid += 1
            content = f"Interface: {iface.source} -> {iface.target} | Protocol: {iface.protocol} | Payload: {', '.join(iface.payload)}"
            units.append(EvidenceUnit(id=f"EV-{uid}", file="OptArrow_Architecture.pdf", symbol=f"{iface.source}->{iface.target}", evidence_type="visual_interface", source_type=EvidenceSourceType.ARCHITECTURE_MODEL, epistemic_type="INTENDED", language="visual", content=content, relationships=[iface.source, iface.target], confidence="AUTHORITATIVE"))
        for dt in visual_arch.data_transformations:
            uid += 1
            content = f"Data Transform: {dt.producer} converts {dt.input} to {dt.output} for {dt.consumer}"
            units.append(EvidenceUnit(id=f"EV-{uid}", file="OptArrow_Architecture.pdf", symbol=f"{dt.input}->{dt.output}", evidence_type="visual_transformation", source_type=EvidenceSourceType.ARCHITECTURE_MODEL, epistemic_type="INTENDED", language="visual", content=content, relationships=[dt.producer, dt.consumer], confidence="AUTHORITATIVE"))
        return units

class CleanContextExtractor:
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path
        self.skip_dirs = {'.git', '.venv', '__pycache__', 'universal_engine', 'scratch', 'docs', 'tests', 'output'}

    def determine_source_type(self, path: Path) -> EvidenceSourceType:
        parts = path.parts
        if 'tests' in parts or path.name.startswith('test_'): return EvidenceSourceType.TEST
        if 'universal_engine' in parts or 'scratch' in parts: return EvidenceSourceType.RESEARCH_ARTIFACT
        if path.suffix in ['.json', '.yaml', '.toml']: return EvidenceSourceType.CONFIGURATION
        return EvidenceSourceType.IMPLEMENTATION

    def extract_code_units(self) -> List[EvidenceUnit]:
        units = []
        files = [p for p in self.repo_path.rglob("*") if p.is_file() and not any(skip in p.parts for skip in self.skip_dirs) and p.suffix != '.pdf']
        unit_id = 0
        for f in files:
            src_type = self.determine_source_type(f)
            if src_type == EvidenceSourceType.RESEARCH_ARTIFACT: continue
            try:
                content = f.read_text(encoding="utf-8", errors="ignore")
                unit_id += 1
                units.append(EvidenceUnit(id=f"EV-{unit_id}", file=str(f.relative_to(self.repo_path)), symbol=None, evidence_type="file_content", source_type=src_type, epistemic_type="IMPLEMENTED", language=f.suffix, content=content[:1500], relationships=[], confidence="HIGH"))
            except: pass
        return units

class GenericKeywordRetriever:
    def retrieve(self, process: ExtractedProcess, units: List[EvidenceUnit], max_tokens: int = 15000) -> List[EvidenceUnit]:
        query_terms = set(re.findall(r'\w+', (process.process_name + " " + " ".join(process.outcomes)).lower())) - {'the', 'a', 'to', 'for', 'process', 'software', 'system'}
        scored = []
        for u in units:
            score = sum(1 for t in query_terms if t in u.content.lower())
            if u.source_type == EvidenceSourceType.ARCHITECTURE_MODEL: score += 5  # Heavily prioritize authoritative visual diagrams
            if score > 0: scored.append((score, u))
        scored.sort(key=lambda x: x[0], reverse=True)
        
        selected = []
        current_tokens = 0
        for score, u in scored:
            tok = TokenTelemetry.estimate(u.model_dump_json())
            if current_tokens + tok > max_tokens: continue
            selected.append(u)
            current_tokens += tok
        return selected

class AgentCore:
    def build_repository_model(self, units: List[EvidenceUnit]) -> RepositoryModel:
        prompt = f"Analyze these raw evidence units (which contain both INTENDED visual architecture and IMPLEMENTED code). Extract precise engineering facts.\n{json.dumps([u.model_dump() for u in units])}"
        return client.beta.chat.completions.parse(model="gpt-4o", messages=[{"role": "user", "content": prompt}], response_format=RepositoryModel).choices[0].message.parsed

    def synthesize_engineering_claims(self, repo_model: RepositoryModel, auth_knowledge: str) -> EngineeringSynthesis:
        prompt = f"""Synthesize Repository Facts into deep Engineering Claims. 
        Reconcile the 'INTENDED' architecture (from diagrams) with 'IMPLEMENTED' reality (from code).
        Only use OBSERVED or INFERRED. Do not invent speculative claims.
        AUTHORITATIVE KNOWLEDGE: {auth_knowledge}
        FACTS: {repo_model.model_dump_json()}"""
        return client.beta.chat.completions.parse(model="gpt-4o", messages=[{"role": "user", "content": prompt}], response_format=EngineeringSynthesis).choices[0].message.parsed

    def plan_document(self, process: ExtractedProcess, claims: EngineeringSynthesis, auth_knowledge: str, prev_docs: str = "") -> DocumentPlan:
        prompt = f"""You are the Document Planner (Agent 3A). Determine a professional engineering document structure for {process.process_name} that demonstrates the outcomes WITHOUT referencing ISO standards. Create semantic headings (e.g. Logical Architecture, Data Flow).
        AUTHORITATIVE KNOWLEDGE: {auth_knowledge}
        PREVIOUS DOCS: {prev_docs}
        CLAIMS: {claims.model_dump_json()}"""
        return client.beta.chat.completions.parse(model="gpt-4o", messages=[{"role": "user", "content": prompt}], response_format=DocumentPlan).choices[0].message.parsed

    def write_engineering_document(self, plan: DocumentPlan, claims: EngineeringSynthesis, auth_knowledge: str, prev_docs: str = "") -> str:
        prompt = f"""You are the Engineering Writer (Agent 3B). Write a deeply technical software specification.
        CRITICAL: NO ISO LEAKAGE. Do not mention ISO 33061, Base Practices, or expose evidence mechanics like '(Source: file)'.
        Use the Engineering Claims to explain *how information changes representation as it moves through the system* (e.g. Python Dict -> Arrow IPC -> Julia Socket).
        AUTHORITATIVE KNOWLEDGE: {auth_knowledge}
        PLAN: {plan.model_dump_json()}
        CLAIMS: {claims.model_dump_json()}
        PREVIOUS DOCS: {prev_docs}"""
        return client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt}], max_tokens=15000).choices[0].message.content

    def generate_audit_report(self, process: ExtractedProcess, claims: EngineeringSynthesis) -> str:
        prompt = f"""Evaluate {process.process_name} Base Practices against the Engineering Claims.
        Create a Markdown GAP ANALYSIS table: Base Practice ID | Title | Status (STRONG EVIDENCE, PARTIAL EVIDENCE, NO EVIDENCE IDENTIFIED, NOT ASSESSABLE FROM REPOSITORY) | Evidence Rationale.
        BASE PRACTICES: {json.dumps([bp.model_dump() for bp in process.base_practices])}
        CLAIMS: {claims.model_dump_json()}"""
        return client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt}], max_tokens=15000).choices[0].message.content

def run_v6_3_pipeline(process_name: str, standard_path: Path, global_units: List[EvidenceUnit], auth_knowledge: str, prev_doc: str = "") -> FinalReports:
    print(f"\n--- V6.3 PIPELINE: {process_name} ---")
    core = AgentCore()
    
    print("1. Ingesting Process Definition...")
    process = client.beta.chat.completions.parse(
        model="gpt-4o", messages=[{"role": "user", "content": f"Extract Base practices and outcomes for '{process_name}' from ISO:\n{standard_path.read_text(errors='ignore')[:15000]}"}],
        response_format=ExtractedProcess
    ).choices[0].message.parsed
    
    print("2. Selective Multimodal Retrieval (RAG)...")
    retrieved_units = GenericKeywordRetriever().retrieve(process, global_units)
    print(f"   Retrieved {len(retrieved_units)} relevant units (prioritizing visual architecture).")

    print("3. Repository Understanding (Facts)...")
    repo_model = core.build_repository_model(retrieved_units)
    
    print("4. Engineering Synthesis (Claims)...")
    claims = core.synthesize_engineering_claims(repo_model, auth_knowledge)
    
    print("5. Document Planner (Agent 3A)...")
    plan = core.plan_document(process, claims, auth_knowledge, prev_doc)
    
    print("6. Engineering Writer (Agent 3B)...")
    doc_1 = core.write_engineering_document(plan, claims, auth_knowledge, prev_doc)
    
    print("7. Audit Reporter (Agent 4)...")
    doc_2 = core.generate_audit_report(process, claims)
    
    return FinalReports(process_document=doc_1, audit_report=doc_2)

if __name__ == "__main__":
    # Resolve default paths relative to repository root
    default_repo = os.getenv("TARGET_REPO_PATH", str((AUTODOC_ROOT.parent / "OPTARROW GIT" / "optArrow").resolve()))
    if not Path(default_repo).exists():
        # Fallback to sibling directory 'optArrow' if present
        sibling_repo = (AUTODOC_ROOT.parent / "optArrow").resolve()
        if sibling_repo.exists():
            default_repo = str(sibling_repo)

    parser = argparse.ArgumentParser(description="V6.3 Multimodal Agentic SDLC Process Documentation Pipeline")
    parser.add_argument("--repo", type=str, default=default_repo, help="Path to target codebase repository (or set TARGET_REPO_PATH)")
    parser.add_argument("--standard", type=str, default=str((AUTODOC_ROOT / "resources" / "standards" / "iso_33061_standard.md").resolve()), help="Path to ISO/IEC TS 33061 standard text")
    parser.add_argument("--pdf", type=str, default=str((AUTODOC_ROOT / "resources" / "case_study" / "OptArrow_Architecture.pdf").resolve()), help="Path to intended visual architecture PDF diagram")
    parser.add_argument("--output-dir", type=str, default=str((AUTODOC_ROOT / "outputs" / "representative_eval").resolve()), help="Directory to save generated engineering specifications and gap audits")
    args = parser.parse_args()
    
    target_repo = Path(args.repo)
    if not target_repo.exists():
        print(f"[ERROR] Target repository not found at: {target_repo}")
        print("Please supply a valid path via --repo <path> or set the TARGET_REPO_PATH environment variable.")
        sys.exit(1)

    standard_file = Path(args.standard)
    if not standard_file.exists():
        print(f"[ERROR] ISO standard file not found at: {standard_file}")
        print("Please supply an authorized standard markdown file via --standard <path>.")
        sys.exit(1)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=== V6.3 MULTIMODAL RAG PIPELINE ===")
    
    global_units = []
    
    # 1. Multimodal Vision Extraction
    pdf_file = Path(args.pdf)
    if pdf_file.exists():
        print("Extracting INTENDED architecture from PDF Blueprint via Vision...")
        vision_agent = MultimodalIngestionAgent()
        visual_arch = vision_agent.parse_pdf(pdf_file)
        global_units.extend(vision_agent.convert_to_evidence(visual_arch))
        print(f"Extracted {len(global_units)} structural facts from diagram.")
    else:
        print(f"[WARN] Architectural PDF diagram not found at: {pdf_file}. Continuing with source code only.")
    
    # 2. Code Extraction
    print("Extracting IMPLEMENTED architecture from Clean Code Corpus...")
    code_units = CleanContextExtractor(target_repo).extract_code_units()
    global_units.extend(code_units)
    print(f"Total Combined Multimodal Evidence Pool: {len(global_units)} units.")

    auth_knowledge = """
    OptArrow is an optimization integration engine connecting optimization clients and solver backends through a stable, high-performance transport layer. 
    Runtime centers on Python and Julia backends, callable from MATLAB. 
    Primary Objective: Solve optimization problems (LP, QP). 
    Stakeholders: Software Engineers, Researchers, Data Scientists, Optimization Specialists.
    """

    try:
        req_reports = run_v6_3_pipeline("System/software requirements definition process", Path(args.standard), global_units, auth_knowledge)
        (output_dir / "V6.3_01_Requirements_Document.md").write_text(req_reports.process_document, encoding="utf-8")
        (output_dir / "V6.3_01_Requirements_Audit.md").write_text(req_reports.audit_report, encoding="utf-8")
        
        arch_reports = run_v6_3_pipeline("Architecture definition process", Path(args.standard), global_units, auth_knowledge, req_reports.process_document)
        (output_dir / "V6.3_02_Architecture_Document.md").write_text(arch_reports.process_document, encoding="utf-8")
        (output_dir / "V6.3_02_Architecture_Audit.md").write_text(arch_reports.audit_report, encoding="utf-8")
        
        print("\n[SUCCESS] V6.3 Multimodal Chained Pipeline Completed!")
    except Exception as e:
        import traceback
        traceback.print_exc()
