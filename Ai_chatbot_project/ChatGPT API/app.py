from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "sk-abcdef1234567890abcdef1234567890abcdef12"
CORS(app)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    try:
        # Get the message from the POST request
        message = request.json.get("message")
        if not message:
            return jsonify({"error": "Message is required"}), 400

        # Use the new OpenAI API call format
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            max_tokens=50
        )
        print("OpenAI Response:", response)

        # Extract the content from the response
        response_content = response['choices'][0]['message']['content']
        return jsonify({"response": response_content}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
  # Log the response


if __name__ == '__main__':
    app.run(debug=True)
