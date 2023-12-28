from flask import Flask, request, jsonify
import google.generativeai as genai
from apiKey import key
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Configure the generative AI model
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        # Extract the message from request
        message = request.json['message']

        # Send message to the chat model and get response
        response = chat.send_message(message)

        # Return the chatbot's response
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in a production environment
