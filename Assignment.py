import pandas as pd
import numpy as np
import random

# Define locations and associated colleges
locations_colleges = {
    "Mumbai": [
        "University of Mumbai", "Indian Institute of Technology Bombay (IIT-B)",
        "Tata Institute of Social Sciences (TISS)", "Narsee Monjee Institute of Management Studies (NMIMS)",
        "St. Xavier's College", "Sardar Patel Institute of Technology", "K. J. Somaiya College of Engineering",
        "Mithibai College"
    ],
    "Delhi": [
        "University of Delhi", "Jawaharlal Nehru University (JNU)", 
        "Delhi Technological University (DTU)", "Indian Institute of Technology Delhi (IIT-D)",
        "Jamia Millia Islamia", "Lady Shri Ram College for Women", 
        "Guru Gobind Singh Indraprastha University"
    ],
    "Bengaluru": [
        "Indian Institute of Science (IISc)", "Indian Institute of Management Bangalore (IIM-B)",
        "National Institute of Fashion Technology (NIFT)", "PES University",
        "RV College of Engineering", "Christ University", 
        "Bangalore Institute of Technology"
    ],
    "Chennai": [
        "Indian Institute of Technology Madras (IIT-M)", "Anna University",
        "Loyola College", "Madras Christian College",
        "SRM Institute of Science and Technology", 
        "Vellore Institute of Technology (VIT)"
    ],
    "Hyderabad": [
        "University of Hyderabad", "Indian School of Business (ISB)",
        "Osmania University", "International Institute of Information Technology (IIIT-H)",
        "Jawaharlal Nehru Technological University (JNTU)"
    ],
    "Pune": [
        "Symbiosis International University", 
        "University of Pune (Savitribai Phule Pune University)",
        "Bharati Vidyapeeth Deemed University", 
        "MIT World Peace University"
    ],
    "Kolkata": [
        "Jadavpur University", 
        "Presidency University", 
        "University of Calcutta", 
        "Indian Statistical Institute"
    ],
    "Ahmedabad": [
        "Indian Institute of Management Ahmedabad (IIM-A)", 
        "Gujarat University", 
        "Nirma University"
    ],
    "Jaipur": [
        "Malaviya National Institute of Technology (MNIT)", 
        "Rajasthan Technical University"
    ],
    "Indore": [
        "Indian Institute of Management Indore (IIM-I)", 
        "Devi Ahilya Vishwavidyalaya"
    ]
}

# Define program interests
program_interests = [
    'Data Science', 'Artificial Intelligence', 'Robotics', 
    'Electric Vehicles', 'Cybersecurity', 'Biotechnology', 
    'Business Administration', 'Environmental Science'
]

#Define lead Sources
lead_sources = [
    'LinkedIn', 'College Collaboration', 'Google Form',
    'Instagram', 'Mass-Mailing', 'Whatsapp'
]

# Define distribution percentages for each column
location_distribution = [0.14, 0.12, 0.11, 0.10, 0.09, 0.07, 0.06, 0.22, 0.04, 0.05]
year_distribution = [0.10, 0.40, 0.27, 0.23]  # Distribution for years 1st to 4th
program_distribution = [0.15, 0.12, 0.10, 0.08, 0.14, 0.09, 0.11, 0.21]  # Distribution for programs
leadsource_distribution = [0.30, 0.25, 0.15, 0.15, 0.10, 0.05] # Distribution for leadsource

# Generate dataset
data = []
num_rows = 15000

for i in range(num_rows):
    lead_id = f"LD{i+1}"
    
    # Randomly select location based on defined distribution
    location = np.random.choice(list(locations_colleges.keys()), p=location_distribution)
    
    # Randomly select college from the chosen location
    college = random.choice(locations_colleges[location])
    
    # Randomly select year of study based on defined distribution
    year_of_study = np.random.choice(['1st', '2nd', '3rd', '4th'], p=year_distribution)
    
    # Randomly select program interest based on defined distribution
    program_interest = np.random.choice(program_interests, p=program_distribution)
    
    # Randomly select lead source
    lead_source = np.random.choice(lead_sources, p=leadsource_distribution)
    
    data.append([lead_id, location, college, year_of_study, program_interest, lead_source])

# Create DataFrame
df = pd.DataFrame(data, columns=["Lead ID", "Location", 
                                  "College/University", 
                                  "Year of Study", 
                                  "Program Interest", 
                                  "Lead Source"])

# Save to CSV file
df.to_csv("leads_dataset.csv", index=False)

print("Dataset generated successfully with 15,000 rows.")

# Save to CSV file
output_file = r"D:\lead_dataset.csv"  # Provide full path
df.to_csv(output_file, index=False)
print(f"Tagging complete! Results saved to {output_file}")