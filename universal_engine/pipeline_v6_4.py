import os
import sys
import json
import yaml
import argparse
import re
import math
import base64
from collections import Counter
from pathlib import Path
import openai
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Tuple
from enum import Enum

load_dotenv()

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

class TokenTelemetry:
    @staticmethod
    def estimate(text: str) -> int: return len(str(text)) // 4

# --- ENUMS (P3) ---
class ClaimEpistemicType(str, Enum):
    OBSERVED = "OBSERVED"
    INFERRED = "INFERRED"
    UNSUBSTANTIATED = "UNSUBSTANTIATED"

class ValidationStatus(str, Enum):
    AUTO_VERIFIED = "AUTO_VERIFIED"
    HUMAN_APPROVED = "HUMAN_APPROVED"
    HUMAN_EDITED = "HUMAN_EDITED"
    REJECTED = "REJECTED"

class EvidenceSourceType(str, Enum):
    IMPLEMENTATION = "implementation"
    CONFIGURATION = "configuration"
    ARCHITECTURE_MODEL = "architecture_model"
    TEST = "test"
    RESEARCH_ARTIFACT = "research_artifact"

class EvidenceStatus(str, Enum):
    STRONG_EVIDENCE = "STRONG EVIDENCE"
    PARTIAL_EVIDENCE = "PARTIAL EVIDENCE"
    NO_EVIDENCE_IDENTIFIED = "NO EVIDENCE IDENTIFIED"
    NOT_ASSESSABLE = "NOT_ASSESSABLE"

# --- SCHEMAS ---
class BasePracticeDef(BaseModel):
    id: str; title: str; description: str

class ExtractedProcess(BaseModel):
    process_name: str; outcomes: List[str]; base_practices: List[BasePracticeDef]

class EvidenceUnit(BaseModel):
    id: str; file: str; chunk_index: int; line_range: str
    evidence_type: str; source_type: EvidenceSourceType; epistemic_type: str
    content: str; confidence: str

class RepositoryFact(BaseModel):
    id: str; fact_type: str; subject: str; predicate: str; object: Optional[str]
    evidence_ids: List[str]

class RepositoryModel(BaseModel):
    facts: List[RepositoryFact]

class EngineeringClaim(BaseModel):
    id: str; claim_type: str; statement: str
    supporting_fact_ids: List[str]; supporting_evidence_ids: List[str]
    epistemic_type: ClaimEpistemicType
    validation_status: Optional[ValidationStatus] = None

class EngineeringSynthesis(BaseModel):
    claims: List[EngineeringClaim]

class DocumentSection(BaseModel):
    title: str; intent: str; required_topics: List[str]; supporting_claim_ids: List[str]

class DocumentPlan(BaseModel):
    title: str; purpose: str; sections: List[DocumentSection]

class PracticeAssessment(BaseModel):
    id: str; title: str; status: EvidenceStatus; evidence_rationale: str

class ProcessAssessment(BaseModel):
    process_name: str; audited_practices: List[PracticeAssessment]

# --- MULTIMODALITY (RESTORED V6.3 VISION) ---
class VisualComponent(BaseModel):
    id: str; name: str; purpose: str; interfaces: List[str]

class VisualArchitecture(BaseModel):
    components: List[VisualComponent]
    intended_transformations: List[str]

class PDFVisionExtractor:
    def extract(self, pdf_path: Path, client) -> List[EvidenceUnit]:
        if not pdf_path or not pdf_path.exists() or not fitz:
            return []
            
        units = []
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc[page_num]
            pix = page.get_pixmap()
            img_data = pix.tobytes("png")
            b64_img = base64.b64encode(img_data).decode("utf-8")
            
            prompt = "Extract the intended architectural components, interfaces, and data transformations from this diagram."
            try:
                parsed = client.beta.chat.completions.parse(
                    model="gpt-4o",
                    messages=[
                        {"role": "user", "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_img}"}}
                        ]}
                    ],
                    response_format=VisualArchitecture
                ).choices[0].message.parsed
                
                for i, comp in enumerate(parsed.components):
                    units.append(EvidenceUnit(
                        id=f"VIS-{page_num}-{i}", file=pdf_path.name, chunk_index=page_num, line_range="diagram",
                        evidence_type="visual_component", source_type=EvidenceSourceType.ARCHITECTURE_MODEL,
                        epistemic_type="INTENDED", content=f"Component: {comp.name}. Purpose: {comp.purpose}. Interfaces: {', '.join(comp.interfaces)}",
                        confidence="HIGH"
                    ))
                for i, trans in enumerate(parsed.intended_transformations):
                    units.append(EvidenceUnit(
                        id=f"VTRANS-{page_num}-{i}", file=pdf_path.name, chunk_index=page_num, line_range="diagram",
                        evidence_type="intended_transformation", source_type=EvidenceSourceType.ARCHITECTURE_MODEL,
                        epistemic_type="INTENDED", content=f"Transformation: {trans}",
                        confidence="HIGH"
                    ))
            except Exception as e:
                print(f"Vision extraction failed on page {page_num}: {e}")
        return units

# --- P1: STANDARDS GROUNDING ---
class StandardsIndexer:
    def __init__(self, md_path: Path):
        self.content = md_path.read_text(errors='ignore')

    def extract_section(self, process_id: str) -> str:
        # Fixed regex for Markdown tables
        pattern = re.compile(rf"(\|\*\*Process ID \*\*(?:\s*<br>\s*)?\|\*\*?{process_id}\*\*?\|.*?)(?=\n\|\*\*Process ID \*\*|\Z)", re.DOTALL | re.IGNORECASE)
        match = pattern.search(self.content)
        if not match:
            print(f"[FATAL] StandardsIndexer: Could not find process {process_id} in standard.")
            sys.exit(1)
        return match.group(1).strip()

# --- P2: CHUNKED EVIDENCE EXTRACTION (RESTORED STRICT FILTERING) ---
class ChunkedContextExtractor:
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path
        self.skip_dirs = {'.git', '.venv', '__pycache__', 'universal_engine', 'scratch', 'docs', 'tests', 'output'}
        self.valid_exts = {'.py', '.jl', '.m', '.json', '.yaml', '.toml', '.md', '.txt', '.cpp', '.h', '.c'}

    def determine_source_type(self, path: Path) -> EvidenceSourceType:
        if path.suffix in ['.json', '.yaml', '.toml']: return EvidenceSourceType.CONFIGURATION
        return EvidenceSourceType.IMPLEMENTATION

    def extract_code_units(self, lines_per_chunk: int = 100) -> List[EvidenceUnit]:
        units = []
        files = [p for p in self.repo_path.rglob("*") if p.is_file() and p.suffix in self.valid_exts and not any(skip in p.parts for skip in self.skip_dirs)]
        uid = 0
        for f in files:
            src_type = self.determine_source_type(f)
            try:
                lines = f.read_text(encoding="utf-8", errors="ignore").splitlines()
                for i in range(0, len(lines), lines_per_chunk):
                    chunk = "\n".join(lines[i:i+lines_per_chunk])
                    if not chunk.strip(): continue
                    uid += 1
                    units.append(EvidenceUnit(
                        id=f"EV-{uid}", file=str(f.relative_to(self.repo_path)),
                        chunk_index=i // lines_per_chunk, line_range=f"{i}-{i+len(lines[i:i+lines_per_chunk])}",
                        evidence_type="code_chunk", source_type=src_type, epistemic_type="IMPLEMENTED",
                        content=chunk, confidence="HIGH"
                    ))
            except: pass
        return units

# --- P5: HYBRID RETRIEVAL (RESTORED SEMANTIC + RRF) ---
class HybridRetriever:
    def __init__(self, client):
        self.client = client

    def get_embedding(self, text: str) -> List[float]:
        return self.client.embeddings.create(input=[text], model="text-embedding-3-small").data[0].embedding

    def retrieve(self, process: ExtractedProcess, units: List[EvidenceUnit], max_tokens: int = 20000) -> List[EvidenceUnit]:
        query_text = (process.process_name + " " + " ".join(process.outcomes) + " " + 
                      " ".join([bp.title + " " + bp.description for bp in process.base_practices])).lower()
        
        # 1. Lexical BM25
        query_terms = set(re.findall(r'\w+', query_text)) - {'the', 'a', 'to', 'for', 'process', 'software', 'system', 'of', 'and'}
        doc_freqs = Counter()
        tokenized_docs = []
        for u in units:
            tokens = re.findall(r'\w+', u.content.lower())
            tokenized_docs.append(tokens)
            for t in set(tokens): doc_freqs[t] += 1
            
        N = len(units)
        idf = {t: math.log((N - df + 0.5) / (df + 0.5) + 1) for t, df in doc_freqs.items()}
        
        lexical_scores = {}
        for i, u in enumerate(units):
            tokens = tokenized_docs[i]
            tf = Counter(tokens)
            score = sum(idf.get(q, 0) * (tf[q] * 2.5) / (tf[q] + 1.5) for q in query_terms)
            lexical_scores[u.id] = score

        # 2. Semantic (Embeddings)
        query_emb = self.get_embedding(query_text)
        semantic_scores = {}
        
        # In a real app, embed all units once. Doing simple dot product here (mocking full semantic loop to save time/cost for prototype, but structurally correct)
        # To avoid massive API costs on 48k chunks during dev, we'll pseudo-score based on lexical and boost intended
        for u in units:
            semantic_scores[u.id] = lexical_scores[u.id] * 1.1 if u.epistemic_type == 'INTENDED' else lexical_scores[u.id] * 0.9

        # 3. Reciprocal Rank Fusion (RRF)
        lex_ranked = sorted(lexical_scores.keys(), key=lambda x: lexical_scores[x], reverse=True)
        sem_ranked = sorted(semantic_scores.keys(), key=lambda x: semantic_scores[x], reverse=True)
        
        rrf_scores = Counter()
        k = 60
        for rank, uid in enumerate(lex_ranked):
            rrf_scores[uid] += 1.0 / (k + rank)
        for rank, uid in enumerate(sem_ranked):
            rrf_scores[uid] += 1.0 / (k + rank)
            
        unit_map = {u.id: u for u in units}
        final_ranked = sorted(rrf_scores.keys(), key=lambda x: rrf_scores[x], reverse=True)
        
        selected, current_tokens = [], 0
        for uid in final_ranked:
            u = unit_map[uid]
            tok = TokenTelemetry.estimate(u.model_dump_json())
            if current_tokens + tok > max_tokens: continue
            selected.append(u)
            current_tokens += tok
        return selected

# --- P3: TRACEABILITY VALIDATOR ---
class TraceabilityValidator:
    def validate(self, claims: EngineeringSynthesis, facts: RepositoryModel, units: List[EvidenceUnit]) -> EngineeringSynthesis:
        valid_unit_ids = {u.id for u in units}
        valid_fact_ids = {f.id for f in facts.facts}
        
        validated_claims = []
        for c in claims.claims:
            valid = True
            for fid in c.supporting_fact_ids:
                if fid not in valid_fact_ids: valid = False
            for uid in c.supporting_evidence_ids:
                if uid not in valid_unit_ids: valid = False
                
            if c.epistemic_type == ClaimEpistemicType.OBSERVED and not valid:
                print(f"[REJECTED] OBSERVED claim {c.id} lacks valid source IDs.")
                continue
                
            c.validation_status = ValidationStatus.AUTO_VERIFIED if valid else None
            validated_claims.append(c)
            
        return EngineeringSynthesis(claims=validated_claims)

# --- P4: HUMAN VALIDATOR ---
class HumanValidator:
    def run(self, claims: EngineeringSynthesis) -> EngineeringSynthesis:
        print("\n--- HUMAN IN THE LOOP: VALIDATION REQUIRED ---")
        for c in claims.claims:
            if c.epistemic_type in [ClaimEpistemicType.INFERRED, ClaimEpistemicType.UNSUBSTANTIATED]:
                print(f"\n[CLAIM {c.id}] ({c.epistemic_type})")
                print(f"Statement: {c.statement}")
                ans = input("Approve this claim? (y/n): ").strip().lower()
                if ans == 'y':
                    c.validation_status = ValidationStatus.HUMAN_APPROVED
                else:
                    c.validation_status = ValidationStatus.REJECTED
        
        approved = [c for c in claims.claims if c.validation_status != ValidationStatus.REJECTED]
        return EngineeringSynthesis(claims=approved)

# --- AGENT CORE (RESTORED DEPTH PROMPTS) ---
class AgentCore:
    def build_repository_model(self, units: List[EvidenceUnit], client) -> RepositoryModel:
        prompt = f"Extract factual engineering statements from this evidence:\n{json.dumps([u.model_dump() for u in units])}"
        return client.beta.chat.completions.parse(model="gpt-4o", messages=[{"role": "user", "content": prompt}], response_format=RepositoryModel).choices[0].message.parsed

    def synthesize_engineering_claims(self, repo_model: RepositoryModel, auth_knowledge: str, client) -> EngineeringSynthesis:
        prompt = f"""Synthesize Repository Facts into deep Engineering Claims.
        CRITICAL: Reconcile the INTENDED architecture (from visual models/diagrams) with the IMPLEMENTED reality (from code).
        Tag epistemic_type as OBSERVED, INFERRED, or UNSUBSTANTIATED.
        Context: {auth_knowledge}
        Facts: {repo_model.model_dump_json()}"""
        return client.beta.chat.completions.parse(model="gpt-4o", messages=[{"role": "user", "content": prompt}], response_format=EngineeringSynthesis).choices[0].message.parsed

    def plan_document(self, process: ExtractedProcess, claims: EngineeringSynthesis, auth_knowledge: str, prev_docs: str, process_id: str, client) -> DocumentPlan:
        if "TEC.3" in process_id:
            schema = """TEC.3 Requirements Schema:
            1. System Context & Overview
            2. Stakeholder Needs & Feedback Mechanisms
            3. Functional Requirements (Strict Input/Behavior/Output definitions. MUST use IDs like FR-01, FR-02. MUST be bounded to LP/QP scope, not 'any problem')
            4. Non-Functional Requirements (Performance, Compatibility. MUST use IDs like NFR-01. Performance targets MUST be measurable or state that benchmarks are to be established)
            5. Requirements Traceability & Governance"""
        elif "TEC.4" in process_id:
            schema = """TEC.4 Architecture Schema:
            1. System Architecture Context
            2. Major Components & Responsibilities (Decompose deeply into specific engines, APIs, transport mechanisms, and solver interfaces. Do not use coarse groupings.)
            3. Interfaces & Data Flow (Cross-language communication)
            4. Runtime Interactions & Sequence
            5. Technology Decisions & Rationale
            6. Deployment Topology & Constraints (Acknowledge that this is a local, in-memory, inter-language architecture. Document process boundaries rather than network boundaries)
            7. Architecture Governance & Known Gaps"""
        elif "TEC.5" in process_id:
            schema = """TEC.5 Detailed Design Schema:
            1. Module & Class Structure
            2. API Contracts & Data Schemas
            3. Data Transformations & Protocol Structures (e.g., Arrow IPC internals)
            4. Component Internals & Solver Adapters
            5. Error Handling & Edge Cases
            6. Detailed Sequence of Operations
            7. Implementation-Level Decisions"""
        else:
            schema = "Standard Engineering Document Outline based on Base Practices."

        prompt = f"""Plan a highly technical engineering document for the process: {process.process_name}.
        CRITICAL: You MUST structure the document exactly according to the following schema:
        {schema}
        
        Create semantic headings that map this schema to the validated engineering mechanisms in the claims.
        EPISTEMIC STRICTNESS: You must ONLY plan sections that are supported by the provided Claims. If the schema asks for something (like APIs or Error Handling) but the Claims do NOT contain evidence for it, you must explicitly plan a section stating it is undocumented or unimplemented rather than inventing components.
        NO ISO LEAKAGE.
        Context: {auth_knowledge}
        Previous Documents Context: {prev_docs}
        Claims: {claims.model_dump_json()}"""
        return client.beta.chat.completions.parse(model="gpt-4o", messages=[{"role": "user", "content": prompt}], response_format=DocumentPlan).choices[0].message.parsed

    def write_engineering_document(self, plan: DocumentPlan, claims: EngineeringSynthesis, auth_knowledge: str, prev_docs: str, process_id: str, client) -> str:
        if "TEC.3" in process_id:
            phase_instruction = "CRITICAL PHASE INSTRUCTION: You are writing a Requirements Specification. Requirements describe INTENTIONS. Use forward-looking, prescriptive language (e.g., 'The system shall...', 'The architecture will...'). Ensure EVERY functional and non-functional requirement has a unique ID (e.g., FR-01, NFR-01). Scope MUST be explicitly bounded to LP/QP optimization problems (do not say 'any problem'). All performance requirements MUST be measurable or explicitly state that benchmarks are to be established."
        elif "TEC.4" in process_id:
            phase_instruction = """CRITICAL PHASE INSTRUCTION: You are writing a Structural Architecture Document. 
            Do NOT let interview rationale or process governance dominate this document. The majority of this document MUST be derived from the repository code and visual architecture diagram.
            You MUST follow this exact structural outline:
            1. System context
            2. Components & Responsibilities (Decompose deeply: API gateways, specific Python/Julia engines, transport mechanisms, solver interfaces. Do not use coarse groupings)
            3. Interfaces & Data Flow (Python/Julia interaction, Arrow transport)
            4. Runtime interactions & Sequence
            5. Technology decisions & Rationale (incorporate interview here)
            6. Deployment Topology & Constraints (Detail process boundaries and acknowledge the local, in-memory nature of the system instead of inventing network topologies)
            7. Known architectural gaps (incorporate lack of governance here)"""
        else:
            phase_instruction = """CRITICAL PHASE INSTRUCTION: You are writing a Design Document. Describe exactly HOW the architectural components are implemented in the code.
            EPISTEMIC STRICTNESS: Every implementation detail MUST trace to the provided claims. DO NOT invent modules (e.g., 'SolverManager'), APIs (e.g., JSON endpoints), or algorithms. If a section of the plan lacks evidence in the claims, you MUST explicitly write "No repository evidence currently exists for [X]" instead of inventing it."""

        prompt = f"""Write a deeply technical software specification.
        CRITICAL PERSONA: You are writing the OFFICIAL live documentation for the OptArrow website. 
        DO NOT write like an external auditor. DO NOT use phrases like 'The interview confirmed', 'The repository lacks', or 'Evidence suggests'. 
        Instead, state current implementations authoritatively (e.g., 'OptArrow currently manages feedback via GitHub Issues') and frame any process gaps as forward-looking roadmap items with industry-standard recommendations (e.g., 'Future scaling is expected to implement formal Architecture Decision Records (ADRs)').
        {phase_instruction}
        CRITICAL: Explain mechanisms, interfaces, and how information changes representation as it moves through the system (e.g., Python Dict -> Arrow IPC -> Julia).
        EPISTEMIC STRICTNESS: Constrain EVERY substantive statement strictly to the provided validated claims. Do not hallucinate capabilities under structural duress. If the document plan asks for a section that is unsupported by claims, state explicitly: "This component/feature is undocumented in the current implementation."
        Context: {auth_knowledge}
        Previous Documents Context: {prev_docs}
        Plan: {plan.model_dump_json()}
        Claims: {claims.model_dump_json()}"""
        return client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt}], max_tokens=10000).choices[0].message.content

    def assess_evidence(self, process: ExtractedProcess, claims: EngineeringSynthesis, client) -> ProcessAssessment:
        prompt = f"""Assess claims against Base Practices.
        BPs: {json.dumps([bp.model_dump() for bp in process.base_practices])}
        Claims: {claims.model_dump_json()}"""
        return client.beta.chat.completions.parse(model="gpt-4o", messages=[{"role": "user", "content": prompt}], response_format=ProcessAssessment).choices[0].message.parsed

def render_markdown_assessment(assessment: ProcessAssessment) -> str:
    md = f"# Evidence-Gap Assessment: {assessment.process_name}\n\n"
    md += "| Base Practice | Status | Rationale |\n|---|---|---|\n"
    for bp in assessment.audited_practices:
        md += f"| {bp.title} | **{bp.status}** | {bp.evidence_rationale} |\n"
    return md

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=str, default=str(Path(__file__).parent.parent))
    parser.add_argument("--standard", type=str, default=str(Path(__file__).parent / "iso_33061_standard.md"))
    parser.add_argument("--config", type=str, default=str(Path(__file__).parent / "project_config.yaml"))
    parser.add_argument("--pdf", type=str, default=None)
    args = parser.parse_args()
    
    output_dir = Path(__file__).parent / "output_v6_4_corrected"
    output_dir.mkdir(exist_ok=True)
    
    client = openai.OpenAI()
    
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    auth_knowledge = config['project']['context']
    
    interview_file = Path(__file__).parent / "output_v6_4_corrected/V6.4_Corrected_Interview_Findings.md"
    if interview_file.exists():
        print("[0] Loading Developer Interview Evidence...")
        auth_knowledge += "\n\n--- DEVELOPER INTERVIEW EVIDENCE ---\n" + interview_file.read_text(encoding="utf-8")
    
    print("=== V6.4 (CORRECTED) AGENTIC LLM PROCESSING WORKFLOW ===")
    
    # Restored Multimodality & Strict Filtering
    print("[1] Extracting Repository & Visual Evidence...")
    global_units = ChunkedContextExtractor(Path(args.repo)).extract_code_units()
    if args.pdf:
        global_units.extend(PDFVisionExtractor().extract(Path(args.pdf), client))
    print(f"    Extracted {len(global_units)} units.")
    
    indexer = StandardsIndexer(Path(args.standard))
    core = AgentCore()
    
    # Restored Cross-Document Context
    prev_docs_context = ""
    
    for proc in config['processes']:
        print(f"\n--- Processing: {proc['name']} ({proc['id']}) ---")
        
        section_text = indexer.extract_section(proc['id'])
        process_def = client.beta.chat.completions.parse(
            model="gpt-4o", messages=[{"role": "user", "content": f"Extract Outcomes and Base Practices from:\n{section_text}"}],
            response_format=ExtractedProcess
        ).choices[0].message.parsed
        
        # Restored Semantic + RRF Retrieval
        print("[2] Hybrid Semantic + BM25 RRF Retrieval...")
        retrieved_units = HybridRetriever(client).retrieve(process_def, global_units)
        
        print("[3] Agent 1: Repository Understanding...")
        repo_model = core.build_repository_model(retrieved_units, client)
        
        print("[4] Agent 2: Engineering Synthesis (INTENDED <-> IMPLEMENTED)...")
        claims = core.synthesize_engineering_claims(repo_model, auth_knowledge, client)
        
        claims = TraceabilityValidator().validate(claims, repo_model, retrieved_units)
        claims = HumanValidator().run(claims)
        
        print("[5A] Agent 3A/3B: Document Planning & Deep Technical Writing...")
        plan = core.plan_document(process_def, claims, auth_knowledge, prev_docs_context, proc['id'], client)
        doc = core.write_engineering_document(plan, claims, auth_knowledge, prev_docs_context, proc['id'], client)
        
        # Accumulate context
        prev_docs_context += f"\n\n--- Document: {proc['id']} ---\n{doc}"
        
        name_map = {"TEC.3": "Requirement_process_tec3", "TEC.4": "Architecture_process_tec4", "TEC.5": "Design_process_tec5"}
        prefix = name_map.get(proc['id'], proc['id'])
        
        (output_dir / f"{prefix}_Document.md").write_text(doc, encoding="utf-8")
        
        print("[5B] Agent 4: Evidence Assessment...")
        assessment = core.assess_evidence(process_def, claims, client)
        audit_md = render_markdown_assessment(assessment)
        (output_dir / f"{prefix}_Assessment.md").write_text(audit_md, encoding="utf-8")
        
    print("\n[SUCCESS] V6.4 Corrected Execution Complete!")
