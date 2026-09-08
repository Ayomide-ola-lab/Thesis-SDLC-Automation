# Standards Context Directory

This directory contains authoritative software engineering lifecycle standard documents supplied to the pipeline at runtime.

## ISO/IEC TS 33061 Context

The default evaluation in this research utilizes **ISO/IEC TS 33061:2021** (*Information technology — Process assessment — Process assessment model for software life cycle processes*), specifically targeting:
* **Section 5.5.4 (TEC.3):** System/software requirements definition process
* **Section 5.5.5 (TEC.4):** Architecture definition process

### Usage and Licensing Note
ISO/IEC standards are protected by copyright. When deploying or replicating this pipeline in public environments:
1. Ensure you hold an authorized copy or organizational license for ISO/IEC TS 33061.
2. Place the extracted markdown text file in this directory (e.g., `iso_33061_standard.md`).
3. Pass the path explicitly to the pipeline using the `--standard` argument:
   ```bash
   python universal_engine/pipeline_v6_3.py --standard resources/standards/iso_33061_standard.md
   ```
