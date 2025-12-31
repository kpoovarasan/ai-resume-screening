from flask import Flask, render_template, request
from utils.text_extractor import extract_text
from utils.preprocess import clean_text
from utils.similarity import calculate_similarity, skill_gap_analysis

app = Flask(__name__)

# HOME PAGE (INPUT FORM)
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


# RESULT PAGE (PROCESS & SHOW OUTPUT)
@app.route("/analyze", methods=["POST"])
def analyze():
    resume_file = request.files.get("resume")
    jd_text = request.form.get("jd")

    if not resume_file or not jd_text:
        return render_template("home.html", error="Please upload resume and job description")

    # Extract & clean text
    resume_text = extract_text(resume_file)
    resume_text = clean_text(resume_text)
    jd_text = clean_text(jd_text)

    # AI processing
    score = calculate_similarity(resume_text, jd_text)
    matched, missing = skill_gap_analysis(resume_text, jd_text)

    result = {
        "score": score,
        "matched": matched,
        "missing": missing
    }
    print(result)
    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
