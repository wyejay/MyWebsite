from flask import Flask, request, jsonify, send_from_directory
import difflib

app = Flask(__name__)

medical_terms = {
    "hypertension": "A condition in which the force of the blood against the artery walls is too high.",
    "diabetes": "A chronic disease that affects how your body turns food into energy.",
    "asthma": "A condition in which your airways narrow and swell, producing extra mucus.",
    "anemia": "A condition where you lack enough healthy red blood cells to carry oxygen to your body’s tissues.",
    "arthritis": "Inflammation of one or more joints, causing pain and stiffness."
}

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

@app.route("/define")
def define():
    term = request.args.get("term", "").strip().lower()
    if not term:
        return jsonify({"definition": "No term provided."})
    if term in medical_terms:
        return jsonify({"definition": medical_terms[term]})
    close = difflib.get_close_matches(term, medical_terms.keys(), n=1)
    if close:
        return jsonify({"definition": f"Did you mean '{close[0]}'? {medical_terms[close[0]]}"})
    return jsonify({"definition": "Term not found in dictionary."})

if __name__ == "_main_":
    app.run(debug=True)
