# Topic Extraction Schema

This reference defines the standard structure for identifying and structuring topics, key themes, and supporting information from any text source (articles, reports, transcripts, etc.).

## 1. Core Fields
Every extracted entry should map to these fields to ensure a structured overview of the content:

| Field | Description | Example |
| :--- | :--- | :--- |
| **Topic/Theme** | The high-level category or subject area. | "Security", "AI Ethics", "Water Crisis" |
| **Key Points** | A concise list of the most important takeaways. | "150% tax deduction for EVs.", "SANDF deployment." |
| **Supporting Evidence** | Direct quotes or data points that validate the key point. | "From March this year, we will introduce..." |
| **Entities** | People, organizations, or locations involved. | "SAPS", "National Treasury", "Cape Town" |
| **Timeline/Context** | Any specific dates, deadlines, or situational context. | "By 2030", "mid-2026", "National Disaster" |
| **Impact/Reasoning** | The intended outcome or significance of the topic. | "To promote a green transition." |

## 2. Trigger Patterns
When scanning text, look for:
- **Major Headers:** High-level section titles.
- **Action Verbs:** *"will"*, *"committed"*, *"directed"*, *"launching"*.
- **Quantitative Data:** Currencies, percentages, headcounts.
- **Problem-Solution Pairs:** Text describing a challenge and its corresponding response.

## 3. Extraction Strategy
1. **Initial Scan:** Identify the main pillars and create a thematic table of contents.
2. **Chunked Analysis:** Use overlapping windows (200 lines, 50-line overlap) to extract detail without losing context.
3. **Synthesis:** Combine similar points into a single "Topic" entry to avoid redundancy in the final CSV.
