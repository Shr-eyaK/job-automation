# main.py - Job Description Parser
# Student project: Extracts company, role, and skills from job descriptions into CSV for analysis

import csv
import re
from pathlib import Path

# CSV file to store parsed job info
csv_file = Path("job_info.csv")

# Predefined roles to look for (expandable)
roles = ["Software Engineer", "Intern", "Developer", "Analyst", "Data Scientist", "Researcher"]

# Predefined skills to extract (expandable)
skills_list = ["Python", "SQL", "Java", "C++", "Excel", "Data Analysis"]

# -------------------------
# Functions
# -------------------------

def extract_company(text):
    """Extracts company name from job description."""
    match = re.search(r" at (.+?)(?:,|\n| for | with |$)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip().title()
    return "Unknown"

def extract_roles(text):
    """Finds roles mentioned in the job description."""
    found_roles = [role for role in roles if role.lower() in text.lower()]
    return found_roles if found_roles else ["Unknown"]

def extract_skills(text):
    """Finds skills mentioned in the job description."""
    found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]
    return found_skills if found_skills else ["Unknown"]

def save_to_csv(company, roles_found, skills_found, description):
    """Saves extracted info to CSV."""
    file_exists = csv_file.exists()
    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Company", "Role(s)", "Skills", "Description"])
        writer.writerow([company, ", ".join(roles_found), ", ".join(skills_found), description])

# -------------------------
# Main loop
# -------------------------
print("Job Description Parser - Student Project")
print("Enter job descriptions one by one. Type 'done' to finish.\n")

while True:
    text = input("Paste a job description (or 'done' to finish):\n")
    if text.lower() == "done":
        break

    company = extract_company(text)
    roles_found = extract_roles(text)
    skills_found = extract_skills(text)

    # Show extracted info
    print("\n--- Extracted Job Info ---")
    print("Company:", company)
    print("Role(s):", ", ".join(roles_found))
    print("Skills:", ", ".join(skills_found))

    # Save to CSV
    save_to_csv(company, roles_found, skills_found, text)
    print("Data saved to job_info.csv\n")