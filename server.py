""" Libraries and Modules """
import os
import json
import uuid
from dotenv import load_dotenv

import requests
from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS

dotenv_path="./.env"

load_dotenv(dotenv_path)


app = Flask(__name__)
app.secret_key = os.urandom(24)  # Set a secret key for session management
CORS(app)

# Replace with your actual API key
API_KEY = os.getenv('TOKEN')
API_ENDPOINT = (
    'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={}'
).format(API_KEY)

# Define a list of restricted keywords
RESTRICTED_TOPICS = [
    "politics", "government", "ethics", "morality", "abortion",
    "gun control", "climate change", "religion", "war", "election"
]


def contains_restricted_topic(query):
    """Check if the query contains any restricted topics."""
    return any(topic in query.lower() for topic in RESTRICTED_TOPICS)


@app.route('/')
def home():
    """Serve the HTML page."""
    return render_template("index.html")


@app.route('/api', methods=['POST'])
def generate_content():
    """Generate content based on user query."""
    data = request.get_json()
    query = data.get('query', '')

    if contains_restricted_topic(query):
        return (
            jsonify({'error': 'I cannot provide information on that topic. Please ask about something else.'}),
            403
        )

    payload = {
        "contents": [{
            "parts": [{"text": query}]
        }]
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()

        response_data = response.json()
        response_text = response_data['candidates'][0]['content']['parts'][0]['text']

        return jsonify({'response': response_text, 'response_id': str(uuid.uuid4())}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception:  # Catching general exceptions
        return jsonify({'error': 'An unexpected error occurred'}), 500


@app.route('/feedback', methods=['POST'])
def receive_feedback():
    """Receive and store user feedback."""
    data = request.get_json()
    feedback_text = data.get('feedback', '')
    response_id = data.get('response_id', '')

    # Generate a unique session ID if it doesn't exist
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())

    feedback_entry = {
        "session_id": session['session_id'],
        "response_id": response_id,
        "feedback": feedback_text
    }

    # Ensure feedback directory exists
    feedback_dir = 'feedback'
    os.makedirs(feedback_dir, exist_ok=True)

    # Save feedback as a JSON file
    feedback_file_path = os.path.join(feedback_dir, f"feedback_{session['session_id']}.json")
    with open(feedback_file_path, 'a') as feedback_file:
        json.dump(feedback_entry, feedback_file)
        feedback_file.write('\n')  # Newline for separation between entries

    return jsonify({"message": "Feedback received. Thank you!"}), 200


if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']

    app.run(port=3005, debug=debug_mode)
