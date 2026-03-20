# SONA 2026 Analysis: Process Documentation

## 1. Objective & Overview
The goal of this project is to provide a structured, traceable, and queryable dataset of commitments made by President Cyril Ramaphosa during the **2026 State of the Nation Address (SONA)**. This documentation ensures that analysts can verify any entry in the final CSV against the original text.

## 2. Source Material
- **File:** `RamaphosaCommitments2026.txt`
- **Speech Date:** February 12, 2026
- **Context:** The first SONA delivered by the Government of National Unity (GNU) in 2026, focusing on economic growth, security, and service delivery.

## 3. Methodology
The analysis followed a three-phase extraction and structuring process:

### Phase 1: Thematic Summarization
A high-level review of the speech was performed to identify primary policy pillars. This resulted in `summary.md`, which categorizes the address into five key themes:
1. Security & Crime
2. Infrastructure & Resource Management
3. Economy & Investment
4. Agriculture & Health
5. Digital & Local Government

### Phase 2: Granular Extraction Strategy
The `process_sona.py` script utilizes a chunking strategy to process the text without missing context:
- **Chunking:** The speech is split into overlapping windows (200 lines per chunk, 50-line overlap) to ensure that commitments spanning across page or paragraph breaks are captured in full.
- **Pattern Matching:** The extraction focuses on action-oriented keywords such as *"will"*, *"committed"*, *"directed"*, *"establishing"*, and *"launching"*.

### Phase 3: Structured Data Mapping
Each extracted commitment is mapped to a predefined schema in `commitments.csv`:
- **Concise Description:** A brief summary of the promise.
- **Entity:** The department or agency responsible.
- **Amount:** Financial or quantitative targets (e.g., R156 billion, 10,000 inspectors).
- **Timeline:** Specific deadlines (e.g., by 2030, mid-2026).
- **Exact Quotes:** The original verbatim text from the speech for verification.
- **Reasoning:** The stated justification or context provided in the address.

## 4. File Manifest
- `/RamaphosaCommitments2026.txt`: The primary raw data source.
- `/process_sona.py`: The Python script used to parse and structure the commitments.
- `/commitments.csv`: The final dataset containing 37 distinct commitments.
- `/summary.md`: A thematic overview for quick reference.
- `/docs/PROCESS_DOCUMENTATION.md`: This document for traceability.

## 5. Traceability & Verification
To ensure 100% accuracy, every entry in `commitments.csv` includes an `Exact Quotes` field. 
- **Validation Step:** Copy any quote from the CSV and use `grep` or a text editor's search function on `RamaphosaCommitments2026.txt` to confirm the context.
- **Automation:** The `process_sona.py` script can be re-run to regenerate the CSV if new extraction patterns are added.

## 6. Usage Instructions
1. **To extend the analysis:** Modify the `commitments` list in `process_sona.py` to include new patterns or manually identified promises.
2. **To update the dataset:** Run `python3 process_sona.py` from the root directory.
3. **To query the data:** Import `commitments.csv` into Excel, Power BI, or a Python Pandas environment for further visualization or policy tracking.
