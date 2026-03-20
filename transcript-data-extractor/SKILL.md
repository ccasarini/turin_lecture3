---
name: transcript-data-extractor
description: Extract and structure commitments, policies, and data from transcripts (speeches, briefings, etc.) into a CSV format. Use when you need to analyze large text documents for specific action-oriented promises or quantitative targets.
---

# Transcript Data Extractor

This skill provides a standardized workflow for converting raw speech or briefing transcripts into structured, queryable data.

## 1. Quick Start
When a transcript analysis is requested:
1.  **Read the source text:** Identify the primary pillars or themes.
2.  **Refer to the Extraction Schema:** Use `references/extraction_schema.md` for definitions of core fields (Concise Description, Entity, Amount, Timeline, Exact Quotes, Reasoning).
3.  **Generate a specialized script:** Use `scripts/extract_transcript_data.py` as a boilerplate for creating your extraction script.

## 2. Extraction Workflow

### Phase 1: High-Level Summarization
- Scan the text for thematic chapters (e.g., Security, Health, Economy).
- Summarize these chapters in a high-level `summary.md` to provide context.

### Phase 2: Chunking & Deep Extraction
- Split the transcript into overlapping chunks (200 lines with 50 lines overlap) to avoid losing context between breaks.
- Use a dedicated Python script (patterned after `scripts/extract_transcript_data.py`) to map identified commitments into the extraction schema.

### Phase 3: Traceability & Organization
- **Traceability:** For every entry in the resulting CSV, the `Exact Quotes` field must be present to allow verification against the source.
- **Documentation:** Create a `PROCESS_DOCUMENTATION.md` in a `docs/` folder to explain the methodology to other analysts.
- **Cleanup:** Move the raw transcript, the script, the CSV output, and the summary into a `process/` directory to maintain a clean workspace.

## 3. Reference Material
- See [references/extraction_schema.md](references/extraction_schema.md) for field definitions and trigger patterns.
- Use [scripts/extract_transcript_data.py](scripts/extract_transcript_data.py) for the core processing logic.
