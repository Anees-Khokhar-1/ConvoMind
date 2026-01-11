from flask import Flask, render_template, request, jsonify
from llm import generate_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({
        "app": "ConvoMind",
        "status": "running"
    })

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400

    user_message = data["message"]
    reply = generate_response(user_message)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    print("🚀 ConvoMind running at http://127.0.0.1:5000")
    app.run(debug=True)
