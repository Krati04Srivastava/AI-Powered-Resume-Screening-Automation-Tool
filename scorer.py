def calculate_score(candidate_skills, job_skills):

    candidate = set(skill.lower() for skill in candidate_skills)
    job = set(skill.lower() for skill in job_skills)

    matched = candidate.intersection(job)
    missing = job - candidate

    score = (len(matched) / len(job)) * 100 if len(job) > 0 else 0

    return score, matched, missing