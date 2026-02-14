# main.py - simplest automation example

# Ask for the job description
text = input("Paste a job description here:\n")

# Try to extract the company name
if " at " in text:
    company = text.split(" at ")[1].split()[0]
else:
    company = "Unknown"

# Try to detect the role from common keywords
roles = ["Intern", "Engineer", "Developer", "Analyst"]
role_found = "Unknown"
for role in roles:
    if role in text:
        role_found = role
        break

# Show the results
print("\nExtracted Info:")
print("Company:", company)
print("Role:", role_found)