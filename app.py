from flask import Flask, request, jsonify
import os
from groq import Groq

app = Flask(__name__)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Stores conversation history for each session
sessions = {}

@app.route("/")
def home():
    return "NMIMS Reception Robot Backend Running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_message = data.get("message", "")
    session_id = data.get("session_id", "default")

    if not user_message:
        return jsonify({"reply": "Please ask something."})

    # Create memory for new session
    if session_id not in sessions:
        sessions[session_id] = []

    # Add user's message
    sessions[session_id].append({
        "role": "user",
        "content": user_message
    })

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=sessions[session_id]
        )

        reply = response.choices[0].message.content

        # Save AI response
        sessions[session_id].append({
            "role": "assistant",
            "content": reply
        })

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run()