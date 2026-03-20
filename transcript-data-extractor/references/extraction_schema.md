# Extraction Schema: Transcript Commitments

This reference defines the standard structure for extracting and structuring data from presidential speeches, policy briefings, or meeting transcripts.

## 1. Core Fields
Every extracted entry should map to these six fields to ensure consistency across different documents:

| Field | Description | Example |
| :--- | :--- | :--- |
| **Concise Description** | A 1-sentence summary of the commitment or point. | "Recruit 5,500 additional police officers." |
| **Entity** | The department, person, or agency responsible. | "SAPS (South African Police Service)" |
| **Amount** | Quantifiable data (currency, staff counts, targets). | "R156 billion", "10,000 inspectors" |
| **Timeline** | Deadlines, start dates, or specific durations. | "By 2030", "mid-2026" |
| **Exact Quotes** | The original verbatim text from the source. | "We are putting more boots on the ground..." |
| **Reasoning** | The justification or intended outcome of the action. | "To tackle gun crime and increase enforcement." |

## 2. Trigger Patterns
When scanning text, prioritize identifying these action-oriented keywords:
- **Directives:** *"I have directed"*, *"I have instructed"*, *"The Minister will"*
- **Commitments:** *"We have committed"*, *"We will"*, *"Government is dedicated to"*
- **Operational:** *"Establishing"*, *"Launching"*, *"Implementing"*, *"Beginning work to"*
- **Financial:** *"R... allocated"*, *"Incentive for..."*, *"Tax deduction for..."*

## 3. Extraction Strategy
1. **Thematic Review:** Scan the whole document for broad pillars (e.g., Economy, Health, Crime).
2. **Context Preservation:** Use overlapping chunks (e.g., 200 lines with 50-line overlap) to ensure continuity.
3. **Traceability:** Always include the `Exact Quotes` field to allow analysts to verify entries.
