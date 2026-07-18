import pdfplumber
import re


SKILLS = [
    "Python",
    "Java",
    "SQL",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Git",
    "GitHub",
    "Django",
    "REST API",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Node.js",
    "MongoDB",
    "MySQL",
    "Power BI",
    "Excel",
    "Machine Learning",
    "Deep Learning",
    "C",
    "C++",
    "OOP",
    "DBMS",
    "SDLC"
]


def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in SKILLS:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills
def read_job_description(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        skills = []

        for line in file:
            line = line.strip()

            if line:
                skills.append(line)

    return skills
def extract_text_from_pdf(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_email(text):
    email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

    if email:
        return email.group()

    return "Not Found"


def extract_phone(text):
    phone = re.search(r"(\+91[\s-]?)?[6-9]\d{9}", text)

    if phone:
        return phone.group()

    return "Not Found"


def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if len(line) > 2 and len(line.split()) <= 4:
            return line

    return "Not Found"