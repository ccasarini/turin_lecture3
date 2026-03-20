---
name: topic-extractor
description: Identify and structure themes, key points, and supporting information from any text (reports, articles, transcripts, etc.) into a CSV format. Use when you need to analyze a large document for structured insights.
---

# Topic Extractor

This skill provides a standardized workflow for converting raw text into structured, queryable data.

## 1. Quick Start
When a topic analysis is requested:
1.  **Read the source text:** Identify the primary pillars or themes.
2.  **Refer to the Topic Schema:** Use `references/topic_schema.md` for definitions of core fields (Topic/Theme, Key Points, Supporting Evidence, Entities, Timeline/Context, Impact/Reasoning).
3.  **Generate a specialized script:** Use `scripts/extract_topics.py` as a boilerplate for creating your extraction script.

## 2. Extraction Workflow

### Phase 1: High-Level Summarization
- Scan the text for thematic chapters or sections.
- Summarize these chapters in a high-level `summary.md` to provide context.

### Phase 2: Chunking & Deep Extraction
- Split the text into overlapping chunks (200 lines with 50 lines overlap) to avoid losing context between breaks.
- Use a dedicated Python script (patterned after `scripts/extract_topics.py`) to map identified topics into the extraction schema.

### Phase 3: Traceability & Organization
- **Traceability:** For every entry in the resulting CSV, the `Supporting Evidence` field must be present to allow verification against the source.
- **Documentation:** Create a `PROCESS_DOCUMENTATION.md` in a `docs/` folder to explain the methodology to other analysts.
- **Cleanup:** Move the raw text, the script, the CSV output, and the summary into a `process/` directory to maintain a clean workspace.

## 3. Reference Material
- See [references/topic_schema.md](references/topic_schema.md) for field definitions and trigger patterns.
- Use [scripts/extract_topics.py](scripts/extract_topics.py) for the core processing logic.
