# Research Provenance and Historical Iterations

This directory preserves earlier prototypes, deprecated services, and experimental pipeline iterations developed throughout the research project. They are retained for provenance and historical reference.

## Directory Structure

```text
archive/
├── prototypes/           # Early exploration scripts with hardcoded heuristics
├── pipeline_iterations/  # Evolution of the Universal Engine (V5.2 through V6.2)
├── autodoc_service/      # Legacy FastAPI-based source code docstring generation service
└── outputs_history/      # Historical output markdown and report artifacts
```

## Evolution Summary

1. **`prototypes/` (Early AutoDoc & Heuristics):**
   * Contained initial single-script prototypes (`prototype_audit_generator.py`, `local_optarrow_runner.py`) that explored code-block extraction and AST parsing.
   * *Limitation:* Heavily coupled to hardcoded repository paths and manually spoon-fed project knowledge.

2. **`autodoc_service/` (Legacy Web Service):**
   * Built as a containerized FastAPI application with GitHub/GitLab integration, automated Sphinx documentation builds, and docstring PR generation.
   * *Limitation:* Focused purely on code-level documentation without integrating external architectural or standards-based evidence.

3. **`pipeline_iterations/` (V5.2 – V6.2):**
   * **V5.2:** Early structured engine separating extraction from prompt templates.
   * **V6.0–V6.2:** Introduction of multi-agent chaining, visual architecture extraction via PyMuPDF/GPT-4o, and keyword-based retrieval.
   * Led directly to the stabilized **V6.3** pipeline located in `universal_engine/`.

4. **`outputs_history/`:**
   * Archival records of generated markdown specifications and audit matrices across prior pipeline versions.
