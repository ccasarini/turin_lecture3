import csv
import re

file_path = 'process/RamaphosaCommitments2026.txt'
with open(file_path, 'r') as f:
    text = f.read()

# Define extraction logic following the new "topic-extractor" skill schema
# schema: Topic/Theme, Key Points, Supporting Evidence, Entities, Timeline/Context, Impact/Reasoning

extracted_topics = [
    {
        "Topic/Theme": "Security & Organized Crime",
        "Key Points": "Deployment of SANDF to Western Cape and Gauteng.",
        "Supporting Evidence": "I am deploying the South African National Defence Force (SANDF) to support the police... within the next few days in the Western Cape and Gauteng to deal with gang violence and illegal mining.",
        "Entities": "SANDF, SAPS, Minister of Police",
        "Timeline/Context": "Within the next few days",
        "Impact/Reasoning": "To strengthen the fight against gang violence and illegal mining."
    },
    {
        "Topic/Theme": "Security & Organized Crime",
        "Key Points": "Recruitment of 5,500 additional police officers.",
        "Supporting Evidence": "We are putting more boots on the ground through the recruitment this year of 5 500 additional police officers.",
        "Entities": "SAPS",
        "Timeline/Context": "This year",
        "Impact/Reasoning": "To tackle gun crime and increase enforcement of existing laws."
    },
    {
        "Topic/Theme": "Infrastructure: Water",
        "Key Points": "R156 billion investment in water and sanitation infrastructure.",
        "Supporting Evidence": "We have committed more than R156 billion in public funding for water and sanitation infrastructure over the next three years.",
        "Entities": "Government",
        "Timeline/Context": "Over the next three years",
        "Impact/Reasoning": "To ensure water security and address systemic failures and neglect of infrastructure."
    },
    {
        "Topic/Theme": "Energy & Green Transition",
        "Key Points": "150% tax deduction for investments in new energy vehicles (NEVs).",
        "Supporting Evidence": "From March this year, we will introduce a 150% tax deduction for investment in new energy vehicles",
        "Entities": "National Treasury, SARS",
        "Timeline/Context": "From March this year",
        "Impact/Reasoning": "To pivot the economy towards green growth and support local production of batteries."
    },
    {
        "Topic/Theme": "Public Health",
        "Key Points": "Massive rollout of Lenacapavir for HIV prevention.",
        "Supporting Evidence": "we will be undertaking a massive rollout of Lenacapavir, a six-monthly injection that has proven highly effective in preventing HIV transmission.",
        "Entities": "Department of Health",
        "Timeline/Context": "Immediate rollout",
        "Impact/Reasoning": "To prevent and ultimately eliminate HIV/AIDS."
    },
    {
        "Topic/Theme": "Governance & Accountability",
        "Key Points": "Introduction of the Whistle-Blower Protection Bill.",
        "Supporting Evidence": "The Whistle-Blower Protection Bill will be introduced in Parliament.",
        "Entities": "Parliament, Government",
        "Timeline/Context": "Upcoming legislative session",
        "Impact/Reasoning": "To prevent victimisation of those who speak out against corruption."
    }
    # (Simplified for demonstration of the new schema)
]

with open('process/topics.csv', 'w', newline='') as csvfile:
    fieldnames = ['Topic/Theme', 'Key Points', 'Supporting Evidence', 'Entities', 'Timeline/Context', 'Impact/Reasoning']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for topic in extracted_topics:
        writer.writerow(topic)

print("Topics CSV created successfully with the new schema.")
