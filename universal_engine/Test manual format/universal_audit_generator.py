"""
Universal Audit Document Generator
==================================
A reusable Software Engineering framework that generates audit-ready documentation
based on configurable Process/Standard rulebooks (YAML).

Usage:
    C:/Users/oladi/.local/bin/uv.exe run python universal_audit_generator.py --repo <path> --standard <yaml_path> --output <dir>
"""

import os
import sys
import json
import argparse
from pathlib import Path
import xml.etree.ElementTree as ET
import re

import openai
import yaml
from dotenv import load_dotenv

# Configure AutoDoc paths dynamically
CURRENT_DIR = Path(__file__).parent
AUTODOC_ROOT = CURRENT_DIR.parent
AUTODOC_SRC = AUTODOC_ROOT / "src"
sys.path.insert(0, str(AUTODOC_SRC))

load_dotenv(AUTODOC_ROOT / ".env")

try:
    from utils.code_block_extraction import GenericCodeBlockExtractor
except ImportError:
    print("[ERROR] Could not import AutoDoc's GenericCodeBlockExtractor. Ensure the PYTHONPATH is correct.")
    sys.exit(1)


class ConfigLoader:
    """Loads and validates the YAML Rulebook defining the standard and process."""
    @staticmethod
    def load_rulebook(yaml_path: Path) -> dict:
        if not yaml_path.exists():
            raise FileNotFoundError(f"Rulebook not found: {yaml_path}")
        with open(yaml_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)


class ContextExtractor:
    """Extracts structural context from the repository using AutoDoc's AST Parser and custom extensions."""
    def __init__(self, repo_path: Path, rules: dict):
        self.repo_path = repo_path
        self.extensions = set(rules.get('extensions', ['.py']))
        self.skip_dirs = set(rules.get('skip_dirs', ['.git', '.venv']))

    def collect_files(self) -> list[Path]:
        files = []
        src_dir = self.repo_path / "src"
        if not src_dir.exists():
            src_dir = self.repo_path
            
        for path in src_dir.rglob("*"):
            if any(skip in path.parts for skip in self.skip_dirs):
                continue
            if path.is_file() and path.suffix in self.extensions:
                files.append(path)
        return files

    def parse_drawio(self, file_path: Path) -> str:
        """Strips HTML from .drawio diagrams to extract clean text."""
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
        print(f"  [OK] Found {len(files)} targeted files for context extraction.")
        
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


class PromptBuilder:
    """Constructs the Few-Shot and Chain-of-Thought prompt based on the Rulebook."""
    @staticmethod
    def build(rulebook: dict, context: str) -> str:
        pe = rulebook['prompt_engineering']
        
        prompt = f"You are a {pe['role']}.\n\n"
        prompt += f"TASK: Evaluate the codebase for the {rulebook['standard_name']} {rulebook['process_name']}.\n\n"
        
        prompt += "STYLE RULES:\n"
        for rule in pe.get('style_rules', []):
            prompt += f"- {rule}\n"
            
        prompt += "\nREQUIREMENTS TO EVALUATE:\n"
        for req in pe.get('requirements', []):
            prompt += f"- {req}\n"

        prompt += "\nFEW-SHOT EXAMPLES:\n"
        for idx, ex in enumerate(pe.get('few_shot_examples', [])):
            prompt += f"Example {idx+1} Input:\n{ex['example_input']}\n"
            prompt += f"Example {idx+1} Output:\n{ex['example_output']}\n\n"

        if pe.get('chain_of_thought'):
            prompt += "CHAIN OF THOUGHT INSTRUCTION:\n"
            prompt += "You MUST map the code evidence to the requirements step-by-step in your internal thought process before writing the final document.\n\n"

        prompt += "OUTPUT FORMAT:\n"
        prompt += 'Return a JSON object with two keys: "architecture_overview" (the formal markdown narrative) and "missing_evidence" (the markdown matrix of unfulfilled requirements).\n\n'

        prompt += f"CODEBASE EVIDENCE:\n-----------------\n{context}\n-----------------\n"
        return prompt


class LLMClient:
    """Handles the OpenAI API communication."""
    def __init__(self, model: str, temperature: float):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is missing.")
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature

    def generate(self, prompt: str) -> dict:
        print(f"  [>] Sending Prompt to OpenAI ({self.model})...")
        response = self.client.chat.completions.create(
            model=self.model,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You are a specialized auditing engine. Output valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
        )
        return json.loads(response.choices[0].message.content.strip())


class UniversalAuditGenerator:
    """The main orchestration engine."""
    def __init__(self, repo_path: Path, standard_path: Path, output_dir: Path):
        self.repo_path = repo_path
        self.standard_path = standard_path
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def run(self):
        print("\n" + "="*70)
        print("  Universal Audit Generator v2.0")
        print("="*70)
        
        print(f"  [>] Loading Rulebook: {self.standard_path.name}")
        rulebook = ConfigLoader.load_rulebook(self.standard_path)
        
        print(f"  [>] Extracting Context from Repo: {self.repo_path}")
        extractor = ContextExtractor(self.repo_path, rulebook['extraction_rules'])
        context = extractor.extract_context()
        
        print("  [>] Building Universal Prompt Pipeline...")
        prompt = PromptBuilder.build(rulebook, context)
        
        llm = LLMClient(
            model=rulebook['prompt_engineering'].get('model', 'gpt-4o'),
            temperature=rulebook['prompt_engineering'].get('temperature', 0.2)
        )
        outputs = llm.generate(prompt)
        
        # Save Outputs
        out_doc = self.output_dir / f"{rulebook['process_name'].replace(' ', '_')}.md"
        out_ev = self.output_dir / f"Missing_Evidence_{rulebook['standard_name'].replace('/', '_')}.md"
        
        with open(out_doc, "w", encoding="utf-8") as f:
            f.write(outputs.get("architecture_overview", "Error generating document."))
        with open(out_ev, "w", encoding="utf-8") as f:
            f.write(outputs.get("missing_evidence", "Error generating evidence matrix."))

        print("\n" + "="*70)
        print(f"  [OK] Process Document saved: {out_doc}")
        print(f"  [OK] Missing Evidence saved: {out_ev}")
        print("="*70 + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Universal Audit Document Generator")
    parser.add_argument("--repo", required=True, help="Path to the target codebase")
    parser.add_argument("--standard", required=True, help="Path to the YAML rulebook")
    parser.add_argument("--output", required=True, help="Directory to save generated documents")
    
    args = parser.parse_args()
    
    engine = UniversalAuditGenerator(Path(args.repo), Path(args.standard), Path(args.output))
    engine.run()
