import os
import json
import argparse
import re
from pathlib import Path
import xml.etree.ElementTree as ET
import sys
import openai
from dotenv import load_dotenv

# Configure AutoDoc paths dynamically
CURRENT_DIR = Path(__file__).parent
AUTODOC_ROOT = CURRENT_DIR.parent
AUTODOC_SRC = AUTODOC_ROOT / "src"
sys.path.insert(0, str(AUTODOC_SRC))

try:
    from utils.code_block_extraction import GenericCodeBlockExtractor
except ImportError:
    print("[ERROR] Could not import AutoDoc's GenericCodeBlockExtractor. Ensure the PYTHONPATH is correct.")
    sys.exit(1)

load_dotenv(AUTODOC_ROOT / ".env")


class ContextExtractor:
    """Extracts structural context from the repository using AutoDoc's AST Parser and .drawio parsing."""
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path
        self.extensions = {'.py'}
        self.skip_dirs = {'.git', '.venv', 'tests', 'scripts', '__pycache__', 'node_modules'}

    def collect_files(self) -> list[Path]:
        files = []
        src_dir = self.repo_path / "src"
        if not src_dir.exists():
            src_dir = self.repo_path
            
        for path in src_dir.rglob("*"):
            if any(skip in path.parts for skip in self.skip_dirs):
                continue
            if path.is_file() and (path.suffix in self.extensions or path.suffix == ".drawio"):
                files.append(path)
        return files

    def parse_drawio(self, file_path: Path) -> str:
        try:
            tree = ET.parse(file_path)
            extracted = []
            for cell in tree.getroot().iter('mxCell'):
                value = cell.get('value')
                if value:
                    clean = re.sub(r'<[^>]+>', ' ', value)
                    clean = clean.replace('&lt;', '<').replace('&gt;', '>').replace('&nbsp;', ' ').replace('&amp;', '&')
                    clean = re.sub(r'<[^>]+>', ' ', clean)
                    clean = ' '.join(clean.split()).strip()
                    if clean:
                        extracted.append(f"- {clean}")
            return "Diagram Text:\n" + "\n".join(extracted) if extracted else "(No text found)"
        except Exception as e:
            return f"Error parsing diagram: {e}"

    def extract_context(self) -> str:
        files = self.collect_files()
        print(f"[Extractor] Found {len(files)} targeted files for context extraction.")
        
        summary_lines = []
        for file_path in files:
            rel_path = file_path.relative_to(self.repo_path)
            summary_lines.append(f"\n### File: {rel_path}")
            
            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            if file_path.suffix == ".drawio":
                summary_lines.append(f"```text\n{self.parse_drawio(file_path)}\n```")
                continue

            # Default to AutoDoc AST parsing for code files
            extractor = GenericCodeBlockExtractor(content, file_path.name)
            blocks = extractor.code_block_extractor()
            
            if blocks:
                for block in blocks:
                    lines = block.strip().split("\n")
                    if len(lines) > 1:
                        summary_lines.append(f"- Block: {lines[1].strip()}")
            else:
                summary_lines.append("- (No structural code signatures found)")
                
        return "\n".join(summary_lines)


class StandardIngestionAgent:
    """Step 1: The Standard Ingestion Agent."""
    def __init__(self, model: str = "gpt-4o", temperature: float = 0.1):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.temperature = temperature

    def extract_base_practices(self, markdown_path: Path, process_name: str) -> dict:
        print(f"\n[Agent 1: Ingestion] Reading standard document: {markdown_path.name}")
        standard_content = markdown_path.read_text(encoding="utf-8", errors="ignore")

        print(f"[Agent 1: Ingestion] Extracting requirements for '{process_name}'...")
        prompt = f"""
You are an expert ISO compliance auditor.
TASK:
Find the section corresponding to the process: "{process_name}".
Extract ALL the "Base practices" (e.g., BP1, BP2) and "Process outcomes" associated with this process.

OUTPUT FORMAT:
{{
    "process_name": "{process_name}",
    "outcomes": ["..."],
    "base_practices": [
        {{"id": "BP1", "title": "...", "description": "..."}}
    ]
}}

ISO STANDARD TEXT:
------------------
{standard_content}
------------------
"""
        response = self.client.chat.completions.create(
            model=self.model,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You are a precise data extraction agent. Output valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
        )
        result = json.loads(response.choices[0].message.content.strip())
        print(f"[Agent 1: Ingestion] Successfully extracted {len(result.get('base_practices', []))} Base Practices!")
        return result


class IterativeEvidenceAuditor:
    """Step 2: The Iterative Evidence Auditor."""
    def __init__(self, model: str = "gpt-4o", temperature: float = 0.2):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.temperature = temperature

    def audit_base_practices(self, extracted_bps: dict, codebase_context: str) -> dict:
        print("\n[Agent 2: Auditor] Starting iterative evidence audit...")
        
        audit_results = {
            "process_name": extracted_bps["process_name"],
            "audited_practices": []
        }

        for bp in extracted_bps.get("base_practices", []):
            print(f"  > Auditing {bp['id']}: {bp['title']}...")
            
            prompt = f"""
You are a Lead Software Auditor.
Your task is to evaluate a single Base Practice against the provided structural codebase context.

BASE PRACTICE TO EVALUATE:
ID: {bp['id']}
Title: {bp['title']}
Description: {bp['description']}

INSTRUCTIONS:
1. Search the Codebase Context for evidence satisfying this Base Practice.
2. If evidence exists (e.g., specific functions, components, or diagram labels), list it.
3. If no evidence exists, flag it as Missing.
4. Provide a boolean 'satisfied' flag.

OUTPUT FORMAT (JSON):
{{
    "id": "{bp['id']}",
    "title": "{bp['title']}",
    "satisfied": true/false,
    "evidence_found": "A concise paragraph explaining what evidence was found and where, or detailing exactly what is missing."
}}

CODEBASE CONTEXT:
-----------------
{codebase_context}
-----------------
"""
            response = self.client.chat.completions.create(
                model=self.model,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": "You are an audit mapping agent. Output valid JSON only."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
            )
            
            result = json.loads(response.choices[0].message.content.strip())
            audit_results["audited_practices"].append(result)
            
            status = "PASS" if result.get("satisfied") else "FAIL/MISSING"
            print(f"    - Result: {status}")

        print(f"[Agent 2: Auditor] Completed audit of all {len(audit_results['audited_practices'])} Base Practices.")
        return audit_results


class NarrativeCompilerAgent:
    """Step 3: The Narrative Compiler."""
    def __init__(self, model: str = "gpt-4o", temperature: float = 0.2):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.temperature = temperature

    def compile_report(self, audit_results: dict, codebase_context: str) -> dict:
        print(f"\n[Agent 3: Compiler] Weaving the final documents for '{audit_results['process_name']}'...")
        
        prompt = f"""
You are an expert Technical Writer and QA Lead.
Your task is to generate TWO completely distinct Markdown documents based on the provided Codebase Context and the Audit Findings.

DOCUMENT 1: THE PROCESS DOCUMENT
This is the formal, narrative architectural document for external consumption.
- It MUST read like a natural engineering document.
- It MUST NOT reference "Base Practices", "BP1", "Missing Evidence", or "ISO standards".
- Write it purely based on the structural evidence found in the Codebase Context.

REQUIRED STRUCTURE FOR DOCUMENT 1:
# Architecture Overview
## Introduction
(Write a detailed prose introduction to the system's purpose based on the codebase context).
## System Elements and Components
(Detail the core components explicitly through narrative descriptions. Do not use bullet points).
## Interfaces and Network Layout
(Discuss external and internal interfaces in prose. Cross-reference the Diagram Text to detail network layout and transport layers).
## Allocation of Functional Requirements
(Discuss how responsibilities are allocated across components).
## Data Flow and Dynamic Behaviors
(Describe interactions between components. Detail strict data transformations as a narrative journey of the data).

DOCUMENT 2: THE INTERNAL AUDIT REPORT
This is the strict compliance gap-analysis for the engineering supervisor.
- It MUST include a Markdown table mapping the exact Base Practices (e.g., BP1, BP2) to what was satisfied or missing based on the Audit Findings.
- State clear, actionable recommendations for the developers.

CODEBASE CONTEXT:
{codebase_context}

AUDIT FINDINGS:
{json.dumps(audit_results, indent=2)}

OUTPUT FORMAT:
Return a valid JSON object with exactly two keys:
1. "process_document": The complete Markdown text for Document 1.
2. "audit_report": The complete Markdown text for Document 2.
"""
        response = self.client.chat.completions.create(
            model=self.model,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You are a professional technical writer. Output valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
        )
        
        reports = json.loads(response.choices[0].message.content.strip())
        print("[Agent 3: Compiler] Final documents successfully compiled!")
        return reports


if __name__ == "__main__":
    engine_dir = Path(__file__).parent
    md_file = engine_dir / "iso_33061_standard.md"
    repo_path = Path("C:/Users/oladi/Desktop/Thesis/OPTARROW GIT/optArrow")
    output_dir = engine_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    ingestion_agent = StandardIngestionAgent()
    extracted_data = ingestion_agent.extract_base_practices(md_file, "Architecture definition process")

    extractor = ContextExtractor(repo_path)
    context = extractor.extract_context()

    auditor = IterativeEvidenceAuditor()
    try:
        final_audit = auditor.audit_base_practices(extracted_data, context)
        
        compiler = NarrativeCompilerAgent()
        reports = compiler.compile_report(final_audit, context)
        
        doc1_file = output_dir / "Automated_Architecture_Process.md"
        doc2_file = output_dir / "Automated_Audit_Report_ISO33061.md"
        
        doc1_file.write_text(reports.get("process_document", ""), encoding="utf-8")
        doc2_file.write_text(reports.get("audit_report", ""), encoding="utf-8")
        
        print("\n" + "="*70)
        print(f"[SUCCESS] The fully autonomous pipeline has completed.")
        print(f"Document 1 (Narrative) saved to: {doc1_file}")
        print(f"Document 2 (Audit Matrix) saved to: {doc2_file}")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"Error: {e}")
