from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask')
def ask():
    question = request.args.get("q", "").lower()

    if "hello" in question:
        answer = "Hello! Welcome to NMIMS."

    elif "dean" in question:
        answer = "The dean office is on the second floor."

    elif "library" in question:
        answer = "The library is in Block B."

    elif "who are you" in question:
        answer = "I am the reception assistant of NMIMS."

    else:
        answer = "Sorry, I do not know the answer."

    return jsonify({
        "reply": answer
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)