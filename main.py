# main.py - Job description parser

import csv
import re
from pathlib import Path

# File to store parsed job info
csv_file = Path("job_info.csv")

# Predefined roles to look for (can expand later)
roles = ["Software Engineer", "Intern", "Developer", "Analyst", "Data Scientist", "Researcher"]

# Function to extract company name
def extract_company(text):
    match = re.search(r" at (.+?)(?:,|\n| for | with |$)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip().title()
    else:
        return "Unknown"

# Function to extract roles
def extract_roles(text):
    found_roles = [role for role in roles if role.lower() in text.lower()]
    if not found_roles:
        found_roles = ["Unknown"]
    return found_roles

# Main loop: keep asking for job descriptions until 'done'
while True:
    text = input("\nPaste a job description (or type 'done' to finish):\n")
    if text.lower() == "done":
        break

    company = extract_company(text)
    role_found = extract_roles(text)

    # Show results
    print("\n--- Extracted Job Info ---")
    print("Company:", company)
    print("Role(s):", ", ".join(role_found))

    # Save to CSV
    file_exists = csv_file.exists()
    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Company", "Role(s)", "Description"])
        writer.writerow([company, ", ".join(role_found), text])
    
    print("\nAll data saved to job_info.csv")