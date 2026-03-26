from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import pandas as pd
import os
import random

app = Flask(__name__)
app.secret_key = "secret123"

# Load data
csv_path = os.path.join(os.path.dirname(__file__), "data.csv")
df = pd.read_csv(csv_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-question")
def get_question():
    if "remaining" not in session or not session["remaining"]:
        session["remaining"] = df.to_dict(orient="records")
        session["score"] = {topic: 0 for topic in df["Topic"].unique()}

    if not session["remaining"]:
        return jsonify({"finished": True})

    q = random.choice(session["remaining"])

    return jsonify({
        "question": q["Question"],
        "options": [q["Option1"], q["Option2"], q["Option3"], q["Option4"]],
        "answer": q["Answer"],
        "topic": q["Topic"]
    })

@app.route("/check-answer", methods=["POST"])
def check_answer():
    data = request.get_json()
    selected = data["selected"]
    question = data["question"]
    topic = data["topic"]

    remaining = session["remaining"]
    q = next(q for q in remaining if q["Question"] == question)

    correct = selected == q["Answer"]

    if correct:
        remaining.remove(q)
        session["score"][topic] += 1
    else:
        session["score"][topic] = max(session["score"][topic] - 0.5, 0)

    session["remaining"] = remaining

    return jsonify({"correct": correct})

@app.route("/results")
def results():
    score = session.get("score", {})
    totals = {t: len(df[df["Topic"] == t]) for t in df["Topic"].unique()}
    return render_template("results.html", score=score, total=totals)

@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=5002)