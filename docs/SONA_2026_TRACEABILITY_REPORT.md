# SONA 2026: Sequential Extraction Traceability Report

## 1. Objective & Scope
This report documents the structured extraction of policy commitments from the **2026 State of the Nation Address (SONA)** delivered by President Cyril Ramaphosa. To ensure 100% accuracy and context preservation, a **Sequential Cumulative Extraction** methodology was employed. This process allows for multiple AI subagents to process the speech in manageable chunks while maintaining a "running state" of identified topics.

## 2. Cumulative Extraction Methodology
Unlike a single-pass extraction, which may lose context in long documents, this project used a "Step-by-Step State" approach:
1.  The speech was divided into **6 overlapping text chunks** to prevent context loss at chunk boundaries.
2.  Each processing step used the output CSV from the *previous* step as its starting context.
3.  New commitments found in the current chunk were appended or merged with the existing dataset.
4.  This resulted in a series of intermediate files (`step_0.csv` to `step_5.csv`), where each file is a superset of the previous one.

## 3. Data Lineage & Source Mapping
- **Original Source File:** `process/RamaphosaCommitments2026.txt`
- **Segmentation Strategy:** 
    - `process/chunks/chunk_0.txt`
    - `process/chunks/chunk_1.txt`
    - `process/chunks/chunk_2.txt`
    - `process/chunks/chunk_3.txt`
    - `process/chunks/chunk_4.txt`
    - `process/chunks/chunk_5.txt`
- **Final Output File:** `process/step_5.csv` (51 distinct commitments)

## 4. Processing Log (The Traceability Trail)

### Step 0: Initial Foundation
- **Input:** `chunk_0.txt`
- **Output:** `process/step_0.csv`
- **Key Focus:** Security, Early Economy, and Operation Vulindlela.
- **Outcome:** Captured initial commitments related to SANDF deployment and police recruitment.

### Step 1: Criminal Justice & Water
- **Input:** `chunk_1.txt` + `step_0.csv`
- **Output:** `process/step_1.csv`
- **Key Focus:** Illicit economy disruption, Whistle-blower protection, and the start of the Water Crisis response.
- **Outcome:** Added 8 new topics including the National Water Crisis Committee.

### Step 2: Infrastructure & Local Government
- **Input:** `chunk_2.txt` + `step_1.csv`
- **Output:** `process/step_2.csv`
- **Key Focus:** Infrastructure bonds, PPP regulations, and Local Government White Paper.
- **Outcome:** Expanded the dataset with detailed infrastructure funding and municipal reform strategies.

### Step 3: Energy, Logistics & Agriculture
- **Input:** `chunk_3.txt` + `step_2.csv`
- **Output:** `process/step_3.csv`
- **Key Focus:** 40% Renewables by 2030, Eskom restructuring, High-speed rail RFPs, and Foot-and-Mouth Disease response.
- **Outcome:** Major expansion into sectoral reforms and industrial policy.

### Step 4: Digital ID, Education & Health
- **Input:** `chunk_4.txt` + `step_3.csv`
- **Output:** `process/step_4.csv`
- **Key Focus:** Launch of Digital ID (MyMzansi), Compulsory Grade R, Child Stunting, and HIV/HPV vaccine rollouts.
- **Outcome:** Integrated social development and digital transformation pillars.

### Step 5: International Relations & Final Synthesis
- **Input:** `chunk_5.txt` + `step_4.csv`
- **Output:** `process/step_5.csv`
- **Key Focus:** AfCFTA implementation, G20 Inequality Panel, and troop withdrawals from DRC.
- **Outcome:** Completed the full policy landscape of the 2026 SONA.

## 5. Schema Compliance
All extracted data follows the **Topic Extraction Schema** to ensure it is queryable and standardized:
- **Topic/Theme:** High-level policy pillar.
- **Key Points:** Concise takeaways.
- **Supporting Evidence:** Verbatim quotes for verification.
- **Entities:** Departments/Agencies responsible.
- **Timeline/Context:** Deadlines and situational triggers.
- **Impact/Reasoning:** Intended outcome/significance.

## 6. How to Audit the Results
To verify any commitment in the final dataset:
1.  Open `process/step_5.csv`.
2.  Copy the text from the `Supporting Evidence` field.
3.  Search for that quote in `process/RamaphosaCommitments2026.txt`.
4.  To see *when* a topic was identified, compare `step_{i}.csv` with `step_{i-1}.csv`; the new rows in `step_{i}` originate from `chunk_{i}`.

## 7. Final Results Summary
The final synthesis (`process/step_5.csv`) provides a comprehensive view of the GNU's 2026 agenda, encompassing **51 distinct policy commitments** across security, infrastructure, energy, social development, and international relations.
