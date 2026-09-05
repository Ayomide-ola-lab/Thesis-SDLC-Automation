# Universal Audit Generator Upgrade

This plan outlines the refactoring of the `prototype_audit_generator.py` script into a robust, reusable Software Engineering framework. Moving away from a hardcoded data-science script, this upgrade will create a universal engine that accepts dynamic inputs (Standards, Processes, Codebases) and outputs audit-ready documentation.

## User Review Required

> [!IMPORTANT]
> Please review the proposed architecture below. Specifically, look at the `YAML Rulebook` structure. Does this configuration format align with your vision of providing "Standards" and "Processes" as dynamic inputs? 

## Proposed Architecture

We will restructure the tool into a modular, function-driven architecture with clear separations of concern:

### 1. The Inputs (Configuration Driven)
Instead of hardcoding ISO 33061 into the Python script, we will create "Rulebooks" (YAML or JSON files). The Python engine will take these rulebooks as input. 

**Example Input Rulebook (`standards/iso33061_architecture.yaml`):**
```yaml
standard: "ISO/IEC TS 33061"
process: "Architecture Definition"
extraction_rules:
  extensions: [".py", ".drawio"]
  skip_dirs: ["tests", "scripts", ".venv"]
prompt_engineering:
  role: "ISO/IEC 33061 Quality Assurance Lead Auditor"
  chain_of_thought: true
  requirements:
    - "BP1: Develop software architectural design"
    - "BP2: Allocate software requirements"
  few_shot_examples:
    - example_input: "def run_server()..."
      example_output: "The system utilizes a FastAPI gateway to initialize the server..."
```

### 2. The Engine (Python Refactor)
We will rewrite the main script into a class-based structure (`UniversalAuditGenerator`) that executes the defined process:
1. **`ConfigLoader`**: Parses the YAML rulebook to determine what standard is being audited.
2. **`ContextExtractor`**: Uses AutoDoc's AST Parser dynamically based on the `extraction_rules` defined in the input.
3. **`PromptBuilder`**: Constructs the complex Few-Shot and Chain-of-Thought prompt by merging the extracted context with the specific `requirements` and `few_shot_examples`.
4. **`LLMClient`**: Executes the OpenAI request and parses the JSON response.

### 3. The Output
The engine will deterministically output the documentation tailored to the specific process requested by the input rulebook, allowing it to seamlessly scale to Requirements, Risk Management, or Testing just by swapping the YAML file.

## Proposed Changes

### Configuration Layer

#### [NEW] `autodoc/standards/iso33061_architecture.yaml`
- A YAML configuration file defining the ISO 33061 Architecture process, rules, and few-shot examples.

### Core Engine

#### [NEW] `autodoc/universal_engine/universal_audit_generator.py`
- A completely modular, object-oriented script that replaces the prototype.
- Contains the `UniversalAuditGenerator` class.
- Accepts command-line arguments for `--repo`, `--standard`, and `--output`.

#### [KEEP] `autodoc/prototype_audit_generator.py`
- We will retain the original hardcoded prototype script for benchmarking, testing, and comparison purposes in your thesis.

## Verification Plan

### Automated Verification
- We will run the new `universal_audit_generator.py` using the `iso33061_architecture.yaml` rulebook against the OptArrow repository.
- We will verify that it successfully extracts the AST, connects to OpenAI, and generates the `Architecture_Overview_ISO33061.md` and `Missing_Evidence_ISO33061.md` outputs.
- We will compare the output quality to ensure the Few-Shot and CoT prompting eliminated bullet-point hallucinations and strictly followed the narrative format.
