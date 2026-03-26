import csv

def extract():
    promises = [
        {
            "Topic/Theme": "Border Security & Immigration",
            "Key Points": "Re-develop border posts via PPPs; 10,000 additional labour inspectors; Electronic Travel Authorisation for all airports and busy land ports.",
            "Supporting Evidence": "Key border posts will be re-developed through public-private partnerships..., hire an additional 10 000 labour inspectors this year., extend the Electronic Travel Authorisation to all international airports.",
            "Entities": "SAPS, DHA, Labour Inspectors",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "Address illegal immigration and secure borders while protecting human rights."
        },
        {
            "Topic/Theme": "Public Service Professionalisation",
            "Key Points": "Public Service Amendment Bill to protect appointments from political interference; mandatory lifestyle audits; central disciplinary registry.",
            "Supporting Evidence": "The Public Service Amendment Bill will protect key appointments from political interference..., Lifestyle audits have been made mandatory..., establishing a central registry for disciplinary cases.",
            "Entities": "Public Service",
            "Timeline/Context": "Ongoing",
            "Impact/Reasoning": "Build an ethical, capable, and developmental state with skilled, honest servants."
        },
        {
            "Topic/Theme": "SOE Governance & Reform",
            "Key Points": "Centralised model for SOE management; National State Enterprises Bill; clear standards for appointments.",
            "Supporting Evidence": "working in a phased manner towards a centralised model for managing our SOE portfolio., finalising the National State Enterprises Bill.",
            "Entities": "Eskom, Transnet, Denel, Prasa",
            "Timeline/Context": "Phased implementation",
            "Impact/Reasoning": "Improve governance, performance, and financial sustainability of state-owned entities."
        },
        {
            "Topic/Theme": "Digital Transformation (MyMzansi)",
            "Key Points": "Launch Digital ID; digitise driver's licenses, Matric certificates, and police statements; remote grant testing on MyMzansi platform.",
            "Supporting Evidence": "DHA will launch a Digital ID..., All these services will be made available on the MyMzansi platform., Citizens will be able to fill out police statements online.",
            "Entities": "DHA, MyMzansi platform, SASSA",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "Harness digital revolution for growth, inclusion, and effective service delivery."
        },
        {
            "Topic/Theme": "International Relations & Trade",
            "Key Points": "Implementation of AfCFTA; use international relations to support manufacturing and export growth.",
            "Supporting Evidence": "contributing to the implementation of the African Continental Free Trade Area..., using our international relations to support domestic economic priorities.",
            "Entities": "AU, SADC, AfCFTA",
            "Timeline/Context": "Ongoing",
            "Impact/Reasoning": "Expand trade between African countries and drive industrialisation."
        },
        {
            "Topic/Theme": "Global Inequality",
            "Key Points": "Launch the International Panel on Inequality building on G20 work.",
            "Supporting Evidence": "working with our international partners towards launching the International Panel on Inequality.",
            "Entities": "G20 Extraordinary Committee on Global Inequality",
            "Timeline/Context": "Not specified",
            "Impact/Reasoning": "Reduce inequality within and between countries."
        },
        {
            "Topic/Theme": "Peacekeeping & Defense",
            "Key Points": "Withdraw troops from UN Mission in DRC to consolidate Defence Force.",
            "Supporting Evidence": "requested the UN to allow us to withdraw our troops from the UN Mission in the Democratic Republic of the Congo.",
            "Entities": "UN, SANDF",
            "Timeline/Context": "Immediate",
            "Impact/Reasoning": "Focus national defense resources and consolidate the SANDF."
        },
        {
            "Topic/Theme": "National Dialogue & Convention",
            "Key Points": "Nationwide public dialogues culminating in a National Convention to guide a national compact and NDP beyond 2030.",
            "Supporting Evidence": "the National Dialogue process will spread across South Africa..., culminate in a National Convention..., guide the formulation of... the next phase of our National Development Plan beyond 2030.",
            "Entities": "Eminent Persons Group, Steering Committee",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "Build national consensus and a long-term plan for the country."
        },
        {
            "Topic/Theme": "Investment Targets",
            "Key Points": "Target of raising R2 trillion in new investments; hosting 6th SA Investment Conference.",
            "Supporting Evidence": "We have now set ourselves a target of raising R2 trillion in new investments over the next five years., hosting the sixth South Africa Investment Conference on 31 March 2026.",
            "Entities": "South Africa Investment Conference",
            "Timeline/Context": "Next 5 years / 31 March 2026",
            "Impact/Reasoning": "Drive inclusive economy and job creation."
        },
        {
            "Topic/Theme": "Small Business Support (SMEs)",
            "Key Points": "R2.5 billion in funding for 180,000 SMEs; R1 billion in guarantees; Business Licensing Bill to simplify startup process.",
            "Supporting Evidence": "provide more than R2.5 billion in funding..., final Bill makes it easier... to start and run a small business.",
            "Entities": "SMEs, Women-and youth-led businesses",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "Back those who create opportunity and reduce bureaucratic hurdles."
        },
        {
            "Topic/Theme": "Economic Transformation & B-BBEE",
            "Key Points": "Reviewing B-BBEE framework to refine, re-align, and strengthen it.",
            "Supporting Evidence": "undertaking a review to refine, re-align and strengthen our Broad-Based Black Economic Empowerment framework.",
            "Entities": "B-BBEE framework",
            "Timeline/Context": "Not specified",
            "Impact/Reasoning": "Drive sustained growth and correct past injustices."
        },
        {
            "Topic/Theme": "Youth Employment (YES & SA Youth)",
            "Key Points": "Regulatory changes for YES; expansion of public employment programmes (EPWP, CWP, Stimulus).",
            "Supporting Evidence": "introduce regulatory changes that will make it much easier for businesses to participate in the YES programme..., expand our public employment programmes.",
            "Entities": "YES, SA Youth, EPWP, CWP",
            "Timeline/Context": "Coming year",
            "Impact/Reasoning": "Create work and learning opportunities on a large scale."
        },
        {
            "Topic/Theme": "Disability Inclusion",
            "Key Points": "Increase employment equity for persons with disabilities to 7%; 7% preferential procurement target.",
            "Supporting Evidence": "increase employment equity targets of persons with disabilities in the Public Service to 7% by 2030, and to mandate a 7% preferential procurement target.",
            "Entities": "Public Service, Government entities",
            "Timeline/Context": "By 2030",
            "Impact/Reasoning": "Ensure no one is left behind in the economy."
        },
        {
            "Topic/Theme": "Education & ECD",
            "Key Points": "Compulsory Grade R; mass registration of ECD facilities (Bana Pele).",
            "Supporting Evidence": "expanding access to early childhood development (ECD) through the Bana Pele mass registration..., By making Grade R compulsory.",
            "Entities": "ECD Facilities, Bana Pele",
            "Timeline/Context": "Not specified",
            "Impact/Reasoning": "Establish a firm foundation for learning in early years."
        },
        {
            "Topic/Theme": "Skills Revolution & TVET",
            "Key Points": "Dual training model; reform SETAs; TVETs as primary sites for occupational training; increase skills levy return to 40%.",
            "Supporting Evidence": "implement a dual training model..., Technical and Vocational Education and Training (TVET) colleges as the primary sites..., increase the proportion of the skills development levy returned to employers... to 40%.",
            "Entities": "SETAs, TVET Colleges",
            "Timeline/Context": "Not specified",
            "Impact/Reasoning": "Align skills development with economic needs."
        },
        {
            "Topic/Theme": "Higher Education",
            "Key Points": "Build more universities and TVETs; address student accommodation shortage.",
            "Supporting Evidence": "build more universities and TVET colleges..., address this challenge [student accommodation], working with financial institutions.",
            "Entities": "Ministry of Higher Education, Ministry of Finance",
            "Timeline/Context": "Immediate",
            "Impact/Reasoning": "Expand opportunities for young people in higher learning."
        },
        {
            "Topic/Theme": "Child Stunting & Malnutrition",
            "Key Points": "End child stunting by 2030; focus on first 1,000 days; clear allocation in MTBPS.",
            "Supporting Evidence": "mission to end child stunting by 2030..., focus on the crucial first 1 000 days of a child’s life.",
            "Entities": "National Strategy to Accelerate Action for Children, MTBPS",
            "Timeline/Context": "By 2030",
            "Impact/Reasoning": "Tackle a massive crisis affecting children's ability to learn and grow."
        },
        {
            "Topic/Theme": "Alcohol Regulation",
            "Key Points": "Curb excessive alcohol use via minimum unit pricing, advertising restrictions, and outlet density limits.",
            "Supporting Evidence": "national government, we have proposed measures... including minimum unit pricing or higher excise duties.",
            "Entities": "Provincial governments",
            "Timeline/Context": "Ongoing consultation",
            "Impact/Reasoning": "Address violence, accidents, and crime linked to alcohol abuse."
        },
        {
            "Topic/Theme": "Social Relief of Distress (SRD) Grant",
            "Key Points": "Continue and redesign SRD grant to support livelihoods and skills.",
            "Supporting Evidence": "this grant will be continued. This year, we will redesign the grant to more effectively support livelihoods.",
            "Entities": "Sassa (implied)",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "Improve lives of the poorest and support productive activity."
        },
        {
            "Topic/Theme": "Housing Model Shift",
            "Key Points": "Shift to supporting people to build/buy/rent own housing via subsidies; R500m for District Six Phase 4.",
            "Supporting Evidence": "introducing a new model for housing... shifting from building houses for people to supporting them..., With R500 million allocated... Phase 4 of construction [District Six].",
            "Entities": "District Six",
            "Timeline/Context": "Ongoing",
            "Impact/Reasoning": "Expand affordable housing and redress past injustices."
        },
        {
            "Topic/Theme": "Healthcare & NHI",
            "Key Points": "Substantial investment in academic hospitals (George Mukhari); rollout of Lenacapavir (HIV) and HPV vaccines.",
            "Supporting Evidence": "undertaking substantial investment in health infrastructure..., massive rollout of Lenacapavir..., HPV vaccine... every young girl between 9 and 15.",
            "Entities": "NHI, George Mukhari Hospital",
            "Timeline/Context": "Ongoing",
            "Impact/Reasoning": "Build a healthy nation and eliminate HIV/cervical cancer."
        },
        {
            "Topic/Theme": "Gender-Based Violence (GBVF)",
            "Key Points": "GBVF classified as a national disaster; Social Workers in police stations; scale up survivor support.",
            "Supporting Evidence": "Last year, we classified gender-based violence and femicide (GBVF) as a national disaster., placement of Social Workers in police stations.",
            "Entities": "National Strategic Plan on GBVF",
            "Timeline/Context": "Ongoing",
            "Impact/Reasoning": "Coordinate response and direct efforts toward impactful interventions."
        },
        {
            "Topic/Theme": "Economic Reform (Operation Vulindlela)",
            "Key Points": "Accelerating economic reform, opening investment and competition; transforming electricity, water, and logistics sectors.",
            "Supporting Evidence": "Through Operation Vulindlela, we have made significant progress in accelerating economic reform and opening the way for investment and competition., we are working to transform the structure of our economy, to fix our infrastructure and make our electricity, water and logistics sectors more competitive and efficient.",
            "Entities": "Operation Vulindlela",
            "Timeline/Context": "Ongoing",
            "Impact/Reasoning": "Foster economic growth and recovery; improve efficiency in key sectors."
        },
        {
            "Topic/Theme": "Infrastructure Investment",
            "Key Points": "R1 trillion in public investment over three years; largest allocation in history.",
            "Supporting Evidence": "Government has committed more than R1 trillion in public investment over three years to build and maintain infrastructure.",
            "Entities": "Infrastructure Fund",
            "Timeline/Context": "Next 3 years",
            "Impact/Reasoning": "Transformative drive for jobs, productivity, and growth."
        },
        {
            "Topic/Theme": "Infrastructure Funding & PPPs",
            "Key Points": "Innovative funding models including the first-ever infrastructure bond and new PPP regulations.",
            "Supporting Evidence": "Through the Infrastructure Fund and new regulations for public-private partnerships... We launched our first-ever infrastructure bond...",
            "Entities": "Infrastructure Fund",
            "Timeline/Context": "Ongoing",
            "Impact/Reasoning": "Attract investors and fast-track projects in energy, water, transport, and digital."
        },
        {
            "Topic/Theme": "Commercial Courts",
            "Key Points": "Establish specialized courts for commercial matters with dedicated judges.",
            "Supporting Evidence": "we will establish specialised courts for commercial matters with dedicated judges and dedicated court rolls to ensure faster outcomes.",
            "Entities": "Judiciary",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "Prevent delays in critical infrastructure and economic projects."
        },
        {
            "Topic/Theme": "State Property Management",
            "Key Points": "Establish a professional State Property Company to manage state-owned buildings and land.",
            "Supporting Evidence": "This year, we will begin work to establish a professional State Property Company to transform the 88 000 buildings and five million hectares of land.",
            "Entities": "State Property Company",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "Turn state assets into engines of growth and development."
        },
        {
            "Topic/Theme": "Energy Transformation & Renewables",
            "Key Points": "40% of energy from renewables by 2030; restructuring Eskom; establishing independent transmission entity.",
            "Supporting Evidence": "By 2030, more than 40% of our energy supply will come from cheap, clean and renewable energy sources., restructuring Eskom and establishing a fully independent state-owned transmission entity.",
            "Entities": "Eskom, NECC",
            "Timeline/Context": "By 2030 / Report in 3 months",
            "Impact/Reasoning": "Ensure long-term energy security and drive down costs."
        },
        {
            "Topic/Theme": "Grid Expansion & Load Reduction",
            "Key Points": "Commencing independent transmission projects; eradicating load reduction by next year.",
            "Supporting Evidence": "commence the first round of independent transmission projects..., objective of eradicating load reduction by next year.",
            "Entities": "Government of South Africa",
            "Timeline/Context": "Next year",
            "Impact/Reasoning": "Modernise energy system and stabilize local supply."
        },
        {
            "Topic/Theme": "Logistics (Rail & Ports)",
            "Key Points": "Private rail access; major PPPs in port terminals; high-speed rail (Joburg-Musina, Durban-Joburg).",
            "Supporting Evidence": "enabled private rail operators to access our network..., initiate major public-private partnerships in our port terminals and rail corridors..., Request For Proposals... for high-speed rail.",
            "Entities": "Durban Pier 2 Container Terminal",
            "Timeline/Context": "Later this year / Dec 2025 (Durban)",
            "Impact/Reasoning": "Return ports to world-class standards and move volumes from road to rail."
        },
        {
            "Topic/Theme": "Agriculture Support",
            "Key Points": "10,000 new Extension Officers; R7.8 billion for black producers via Blended Finance Scheme.",
            "Supporting Evidence": "We will deploy 10 000 new Extension Officers..., provided R7.8 billion in innovative funding to black producers.",
            "Entities": "Land Bank",
            "Timeline/Context": "Not specified",
            "Impact/Reasoning": "Improve productivity and create opportunities for youth."
        },
        {
            "Topic/Theme": "Foot-and-Mouth Disease (FMD) Response",
            "Key Points": "National vaccination of 14 million cattle (28m vaccines); FMD classified as a National Disaster.",
            "Supporting Evidence": "We have decided to vaccinate the national herd of 14 million cattle., classified foot-and-mouth disease as a national disaster.",
            "Entities": "Department of Agriculture",
            "Timeline/Context": "Next 12 months",
            "Impact/Reasoning": "Mitigate devastation of herds and restore exports."
        },
        {
            "Topic/Theme": "Digital Infrastructure",
            "Key Points": "R50 billion investment in data centres over three years.",
            "Supporting Evidence": "more than R50 billion of investment expected over the next three years.",
            "Entities": "Private sector investors",
            "Timeline/Context": "Next 3 years",
            "Impact/Reasoning": "Support growth of the digital technology sector."
        },
        {
            "Topic/Theme": "Tourism & Digital Visas",
            "Key Points": "Electronic Travel Authorisation (ETA) for all visa-required countries; 24-hour processing.",
            "Supporting Evidence": "extend the Electronic Travel Authorisation System to all countries that require a visa... processed digitally within 24 hours.",
            "Entities": "Department of Home Affairs",
            "Timeline/Context": "Coming year",
            "Impact/Reasoning": "Promote international arrivals and support job creation."
        },
        {
            "Topic/Theme": "Green Economy & EVs",
            "Key Points": "150% tax deduction for New Energy Vehicles (NEVs); battery production support.",
            "Supporting Evidence": "From March this year, we will introduce a 150% tax deduction for investment in new energy vehicles...",
            "Entities": "Just Energy Transition Investment Plan",
            "Timeline/Context": "March this year",
            "Impact/Reasoning": "Pivot economy to lead in global green products."
        },
        {
            "Topic/Theme": "Mining & Critical Minerals",
            "Key Points": "Funding for geological mapping and exploration; local beneficiation of critical minerals.",
            "Supporting Evidence": "dedicating funds towards geological mapping and exploration..., G20 countries supported our proposal to expand local beneficiation.",
            "Entities": "IDC, Frontier Rare Earths Project",
            "Timeline/Context": "Ongoing",
            "Impact/Reasoning": "Harness mineral reserves (iron ore valued at R40 trillion) as a sunrise industry."
        },
        {
            "Topic/Theme": "Anti-Corruption & Institutional Rebuilding",
            "Key Points": "Strengthening anti-corruption laws, rebuilding SARS and Investigating Directorate.",
            "Supporting Evidence": "We are strengthening our anti-corruption laws., The work we have done to rebuild key institutions from state capture is showing results.",
            "Entities": "SARS, Investigating Directorate Against Corruption, FATF",
            "Timeline/Context": "Ongoing",
            "Impact/Reasoning": "Ensuring ethical governance and rule of law."
        },
        {
            "Topic/Theme": "Organised Crime (General Focus)",
            "Key Points": "Stepping up the fight using technology, intelligence, and integrated law enforcement.",
            "Supporting Evidence": "Our primary focus this year is stepping up the fight against organised crime and criminal syndicates using technology, intelligence and integrated law enforcement.",
            "Entities": "Government of National Unity",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "Addressing the immediate threat to democracy and economy."
        },
        {
            "Topic/Theme": "Organised Crime (Gang Violence & Illegal Mining)",
            "Key Points": "Deploying SANDF to support police in Western Cape and Gauteng; tactical plan within days.",
            "Supporting Evidence": "I am deploying the South African National Defence Force (SANDF) to support the police..., I have directed the Minister of Police and the SANDF to develop a tactical plan where our security forces should be deployed within the next few days in the Western Cape and Gauteng...",
            "Entities": "SANDF, Minister of Police, SAPS, Western Cape, Gauteng",
            "Timeline/Context": "Next few days",
            "Impact/Reasoning": "Dismantle criminal networks and stop gang violence."
        },
        {
            "Topic/Theme": "Gun Crime Control",
            "Key Points": "Streamlining firearm legislation and increasing enforcement of gun laws.",
            "Supporting Evidence": "We are going to tackle gun crime by streamlining legislation and regulations on licencing, possessing and trading in firearms and ammunition.",
            "Entities": "Government of South Africa",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "Reduce violent crime and illegal firearm use."
        },
        {
            "Topic/Theme": "Police Capacity Building",
            "Key Points": "Recruitment of 5,500 additional police officers this year.",
            "Supporting Evidence": "We are putting more boots on the ground through the recruitment this year of 5 500 additional police officers...",
            "Entities": "SAPS",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "Strengthening law enforcement visibility and response."
        },
        {
            "Topic/Theme": "Illicit Economy Disruption",
            "Key Points": "Establishing a National Illicit Economy Disruption Programme targeting high-risk sectors (tobacco, fuel, alcohol).",
            "Supporting Evidence": "We are establishing a National Illicit Economy Disruption Programme... will target high-risk sectors like tobacco, fuel, alcohol and other counterfeit products.",
            "Entities": "State agencies, private sector",
            "Timeline/Context": "This year",
            "Impact/Reasoning": "Protecting jobs and industry from counterfeit goods."
        },
        {
            "Topic/Theme": "Police & Criminal Justice Reform",
            "Key Points": "Vetting senior SAPS management, lifestyle audits, and a new criminal justice reform initiative in The Presidency.",
            "Supporting Evidence": "State Security Agency will re-vet the Senior Management of the SAPS... we will use a similar approach [to Operation Vulindlela] to establish a hard-hitting new criminal justice reform initiative.",
            "Entities": "SAPS, State Security Agency, The Presidency, Madlanga Commission",
            "Timeline/Context": "Not specified",
            "Impact/Reasoning": "Ensure an ethical, responsive police service and reform the criminal justice system."
        },
        {
            "Topic/Theme": "Whistle-blower Protection",
            "Key Points": "Introducing the Whistle-Blower Protection Bill to criminalize retaliation and provide support.",
            "Supporting Evidence": "The Whistle-Blower Protection Bill will be introduced in Parliament. Among other things, this will criminalise retaliation and provide psychosocial, legal and financial support.",
            "Entities": "Parliament",
            "Timeline/Context": "Not specified",
            "Impact/Reasoning": "Protect those who speak out against corruption."
        },
        {
            "Topic/Theme": "Procurement Reform",
            "Key Points": "Restructuring procurement to end corruption using technology and new regulations.",
            "Supporting Evidence": "Measures will include the use of technology and the finalisation of new Public Procurement Act regulations by mid-2026.",
            "Entities": "AGSA",
            "Timeline/Context": "mid-2026",
            "Impact/Reasoning": "Eliminate corruption at its source in the procurement system."
        },
        {
            "Topic/Theme": "Water Security & Crisis Management",
            "Key Points": "Elevating water response to a National Water Crisis Committee chaired by the President; R156 billion committed to infrastructure.",
            "Supporting Evidence": "we will now elevate our response to the water crisis to a National Water Crisis Committee, which I will chair., We have committed more than R156 billion... over the next three years.",
            "Entities": "President, National Water Resource Infrastructure Agency",
            "Timeline/Context": "Immediate / Next 3 years",
            "Impact/Reasoning": "Address systemic failures and ensure long-term water security."
        },
        {
            "Topic/Theme": "Water Accountability",
            "Key Points": "Introducing the Water Services Amendment Bill to hold providers accountable; criminal charges against failing officials.",
            "Supporting Evidence": "The Water Services Amendment Bill will enable us to hold water service providers accountable..., move to lay charges against Municipal Managers in their personal capacity.",
            "Entities": "Municipal Managers",
            "Timeline/Context": "Immediate",
            "Impact/Reasoning": "Holding officials responsible for service delivery failures."
        },
        {
            "Topic/Theme": "Local Government Reform",
            "Key Points": "Finalising a revised White Paper on Local Government with a differentiated approach to powers; independent official appointments; targeted support for eThekwini/Joburg.",
            "Supporting Evidence": "in the coming months finalise a revised White Paper on Local Government., senior officials... appointed through an independent process free from political interference., Targeted support... through the Presidential Working Groups on eThekwini and Johannesburg.",
            "Entities": "Traditional and Khoi-San leadership institutions, Presidential Working Groups",
            "Timeline/Context": "Coming months",
            "Impact/Reasoning": "Re-imagining local government for better service delivery."
        },
        {
            "Topic/Theme": "Economic Growth Strategy (MTDP)",
            "Key Points": "Implementing a comprehensive plan focused on digital/green economy and public infrastructure.",
            "Supporting Evidence": "Cabinet has approved a comprehensive implementation plan to drive growth and inclusion.",
            "Entities": "Cabinet",
            "Timeline/Context": "Not specified",
            "Impact/Reasoning": "Revive growth and create quality jobs."
        },
        {
            "Topic/Theme": "Job Creation (Employment Stimulus)",
            "Key Points": "Created over 2.5 million opportunities, mainly for young people and women.",
            "Supporting Evidence": "We have created over 2.5 million opportunities through the Presidential Employment Stimulus, mainly for young people and women.",
            "Entities": "Presidential Employment Stimulus, EPWP, CWP",
            "Timeline/Context": "Past/Ongoing",
            "Impact/Reasoning": "Reducing unemployment and poverty."
        },
        {
            "Topic/Theme": "Social Protection (SRD Grant)",
            "Key Points": "Expanded social protection to reduce food poverty.",
            "Supporting Evidence": "By expanding our social protection system through the Social Relief of Distress (SRD) Grant, we have reduced the number of people living in food poverty.",
            "Entities": "SRD Grant",
            "Timeline/Context": "Ongoing",
            "Impact/Reasoning": "Mitigate hunger and poverty."
        }
    ]

    fieldnames = ['Topic/Theme', 'Key Points', 'Supporting Evidence', 'Entities', 'Timeline/Context', 'Impact/Reasoning']
    
    with open('process/topics.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for p in promises:
            writer.writerow(p)

    print("Comprehensive topics.csv created successfully with 51 promises.")

if __name__ == "__main__":
    extract()
