"""
Audit Document Generator Prototype: Software Architecture
=========================================================
Scans the OptArrow source code, extracts docstrings and structure, 
incorporates .drawio diagram context, and uses an LLM to generate 
an ISO 33061-compliant Architecture Overview.

Usage:
    C:/Users/oladi/.local/bin/uv.exe run python prototype_audit_generator.py
"""

import os
import sys
from pathlib import Path
import openai
import json
import xml.etree.ElementTree as ET
import re

# -- Path setup: make sure AutoDoc's src is importable ----------------------
AUTODOC_SRC = Path(__file__).parent / "src"
sys.path.insert(0, str(AUTODOC_SRC))

# -- Configure the .env so the OpenAI key is loaded -------------------------
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / ".env")

# -- AutoDoc internal utilities ----------------------------------------------
from utils.code_block_extraction import GenericCodeBlockExtractor

# -- Configuration -----------------------------------------------------------
OPTARROW_ROOT = Path(r"c:\Users\oladi\Desktop\optArrow-main_2\optArrow-main")
OUTPUT_DIR = Path(r"C:\Users\oladi\Desktop\Thesis\Auto_Doc_GIT_V6\Update the code")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
ARCH_DOC_FILE = OUTPUT_DIR / "Architecture_Overview_ISO33061.md"
MISSING_EVIDENCE_FILE = OUTPUT_DIR / "Missing_Evidence_ISO33061.md"

SUPPORTED_EXTENSIONS = {".py": "python", ".drawio": "xml"}
SKIP_DIRS = {".git", ".venv", "__pycache__", "node_modules", "tests", "scripts"}

def collect_source_files(root: Path) -> list[Path]:
    """Walk the OptArrow repo and collect core source files and diagrams."""
    files = []
    src_dir = root / "src"
    if not src_dir.exists():
        src_dir = root
        
    for path in src_dir.rglob("*"):
        if any(skip in path.parts for skip in SKIP_DIRS):
            continue
        if path.is_file() and path.suffix in SUPPORTED_EXTENSIONS:
            files.append(path)
    return files


def parse_drawio_diagram(file_path: Path) -> str:
    """Extract clean text labels from a .drawio XML file, stripping HTML."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        extracted_texts = []
        # Find all mxCell elements
        for cell in root.iter('mxCell'):
            value = cell.get('value')
            if value:
                # Strip HTML tags using regex
                clean_text = re.sub(r'<[^>]+>', ' ', value)
                # Unescape HTML entities (basic ones)
                clean_text = clean_text.replace('&lt;', '<').replace('&gt;', '>').replace('&nbsp;', ' ').replace('&amp;', '&')
                # Strip remaining HTML tags that were inside escaped ones
                clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
                clean_text = ' '.join(clean_text.split()) # normalize whitespace
                if clean_text.strip():
                    extracted_texts.append("- " + clean_text.strip())
                    
        if not extracted_texts:
            return "(No text found in diagram)"
            
        return "Diagram Text Labels Extracted:\n" + "\n".join(extracted_texts)
    except Exception as e:
        return f"Error parsing diagram: {e}"


def generate_architecture_doc(codebase_summary: str) -> dict:
    """Send the codebase summary to OpenAI to generate ISO 33061 docs."""
    prompt = f"""
You are an expert Software Architect and Quality Assurance Auditor.
I am providing you with a high-level summary of a Python codebase (OptArrow), which includes both Python AST definitions and a raw XML `.drawio` Architecture Diagram.

Your task is to generate TWO outputs compliant with ISO/IEC TS 33061 "Architecture Definition Process".
IMPORTANT: The "Architecture Overview" MUST be formatted as a Formal Narrative Report. 
CRITICAL STYLE RULE: DO NOT use bulleted lists or raw technical dumps to describe components, interfaces, or data flows. You MUST write in flowing prose paragraphs (complete sentences) that tell the story of the architecture. Synthesize the technical details into a readable, high-level narrative that a non-technical auditor can read, while maintaining the deep technical facts (e.g., instead of a bulleted list of endpoints, write a paragraph describing how the FastAPI gateway receives POST requests).

Within this narrative structure, you MUST weave in the ISO 33061 Architecture Requirements:
1. Identify system elements and components explicitly through narrative descriptions.
2. Discuss external and internal interfaces in prose. Specifically, cross-reference the diagram to detail the network layout, including the exact transport layers (e.g., Arrow Flight gRPC vs. Arrow IPC over TCP) and the explicit solvers used (e.g., JuMP, HiGHS).
3. Discuss the allocation of functional requirements to these architectural elements in flowing paragraphs.
4. Describe dynamic behaviors and interactions between components in the Data Flow section. Detail the strict data transformations (e.g., PyArrow Table -> Python Dict -> ConcreteModel) as a narrative journey of the data.

The Architecture Overview MUST include the following image right after the Introduction section:
![OptArrow Architecture](OptArrow_Architecture.png)

Identify Missing Evidence: 
Specify what required architecture documentation is missing in the code (e.g., lack of documented interface protocols, security configurations, deployment definitions).

Return a JSON object with two keys:
"architecture_overview": The full markdown string for the Architecture Overview (Strictly Formal Narrative Prose).
"missing_evidence": The full markdown string for the Missing Evidence.

Codebase Summary:
-----------------
{codebase_summary}
-----------------

Return strictly valid JSON.
"""
    print("  [>] Sending request to OpenAI (this may take a minute)...")
    
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a senior software architect. Output JSON only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )
    
    return json.loads(response.choices[0].message.content.strip())


def run_prototype():
    print("\n" + "="*60)
    print("  AutoDoc Prototype - ISO 33061 Architecture Generator")
    print("="*60)

    source_files = collect_source_files(OPTARROW_ROOT)
    print(f"\n[OK] Found {len(source_files)} core source files in OptArrow\n")

    print("  [>] Extracting structural context from files...")
    codebase_summary_lines = []
    
    for file_path in source_files:
        relative_path = file_path.relative_to(OPTARROW_ROOT)
        codebase_summary_lines.append(f"\n### File: {relative_path}")
        
        try:
            content = file_path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        if file_path.suffix == ".drawio":
            clean_diagram_text = parse_drawio_diagram(file_path)
            codebase_summary_lines.append(f"```text\n{clean_diagram_text}\n```")
            continue

        extractor = GenericCodeBlockExtractor(content, file_path.name)
        code_blocks = extractor.code_block_extractor()

        if code_blocks:
            for block in code_blocks:
                lines = block.strip().split("\n")
                signature = "Unknown function"
                if len(lines) > 1:
                    signature = lines[1].strip()
                codebase_summary_lines.append(f"- Block: {signature}")
        else:
            codebase_summary_lines.append("- (No specific classes/functions found)")

    full_summary = "\n".join(codebase_summary_lines)
    
    # Send to OpenAI
    outputs = generate_architecture_doc(full_summary)
    
    # Save outputs
    with open(ARCH_DOC_FILE, "w", encoding="utf-8") as f:
        f.write(outputs.get("architecture_overview", "Error generating Architecture Overview."))
        
    with open(MISSING_EVIDENCE_FILE, "w", encoding="utf-8") as f:
        f.write(outputs.get("missing_evidence", "Error generating Missing Evidence."))

    print("\n" + "="*60)
    print("  Generation Complete")
    print("="*60)
    print(f"  [OK] Architecture Document saved to: {ARCH_DOC_FILE}")
    print(f"  [OK] Missing Evidence Document saved to: {MISSING_EVIDENCE_FILE}")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_prototype()
