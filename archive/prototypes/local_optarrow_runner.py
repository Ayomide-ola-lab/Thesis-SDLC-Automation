"""
Local AutoDoc Runner for OptArrow
==================================
Runs AutoDoc's docstring analysis and generation directly against
the local OptArrow repository - no GitHub token required.

Usage:
    Run from inside the autodoc folder:
    C:/Users/oladi/.local/bin/uv.exe run python local_optarrow_runner.py
"""

import json
import os
import sys
from pathlib import Path

# -- Path setup: make sure AutoDoc's src is importable ----------------------
AUTODOC_SRC = Path(__file__).parent / "src"
sys.path.insert(0, str(AUTODOC_SRC))

# -- Configure the .env so the OpenAI key is loaded -------------------------
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / ".env")

# -- AutoDoc internal utilities ----------------------------------------------
from utils.code_block_extraction import GenericCodeBlockExtractor
from utils.docstring_generation import (
    format_docstring_for_language,
    generate_docstring_with_openai,
    DEFAULT_OPENAI_MODEL,
)
from utils.docstring_validation import (
    analyze_docstring_in_blocks,
    analyze_docstring_in_module,
)

# -- Configuration -----------------------------------------------------------
OPTARROW_ROOT = Path(r"c:\Users\oladi\Desktop\optArrow-main_2")
OUTPUT_DIR = Path(__file__).parent / "data" / "local_optarrow_run"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SUPPORTED_EXTENSIONS = {
    ".py": "python",
    ".pyw": "python",
    ".js": "javascript",
    ".jsx": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",
}

# Folders to skip (not source code)
SKIP_DIRS = {".git", ".venv", "__pycache__", "node_modules", ".mypy_cache"}


def collect_source_files(root: Path) -> list[tuple[Path, str]]:
    """Walk the OptArrow repo and collect all supported source files."""
    files = []
    for path in root.rglob("*"):
        # Skip unwanted directories
        if any(skip in path.parts for skip in SKIP_DIRS):
            continue
        if path.is_file() and path.suffix in SUPPORTED_EXTENSIONS:
            language = SUPPORTED_EXTENSIONS[path.suffix]
            files.append((path, language))
    return files


def run_local_analysis():
    """Main entry point: analyse all OptArrow source files locally."""
    print("\n" + "="*60)
    print("  AutoDoc - Local OptArrow Analysis")
    print("="*60)

    source_files = collect_source_files(OPTARROW_ROOT)
    print(f"\n[OK] Found {len(source_files)} supported source files in OptArrow\n")

    all_suggestions = []
    summary_rows = []

    suggested_txt = OUTPUT_DIR / "suggested_docstrings.txt"
    suggested_json = OUTPUT_DIR / "suggested_docstrings.json"

    # Clear previous output
    if suggested_txt.exists():
        suggested_txt.unlink()

    for file_path, language in source_files:
        relative_path = file_path.relative_to(OPTARROW_ROOT)
        print(f"  Analysing: {relative_path}")

        try:
            content = file_path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"     [WARN] Could not read file: {e}")
            continue

        if not content.strip():
            print(f"     [WARN] File is empty, skipping.")
            continue

        extractor = GenericCodeBlockExtractor(content, file_path.name)
        code_blocks = extractor.code_block_extractor()

        if not code_blocks:
            # Check for module-level docstring
            module_docstring = analyze_docstring_in_module(content, language)
            if not module_docstring:
                print(f"     [!] Missing module-level docstring - generating...")
                generated = generate_docstring_with_openai(content, language)
                if generated:
                    formatted = format_docstring_for_language(generated, language)
                    all_suggestions.append({
                        "file_path": str(relative_path),
                        "file_name": file_path.name,
                        "function_name": f"Module: {file_path.name}",
                        "block_type": "module",
                        "line_number": 1,
                        "language": language,
                        "generated_docstring": generated,
                    })
                    with open(suggested_txt, "a", encoding="utf-8") as f:
                        f.write(f"\n# File: {file_path.name}, Path: {relative_path}\n")
                        f.write(f"# Function: Module-level\n")
                        f.write(f"{formatted}\n")
                        f.write("-" * 80 + "\n")
                    summary_rows.append({
                        "file": str(relative_path),
                        "function": f"Module: {file_path.name}",
                        "missing": True,
                        "generated": True
                    })
            else:
                print(f"     [OK] Module docstring already exists.")
                summary_rows.append({
                    "file": str(relative_path),
                    "function": f"Module: {file_path.name}",
                    "missing": False,
                    "generated": False
                })
            continue

        # Analyse each code block
        block_analysis = analyze_docstring_in_blocks(
            code_blocks,
            file_name=file_path.name,
            file_path=str(relative_path),
            language=language,
            suggested_file=str(suggested_txt),
            model=DEFAULT_OPENAI_MODEL,
            existing_suggestions={"exact": {}, "fuzzy": {}},
        )

        blocks_missing = block_analysis.get("blocks_without_docstring", 0)
        blocks_present = block_analysis.get("blocks_with_docstring", 0)
        print(f"     [OK] {blocks_present} with docstring | [!] {blocks_missing} missing")

        for analysis in block_analysis.get("docstring_analysis", []):
            summary_rows.append({
                "file": str(relative_path),
                "function": analysis.get("function_name", ""),
                "missing": analysis.get("missing_docstring", False),
                "generated": "generated_docstring" in analysis
            })
            if analysis.get("generated_docstring"):
                all_suggestions.append({
                    "file_path": str(relative_path),
                    "file_name": file_path.name,
                    "function_name": analysis.get("function_name", ""),
                    "block_type": analysis.get("block_type", ""),
                    "line_number": analysis.get("line_number", 0),
                    "language": language,
                    "generated_docstring": analysis["generated_docstring"],
                })

    # Save JSON summary
    with open(suggested_json, "w", encoding="utf-8") as f:
        json.dump({
            "repo": "optArrow (local)",
            "total_files_analysed": len(source_files),
            "suggestions": all_suggestions,
        }, f, indent=2)

    # Print final summary
    total_missing = sum(1 for r in summary_rows if r["missing"])
    total_generated = sum(1 for r in summary_rows if r["generated"])
    print("\n" + "="*60)
    print("  Analysis Complete")
    print("="*60)
    print(f"  Total functions/modules analysed : {len(summary_rows)}")
    print(f"  [!] Missing docstrings found     : {total_missing}")
    print(f"  [*] Docstrings generated         : {total_generated}")
    print(f"\n  Output saved to:")
    print(f"     {suggested_txt}")
    print(f"     {suggested_json}")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_local_analysis()
