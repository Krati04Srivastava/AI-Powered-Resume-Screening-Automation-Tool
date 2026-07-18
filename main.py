import os

from parser import (
    extract_text_from_pdf,
    extract_email,
    extract_phone,
    extract_name,
    extract_skills
)
from parser import read_job_description
from scorer import calculate_score
from report import generate
resume_folder = "resumes"
job_skills=read_job_description("job_description/jd.txt")
all_candidates = []
for file in os.listdir(resume_folder):



    if file.endswith(".pdf"):
        path = os.path.join(resume_folder, file)

        text = extract_text_from_pdf(path)

        print("=" * 10)
        print(file)

        print("Name :", extract_name(text))
        print("Email:", extract_email(text))
        print("Phone:", extract_phone(text))
        skills = extract_skills(text)
        print("Skills Found:", skills)
        score,matched,missing=calculate_score(skills,job_skills)
        print("Skills :", skills)

        print("Matched Skills :", matched)

        print("Missing Skills :", missing)

        print(f"ATS Score : {score:.2f}%")
        all_candidates.append({
            "Candidate": extract_name(text),
            "Email": extract_email(text),
            "Phone": extract_phone(text),
            "ATS Score": round(score, 2),
            "Matched Skills": ", ".join(matched),
            "Missing Skills": ", ".join(missing)
        })
print(f"Total Candidates: {len(all_candidates)}") #1
generate(all_candidates)
