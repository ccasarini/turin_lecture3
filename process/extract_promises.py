import csv

def extract():
    promises = [
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
            "Supporting Evidence": "We are putting more boots on the ground through the recruitment this year of 5 500 additional police officers, adding to the 20 000 new officers we announced in previous SoNAs.",
            "Entities": "SAPS",
            "Timeline/Context": "This year (2026)",
            "Impact/Reasoning": "To tackle gun crime and increase enforcement of existing laws."
        },
        {
            "Topic/Theme": "Security & Organized Crime",
            "Key Points": "Establishment of National Illicit Economy Disruption Programme.",
            "Supporting Evidence": "We are establishing a National Illicit Economy Disruption Programme that brings together key state agencies and other stakeholders, including the private sector.",
            "Entities": "State agencies, Private Sector",
            "Timeline/Context": "Ongoing/Immediate",
            "Impact/Reasoning": "To target high-risk sectors like tobacco, fuel, alcohol using data analytics and AI."
        },
        {
            "Topic/Theme": "Security & Organized Crime",
            "Key Points": "Re-vetting and lifestyle audits of SAPS and Metro Police Senior Management.",
            "Supporting Evidence": "The State Security Agency will re-vet the Senior Management of the SAPS and Metro Police departments. The vetting process will include lifestyle audits.",
            "Entities": "State Security Agency, SAPS, Metro Police",
            "Timeline/Context": "Following Madlanga Commission findings",
            "Impact/Reasoning": "To address rampant corruption and abuse of power exposed by the commission."
        },
        {
            "Topic/Theme": "Security & Organized Crime",
            "Key Points": "Introduction of Whistle-Blower Protection Bill.",
            "Supporting Evidence": "The Whistle-Blower Protection Bill will be introduced in Parliament. Among other things, this will criminalise retaliation and provide psychosocial, legal and financial support to whistle-blowers.",
            "Entities": "Parliament",
            "Timeline/Context": "Upcoming legislative session",
            "Impact/Reasoning": "To prevent victimisation of those who speak out against corruption."
        },
        {
            "Topic/Theme": "Security & Organized Crime",
            "Key Points": "Finalisation of new Public Procurement Act regulations.",
            "Supporting Evidence": "Measures will include the use of technology and the finalisation of new Public Procurement Act regulations by mid-2026.",
            "Entities": "Government",
            "Timeline/Context": "By mid-2026",
            "Impact/Reasoning": "To end corruption in the procurement system where most incidents originate."
        },
        {
            "Topic/Theme": "Water Infrastructure",
            "Key Points": "R156 billion investment in water and sanitation infrastructure.",
            "Supporting Evidence": "We have committed more than R156 billion in public funding for water and sanitation infrastructure over the next three years.",
            "Entities": "Government",
            "Timeline/Context": "Over the next three years",
            "Impact/Reasoning": "To ensure long-term water security and address infrastructure neglect."
        },
        {
            "Topic/Theme": "Water Infrastructure",
            "Key Points": "Establishment of National Water Crisis Committee chaired by the President.",
            "Supporting Evidence": "we will now elevate our response to the water crisis to a National Water Crisis Committee, which I will chair.",
            "Entities": "Presidency",
            "Timeline/Context": "Immediate elevation",
            "Impact/Reasoning": "To coordinate all efforts into a single body and deploy technical experts to municipalities."
        },
        {
            "Topic/Theme": "Water Infrastructure",
            "Key Points": "R54 billion incentive for metros to reform services.",
            "Supporting Evidence": "we have introduced a new R54 billion incentive for metros to reform their water, sanitation and electricity services.",
            "Entities": "Metros",
            "Timeline/Context": "Announced",
            "Impact/Reasoning": "To ensure revenue from water usage is reinvested into infrastructure rather than diverted."
        },
        {
            "Topic/Theme": "Governance & Local Government",
            "Key Points": "Finalisation of revised White Paper on Local Government.",
            "Supporting Evidence": "we will, in the coming months finalise a revised White Paper on Local Government.",
            "Entities": "Government",
            "Timeline/Context": "In the coming months",
            "Impact/Reasoning": "To provide solutions for an effective local government system and reimagined municipal functions."
        },
        {
            "Topic/Theme": "Infrastructure & Economy",
            "Key Points": "R1 trillion public investment in infrastructure.",
            "Supporting Evidence": "Government has committed more than R1 trillion in public investment over three years to build and maintain infrastructure.",
            "Entities": "Government",
            "Timeline/Context": "Over three years",
            "Impact/Reasoning": "Largest allocation in history to build jobs, productivity, and growth."
        },
        {
            "Topic/Theme": "Infrastructure & Economy",
            "Key Points": "Establishment of specialized commercial courts.",
            "Supporting Evidence": "we will establish specialised courts for commercial matters with dedicated judges and dedicated court rolls to ensure faster outcomes",
            "Entities": "Judiciary",
            "Timeline/Context": "Immediate/Upcoming",
            "Impact/Reasoning": "To prevent delays in critical projects caused by tender disputes."
        },
        {
            "Topic/Theme": "Infrastructure & Economy",
            "Key Points": "Establishment of a professional State Property Company.",
            "Supporting Evidence": "This year, we will begin work to establish a professional State Property Company to transform the 88 000 buildings and five million hectares of land owned by the State",
            "Entities": "Government",
            "Timeline/Context": "Work begins this year",
            "Impact/Reasoning": "To turn state assets into professionally managed engines of growth."
        },
        {
            "Topic/Theme": "Energy & Green Transition",
            "Key Points": "40% of energy supply from renewable sources by 2030.",
            "Supporting Evidence": "By 2030, more than 40% of our energy supply will come from cheap, clean and renewable energy sources.",
            "Entities": "Energy Sector",
            "Timeline/Context": "By 2030",
            "Impact/Reasoning": "To drive down costs and ensure long-term energy security."
        },
        {
            "Topic/Theme": "Energy & Green Transition",
            "Key Points": "Eradication of load reduction by next year.",
            "Supporting Evidence": "We will work in each province to address transformer overloading... with the objective of eradicating load reduction by next year.",
            "Entities": "Eskom, Provinces",
            "Timeline/Context": "By 2027",
            "Impact/Reasoning": "To modernise the energy system and address local equipment failures."
        },
        {
            "Topic/Theme": "Energy & Green Transition",
            "Key Points": "150% tax deduction for investment in New Energy Vehicles (NEVs).",
            "Supporting Evidence": "From March this year, we will introduce a 150% tax deduction for investment in new energy vehicles",
            "Entities": "National Treasury, SARS",
            "Timeline/Context": "From March 2026",
            "Impact/Reasoning": "To pivot the economy towards green growth and support local battery production."
        },
        {
            "Topic/Theme": "Logistics & Transport",
            "Key Points": "Public-private partnerships in port terminals and rail corridors.",
            "Supporting Evidence": "Later this year, we will initiate major public-private partnerships in our port terminals and rail corridors through a concession model",
            "Entities": "Transnet, Private Sector",
            "Timeline/Context": "Later this year",
            "Impact/Reasoning": "To mobilise private investment while preserving public ownership."
        },
        {
            "Topic/Theme": "Agriculture",
            "Key Points": "Deployment of 10,000 new Extension Officers.",
            "Supporting Evidence": "We will deploy 10 000 new Extension Officers to support farmers and improve agricultural productivity.",
            "Entities": "Department of Agriculture",
            "Timeline/Context": "Upcoming",
            "Impact/Reasoning": "To support farmers and create opportunities for youth."
        },
        {
            "Topic/Theme": "Agriculture",
            "Key Points": "Vaccination of 14 million cattle against Foot-and-Mouth Disease (FMD).",
            "Supporting Evidence": "We have decided to vaccinate the national herd of 14 million cattle. This requires 28 million vaccines over the next 12 months.",
            "Entities": "Department of Agriculture, Private Sector",
            "Timeline/Context": "Next 12 months",
            "Impact/Reasoning": "To address the national disaster of FMD outbreak and lift export bans."
        },
        {
            "Topic/Theme": "Economy & Investment",
            "Key Points": "R2 trillion investment target over five years.",
            "Supporting Evidence": "We have now set ourselves a target of raising R2 trillion in new investments over the next five years.",
            "Entities": "Government",
            "Timeline/Context": "Next five years",
            "Impact/Reasoning": "To build on previous success and drive economic growth."
        },
        {
            "Topic/Theme": "Economy & Investment",
            "Key Points": "R2.5 billion funding for 180,000 SMEs.",
            "Supporting Evidence": "This year, we will provide more than R2.5 billion in funding to over 180 000 small and medium enterprises, and extend a further R1 billion in guarantees.",
            "Entities": "Government",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "To back those who create opportunity, focusing on women and youth-led businesses."
        },
        {
            "Topic/Theme": "Digital Transformation",
            "Key Points": "Launch of Digital ID.",
            "Supporting Evidence": "This year, the DHA will launch a Digital ID to enable safe and secure use of digital services for all South Africans.",
            "Entities": "Department of Home Affairs",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "To enable safe digital services and digitise government functions like driver's licenses and SASSA tests."
        },
        {
            "Topic/Theme": "Education & Skills",
            "Key Points": "Compulsory Grade R.",
            "Supporting Evidence": "By making Grade R compulsory, we are getting all children off to a good start.",
            "Entities": "Basic Education",
            "Timeline/Context": "Implementation phase",
            "Impact/Reasoning": "To establish a firm foundation for learning."
        },
        {
            "Topic/Theme": "Education & Skills",
            "Key Points": "Restoration of skills development levy return to 40%.",
            "Supporting Evidence": "we will increase the proportion of the skills development levy returned to employers, restoring it to its original level of 40%.",
            "Entities": "Department of Higher Education",
            "Timeline/Context": "Upcoming",
            "Impact/Reasoning": "To support effective workplace-based learning."
        },
        {
            "Topic/Theme": "Health & Social Development",
            "Key Points": "Mission to end child stunting by 2030.",
            "Supporting Evidence": "This year, we will embark on a mission to end child stunting by 2030... focusing on the crucial first 1 000 days of a child’s life.",
            "Entities": "Government",
            "Timeline/Context": "By 2030",
            "Impact/Reasoning": "To address the crisis where a quarter of children under five are stunted."
        },
        {
            "Topic/Theme": "Health & Social Development",
            "Key Points": "Redesign of the SRD Grant.",
            "Supporting Evidence": "This year, we will redesign the grant to more effectively support livelihoods, skills development, work opportunities and productive activity.",
            "Entities": "SASSA, Dept of Social Development",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "To transform the grant into an instrument that improves lives beyond just food poverty."
        },
        {
            "Topic/Theme": "Health & Social Development",
            "Key Points": "Rollout of Lenacapavir for HIV prevention.",
            "Supporting Evidence": "we will be undertaking a massive rollout of Lenacapavir, a six-monthly injection that has proven highly effective in preventing HIV transmission.",
            "Entities": "Department of Health",
            "Timeline/Context": "Massive rollout starting",
            "Impact/Reasoning": "To prevent and ultimately eliminate HIV/AIDS."
        },
        {
            "Topic/Theme": "Health & Social Development",
            "Key Points": "HPV vaccine for girls aged 9-15.",
            "Supporting Evidence": "ensure that every young girl between the ages of 9 and 15 receives the HPV vaccine.",
            "Entities": "Department of Health",
            "Timeline/Context": "Immediate/Ongoing",
            "Impact/Reasoning": "To end cervical cancer."
        },
        {
            "Topic/Theme": "Borders & Labor Enforcement",
            "Key Points": "Hiring of 10,000 additional labour inspectors.",
            "Supporting Evidence": "To tighten enforcement, we will hire an additional 10 000 labour inspectors this year.",
            "Entities": "Department of Employment and Labour",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "To crack down on violations of immigration and labour laws."
        },
        {
            "Topic/Theme": "National Dialogue",
            "Key Points": "National Dialogue and National Convention.",
            "Supporting Evidence": "This year, the National Dialogue process will spread across South Africa... These public dialogues will culminate in a National Convention",
            "Entities": "Eminent Persons Group, Steering Committee",
            "Timeline/Context": "Throughout 2026",
            "Impact/Reasoning": "To guide the formulation of a national compact and the next phase of the NDP."
        }
    ]

    fieldnames = ['Topic/Theme', 'Key Points', 'Supporting Evidence', 'Entities', 'Timeline/Context', 'Impact/Reasoning']
    
    with open('process/topics.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for p in promises:
            writer.writerow(p)

    print("Comprehensive topics.csv created successfully.")

if __name__ == "__main__":
    extract()
