from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from utils.gemini_skill_generator import generate_skills_from_role

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(resume_text, role):
    # 1️⃣ Generate AI skills using Gemini
    skills = generate_skills_from_role(role)

    # 2️⃣ Convert skills list → text
    skills_text = " ".join(skills)

    # 3️⃣ Create embeddings
    resume_embedding = model.encode(resume_text)
    skills_embedding = model.encode(skills_text)

    # 4️⃣ Cosine similarity
    score = cosine_similarity(
        [resume_embedding],
        [skills_embedding]
    )[0][0]

    return round(score * 100, 2)
def skill_gap_analysis(resume_text, role):
    role_skills = generate_skills_from_role(role)
    resume_text = resume_text.lower()

    matched = [s for s in role_skills if s in resume_text]
    missing = [s for s in role_skills if s not in resume_text]

    return matched, missing
