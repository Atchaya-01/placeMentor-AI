from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Chatbot Route
@app.route("/chatbot", methods=["POST"])
def chatbot():

    data = request.get_json()

    user_message = data["message"].lower()

    # Chatbot Logic

    if "cgpa" in user_message:

        reply = (
        "To increase CGPA:\n"
        "- Revise daily\n"
        "- Practice previous papers\n"
        "- Focus on weak subjects"
        )

    elif "skills" in user_message:

        reply = (
        "Recommended Skills:\n"
        "- Python\n"
        "- SQL\n"
        "- Web Development\n"
        "- Data Structures"
        )

    elif "resume" in user_message:

        reply = (
        "Resume Tips:\n"
        "- Add projects\n"
        "- Include internships\n"
        "- Mention certifications"
        )

    elif "interview" in user_message:

        reply = (
        "Interview Preparation:\n"
        "- Practice coding\n"
        "- Solve aptitude problems\n"
        "- Attend mock interviews"
        )

    elif "placement" in user_message:

        reply = (
        "Placement Tips:\n"
        "- Maintain good CGPA\n"
        "- Build projects\n"
        "- Practice DSA daily"
        )

    else:

        reply = (
        "I can help with:\n"
        "- CGPA improvement\n"
        "- Skills\n"
        "- Resume\n"
        "- Interview preparation"
        )

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(debug=True)