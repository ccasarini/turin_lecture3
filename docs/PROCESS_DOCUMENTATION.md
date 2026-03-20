# SONA 2026 Analysis: Process Documentation

## 1. Objective & Overview
The goal of this project is to provide a structured, traceable, and queryable dataset of commitments made by President Cyril Ramaphosa during the **2026 State of the Nation Address (SONA)**. This documentation ensures that analysts can verify any entry in the final CSV against the original text.

## 2. Source Material
- **File:** `process/RamaphosaCommitments2026.txt`
- **Speech Date:** February 12, 2026
- **Context:** The first SONA delivered by the Government of National Unity (GNU) in 2026, focusing on economic growth, security, and service delivery.

## 3. Methodology
The analysis followed a multi-phase extraction and structuring process, utilizing the **Topic Extractor** skill guidelines.

### Phase 1: High-Level Summarization
A high-level review of the speech was performed to identify primary policy pillars. This resulted in `process/summary.md`, which categorizes the address into key themes like Security, Infrastructure, Economy, and Health.

### Phase 2: Granular Extraction Strategy
The analysis uses a combination of scripts to parse the text:
- **Chunking:** The speech is split into overlapping windows (200 lines per chunk, 50-line overlap) to ensure no context is lost.
- **Pattern Matching:** The extraction focuses on action-oriented keywords such as *"will"*, *"committed"*, *"directed"*, *"establishing"*, and *"launching"*.
- **Tooling:** A specialized script `process/extract_promises.py` (based on the `topic-extractor/scripts/extract_topics.py` boilerplate) was used to generate the final dataset.

### Phase 3: Structured Data Mapping
Each extracted commitment is mapped to the standard Topic Extraction Schema in `process/topics.csv`:
- **Topic/Theme:** The high-level category.
- **Key Points:** A concise summary of the promise.
- **Supporting Evidence:** The original verbatim text from the speech.
- **Entities:** The department or agency responsible.
- **Timeline/Context:** Specific deadlines or situational context.
- **Impact/Reasoning:** The stated justification or intended outcome.

## 4. File Manifest
- `/process/RamaphosaCommitments2026.txt`: The primary raw data source.
- `/process/extract_promises.py`: The Python script used to parse and structure the commitments into the new schema.
- `/process/topics.csv`: The final dataset containing 30+ distinct commitments following the Topic Extraction Schema.
- `/process/commitments.csv`: Legacy dataset with a simplified schema.
- `/process/summary.md`: A thematic overview for quick reference.
- `/docs/PROCESS_DOCUMENTATION.md`: This document for traceability.

## 5. Traceability & Verification
To ensure 100% accuracy, every entry in `process/topics.csv` includes a `Supporting Evidence` field. 
- **Validation Step:** Copy any quote from the CSV and use `grep` or a text editor's search function on `process/RamaphosaCommitments2026.txt` to confirm the context.
- **Automation:** The `process/extract_promises.py` script can be re-run to regenerate the CSV.

## 6. Usage Instructions
1. **To extend the analysis:** Modify the `promises` list in `process/extract_promises.py` to include new identified promises.
2. **To update the dataset:** Run `python3 process/extract_promises.py`.
3. **To query the data:** Import `process/topics.csv` into Excel, Power BI, or a Python Pandas environment.
