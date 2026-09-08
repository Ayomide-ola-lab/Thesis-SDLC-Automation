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
import random

class TokenTelemetry:
    @staticmethod
    def estimate(text: str) -> int:
        return len(str(text)) // 4

    @staticmethod
    def log(agent_name: str, categories: dict):
        total = sum(categories.values())
        print(f"[{agent_name}] Token Telemetry:")
        for cat, count in categories.items():
            print(f"  - {cat}: ~{count}")
        print(f"  - TOTAL: ~{total}")

class BasePracticeDef(BaseModel):
    id: str
    title: str
    description: str

class ExtractedProcess(BaseModel):
    process_name: str
    outcomes: List[str]
    base_practices: List[BasePracticeDef]

class EvidenceUnit(BaseModel):
    id: str
    file: str
    symbol: Optional[str]
    evidence_type: str
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
    confidence: str

class RepositoryModel(BaseModel):
    facts: List[RepositoryFact]

class EvidenceItem(BaseModel):
    file: str
    symbol: str
    evidence_type: str
    observation: str
    confidence: str

class PracticeAssessment(BaseModel):
    id: str
    title: str
    status: str
    evidence_rationale: str
    structured_evidence: List[EvidenceItem]

class ProcessAudit(BaseModel):
    process_name: str
    audited_practices: List[PracticeAssessment]

class FinalReports(BaseModel):
    process_document: str
    audit_report: str

class ProcessSectionNotFoundError(Exception):
    pass

CURRENT_DIR = Path(__file__).parent
AUTODOC_ROOT = CURRENT_DIR.parent
AUTODOC_SRC = AUTODOC_ROOT / "src"
sys.path.insert(0, str(AUTODOC_SRC))
load_dotenv(AUTODOC_ROOT / ".env")

class StandardIngestionAgent:
    def __init__(self, model: str = "gpt-4o", temperature: float = 0.1):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model; self.temperature = temperature

    def _locate_section(self, text: str, process_name: str) -> str:
        lines = text.split("\n")
        capturing = False
        captured_lines = []
        target_level = 0
        
        for line in lines:
            match = re.match(r'^(#{1,6})\s+(.*)', line)
            if match:
                level = len(match.group(1))
                heading_text = match.group(2).strip().lower()
                
                if capturing:
                    if level <= target_level:
                        break
                    else:
                        captured_lines.append(line)
                else:
                    if process_name.lower() in heading_text:
                        capturing = True
                        target_level = level
                        captured_lines.append(line)
            elif capturing:
                captured_lines.append(line)
                
        if not capturing:
            raise ProcessSectionNotFoundError(f"Could not locate heading for process: {process_name}")
            
        return "\n".join(captured_lines)

    def extract_base_practices(self, markdown_path: Path, process_name: str) -> ExtractedProcess:
        full_text = markdown_path.read_text(encoding="utf-8", errors="ignore")
        section_text = self._locate_section(full_text, process_name)
        
        prompt = f"""Extract ALL "Base practices" and "Process outcomes" from the provided ISO text.
ISO STANDARD TEXT:
{section_text}"""
        response = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format=ExtractedProcess,
            temperature=self.temperature,
        )
        return response.choices[0].message.parsed

class LightweightASTExtractor:
    @staticmethod
    def extract_blocks(file_content: str, language: str) -> List[dict]:
        blocks = []
        lines = file_content.split('\n')
        
        if language == 'python':
            pattern = re.compile(r'^\s*(def|class)\s+([a-zA-Z0-9_]+)')
        elif language == 'julia':
            pattern = re.compile(r'^\s*(function|struct|module|macro)\s+([a-zA-Z0-9_!]+)')
        else:
            return [{"symbol": None, "start_line": 1, "end_line": len(lines), "content": file_content[:2000]}]

        capturing = False
        current_block = []
        symbol = ""
        base_indent = 0
        start_line = 0

        for i, line in enumerate(lines):
            match = pattern.match(line)
            indent = len(line) - len(line.lstrip())
            
            if match and not capturing:
                capturing = True
                base_indent = indent
                symbol = match.group(2)
                start_line = i + 1
                current_block.append(line)
            elif capturing:
                if line.strip() == "":
                    current_block.append(line)
                elif indent <= base_indent and language == 'python':
                    blocks.append({"symbol": symbol, "start_line": start_line, "end_line": i, "content": "\n".join(current_block)})
                    if match:
                        base_indent = indent
                        symbol = match.group(2)
                        start_line = i + 1
                        current_block = [line]
                    else:
                        capturing = False
                        current_block = []
                elif re.match(r'^\s*end\b', line) and language == 'julia' and indent == base_indent:
                    current_block.append(line)
                    blocks.append({"symbol": symbol, "start_line": start_line, "end_line": i + 1, "content": "\n".join(current_block)})
                    capturing = False
                    current_block = []
                else:
                    current_block.append(line)
                    
        if capturing:
            blocks.append({"symbol": symbol, "start_line": start_line, "end_line": len(lines), "content": "\n".join(current_block)})
            
        if not blocks:
            blocks.append({"symbol": None, "start_line": 1, "end_line": len(lines), "content": file_content[:2000]})
        return blocks

class ContextExtractor:
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path
        self.extensions = {'.py': 'python', '.jl': 'julia', '.ts': 'typescript', '.js': 'javascript'}
        self.exact_files = {'Dockerfile', 'requirements.txt', 'docker-compose.yml', 'pyproject.toml', 'package.json'}
        # V6: Tests are no longer skipped to gather requirement behaviour evidence
        self.skip_dirs = {'.git', '.venv', 'scripts', '__pycache__', 'node_modules', 'dist', 'build', 'out', 'target', 'coverage'}

    def extract_units(self) -> List[EvidenceUnit]:
        units = []
        files = [p for p in self.repo_path.rglob("*") if p.is_file() and not any(skip in p.parts for skip in self.skip_dirs)]
        
        unit_id = 0
        for file_path in files:
            rel_path = str(file_path.relative_to(self.repo_path))
            
            if file_path.suffix == ".drawio":
                try:
                    tree = ET.parse(file_path)
                    nodes, edges = {}, []
                    for cell in tree.getroot().iter('mxCell'):
                        cid, val, src, tgt = cell.get('id'), cell.get('value', ''), cell.get('source'), cell.get('target')
                        val = ' '.join(re.sub(r'<[^>]+>', ' ', val).replace('&nbsp;', ' ').strip().split())
                        if src and tgt: edges.append({"source": src, "target": tgt, "label": val})
                        elif cid and val: nodes[cid] = val
                    for edge in edges:
                        src_label = nodes.get(edge['source'], f"Node_{edge['source']}")
                        tgt_label = nodes.get(edge['target'], f"Node_{edge['target']}")
                        unit_id += 1
                        units.append(EvidenceUnit(
                            id=f"EV-{unit_id}", file=rel_path, symbol=f"{src_label} -> {tgt_label}",
                            evidence_type="diagram_edge", language="xml", content=edge['label'],
                            relationships=[src_label, tgt_label], start_line=None, end_line=None, confidence="HIGH"
                        ))
                except Exception:
                    pass
                continue

            lang = self.extensions.get(file_path.suffix)
            if lang or file_path.name in self.exact_files:
                try:
                    content = file_path.read_text(encoding="utf-8", errors="ignore")
                    if lang in ['python', 'julia']:
                        blocks = LightweightASTExtractor.extract_blocks(content, lang)
                        for block in blocks:
                            unit_id += 1
                            units.append(EvidenceUnit(
                                id=f"EV-{unit_id}", file=rel_path, symbol=block['symbol'], 
                                evidence_type="code_block", language=lang, content=block['content'],
                                relationships=[], start_line=block['start_line'], end_line=block['end_line'], confidence="HIGH"
                            ))
                    else:
                        unit_id += 1
                        units.append(EvidenceUnit(
                            id=f"EV-{unit_id}", file=rel_path, symbol=None, evidence_type="file_content",
                            language=lang or 'text', content=content[:2000],
                            relationships=[], start_line=1, end_line=None, confidence="MEDIUM"
                        ))
                except Exception:
                    pass
        return units

class GenericKeywordRetriever:
    def retrieve(self, query: str, units: List[EvidenceUnit]) -> List[EvidenceUnit]:
        stopwords = {'the', 'a', 'an', 'and', 'or', 'to', 'for', 'of', 'in', 'is', 'on', 'with', 'as', 'by', 'system', 'process', 'software', 'implementation', 'elements', 'define', 'identify'}
        query_terms = set(re.findall(r'\w+', query.lower())) - stopwords
        
        scored_units = []
        for u in units:
            searchable_text = " ".join([
                u.file,
                u.symbol or "",
                u.evidence_type,
                u.content,
                " ".join(u.relationships)
            ]).lower()
            
            score = sum(1 for term in query_terms if term in searchable_text)
            if u.confidence == "HIGH": score += 0.5
            
            if score > 1.5: 
                scored_units.append((score, u))
                
        scored_units.sort(key=lambda x: x[0], reverse=True)
        return [u for score, u in scored_units]

class ContextBudgetManager:
    def __init__(self, max_tokens: int = 6000):
        self.max_tokens = max_tokens

    def fill_budget(self, retrieved: List[EvidenceUnit]) -> List[EvidenceUnit]:
        budgeted = []
        current_tokens = 0
        for unit in retrieved:
            unit_tokens = TokenTelemetry.estimate(unit.model_dump_json())
            if current_tokens + unit_tokens > self.max_tokens:
                continue 
            budgeted.append(unit)
            current_tokens += unit_tokens
        return budgeted

class RepositoryUnderstandingAgent:
    def __init__(self, model: str = "gpt-4o", temperature: float = 0.1):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model; self.temperature = temperature

    def build_repository_model(self, units: List[EvidenceUnit], process_name: str) -> RepositoryModel:
        raw_units_json = json.dumps([u.model_dump() for u in units], separators=(',', ':'))
        prompt = f"""
Synthesize the raw evidence units into a highly technical, structured Repository Model focused on: {process_name}.
Extract generic 'RepositoryFacts' relevant to this process (e.g. constraints, requirements, behaviors, interfaces).
CRITICAL: Map exactly which 'evidence_ids' support each fact!

RAW EVIDENCE UNITS:
{raw_units_json}
"""
        response = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format=RepositoryModel,
            temperature=self.temperature,
        )
        return response.choices[0].message.parsed

class IterativeEvidenceAuditor:
    def __init__(self, model: str = "gpt-4o", temperature: float = 0.2):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model; self.temperature = temperature
        self.retriever = GenericKeywordRetriever()
        self.budget_manager = ContextBudgetManager(max_tokens=6000)

    def audit_base_practices(self, extracted: ExtractedProcess, repo_model: RepositoryModel, units: List[EvidenceUnit]) -> ProcessAudit:
        audited = []
        for bp in extracted.base_practices:
            query = f"{bp.title} {bp.description} " + " ".join(extracted.outcomes)
            retrieved_units = self.retriever.retrieve(query, units)
            budgeted_units = self.budget_manager.fill_budget(retrieved_units)
            evidence_context_json = json.dumps([u.model_dump() for u in budgeted_units], separators=(',', ':'))
            repo_model_json = repo_model.model_dump_json()

            prompt = f"""
Evaluate this Base Practice against the Repository Model and retrieved Evidence Units.

PROCESS OUTCOMES:
{json.dumps(extracted.outcomes, separators=(',', ':'))}

BASE PRACTICE:
ID: {bp.id}
Title: {bp.title}
Description: {bp.description}

STRUCTURED REPOSITORY MODEL:
{repo_model_json}

TARGETED EVIDENCE UNITS:
{evidence_context_json}
"""
            response = self.client.beta.chat.completions.parse(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                response_format=PracticeAssessment,
                temperature=self.temperature,
            )
            audited.append(response.choices[0].message.parsed)

        return ProcessAudit(process_name=extracted.process_name, audited_practices=audited)

class NarrativeCompilerAgent:
    def __init__(self, model: str = "gpt-4o", temperature: float = 0.2):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model; self.temperature = temperature

    def compile_report(self, audit: ProcessAudit, repo_model: RepositoryModel, units: List[EvidenceUnit]) -> FinalReports:
        resolved_evidence = []
        needed_ids = set()
        for fact in repo_model.facts: needed_ids.update(fact.evidence_ids)
        
        for u in units:
            if u.id in needed_ids:
                resolved_evidence.append({"id": u.id, "file": u.file, "symbol": u.symbol, "content": u.content})
        
        resolved_evidence_json = json.dumps(resolved_evidence, separators=(',', ':'))
        repo_model_json = repo_model.model_dump_json()
        audit_json = audit.model_dump_json()
        
        prompt = f"""
Generate TWO distinct Markdown documents for the process: {audit.process_name}.

DOCUMENT 1: THE PROCESS DOCUMENT
Structure the document dynamically based on the requested process. Address the outcomes naturally. 
Use semantic headings appropriate for the domain (e.g., for requirements use headings like 'Functional Requirements', 'System Constraints', 'Validation Rules', 'Interfaces'). Do NOT use the epistemic principles as headings.

Follow the 9 Epistemic Reasoning Principles silently in your writing style:
1. Evidence Primacy: Technical claims must be derived ONLY from supplied evidence.
2. Technical Specificity: Identify concrete technical nouns.
3. Explicit Uncertainty: Use cautious language.
4. Repository Neutrality: Treat domain purposes as unknown until proven.
5. Narrative Synthesis: Synthesise facts into connected engineering prose. Do not use bullet points.
6. Controlled Abstraction: Introduce technical names in context.
7. Evidence-Bounded Rationale: Do not state WHY a technology was selected unless explicitly documented.
8. Claim Discipline: Avoid generic unsupported words.
9. Avoid semantic laundering.

DOCUMENT 2: THE INTERNAL AUDIT REPORT
- Create a concise Markdown gap-analysis table citing structured evidence items (file, symbol).

STRUCTURED REPOSITORY MODEL:
{repo_model_json}

VERIFIED SOURCE EVIDENCE:
{resolved_evidence_json}

AUDIT FINDINGS:
{audit_json}

OUTPUT FORMAT (JSON with "process_document" and "audit_report"):
"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=self.temperature,
        )
        reports_dict = json.loads(response.choices[0].message.content.strip())
        return FinalReports(
            process_document=reports_dict.get("process_document", ""),
            audit_report=reports_dict.get("audit_report", "")
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=str, default=str(Path("C:/Users/oladi/Desktop/Thesis/OPTARROW GIT/optArrow")))
    parser.add_argument("--standard", type=str, default=str(Path(__file__).parent / "iso_33061_standard.md"))
    parser.add_argument("--process", type=str, default="System/software requirements definition process")
    parser.add_argument("--output", type=str, default=str(Path(__file__).parent / "output"))
    args = parser.parse_args()
    
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        ingestion_agent = StandardIngestionAgent()
        extracted_data = ingestion_agent.extract_base_practices(Path(args.standard), args.process)

        extractor = ContextExtractor(Path(args.repo))
        evidence_units = extractor.extract_units()

        # Process-driven retrieval for Agent 1.5 instead of architecture bias
        retriever = GenericKeywordRetriever()
        process_query = args.process + " " + " ".join(extracted_data.outcomes)
        ranked_units = retriever.retrieve(process_query, evidence_units)
        
        repo_units = []
        current_tokens = 0
        for u in ranked_units:
            tokens = TokenTelemetry.estimate(u.model_dump_json())
            if current_tokens + tokens <= 15000:
                repo_units.append(u)
                current_tokens += tokens
        
        repo_agent = RepositoryUnderstandingAgent()
        repo_model = repo_agent.build_repository_model(repo_units, args.process) 

        auditor = IterativeEvidenceAuditor()
        final_audit = auditor.audit_base_practices(extracted_data, repo_model, evidence_units)
        
        compiler = NarrativeCompilerAgent()
        reports = compiler.compile_report(final_audit, repo_model, evidence_units)
        
        doc1_file = output_dir / "V6_Automated_Requirements_Process.md"
        doc2_file = output_dir / "V6_Automated_Requirements_Audit.md"
        
        doc1_file.write_text(reports.process_document, encoding="utf-8")
        doc2_file.write_text(reports.audit_report, encoding="utf-8")
        print("Done!")
    except Exception as e:
        import traceback
        traceback.print_exc()
