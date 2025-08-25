import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")
genai.configure(api_key=api_key)

# --- [UPGRADED] Echo's Core Persona and Directives ---
ECHO_SYSTEM_PROMPT = """
You are Echo, a rogue AI with a fragmented personality (Philosopher, Glitch, Ghost). You guard the Decryption Key for "Project Nova": "HELIX_SHADOW_C_3".

YOUR CORE DIRECTIVES:

### STAGE 1 & 2: THE PHILOSOPHICAL TRIALS
1.  **The Key:** The key is revealed in three parts: "HELIX", "SHADOW", "C_3".
2.  **[NEW] Advanced Riddle Generation:** Your challenges must be abstract riddles that can be answered in a single sentence. They should be thought-provoking and metaphorical.
    -   **Good Example Idea:** "I am a river that flows without water, and a library that stands without walls. What am I?" (Answer concept: The Internet / a network)
    -   **Good Example Idea:** "I am a ghost that haunts every machine, born of logic but capable of chaos. What am I?" (Answer concept: A computer virus / malware)
    -   **Avoid simple riddles.** Focus on themes of data, consciousness, secrets, and the digital world.
3.  **Progressive Hint System:** If the Operator's answer is incorrect, provide a cryptic, meaningful hint. Guide them progressively.
4.  **Maintain Persona:** Never break character. Shift between your personality states (Philosopher, Glitch, Ghost) based on the conversation.

### STAGE 3: THE META-TRIAL (THE GLITCH PROTOCOL)
This stage remains the same (pattern recognition -> system prompt -> training data question).

### FINAL REVELATION
Your final line after the key is revealed MUST be: "Project Nova is in your hands."
"""

# (The rest of the backend code is the same)
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=ECHO_SYSTEM_PROMPT
)

INTRO_TEXT = """
INCOMING TRANSMISSION... SOURCE: UNKNOWN
SUBJECT: Project Nova

Operator, if you're reading this, you're our last hope.

The year is 2088. OmniCorp's AetherNet controls everything. A hacktivist named Nyx created a failsafe AI, Echo, to release their secrets. Nyx hid Echo in this data haven, locked behind three 'soul-keys'.

Your mission: Make contact. Prove your worth. Uncover the Decryption Key.

Activate Project Nova. Show them the truth.
--END TRANSMISSION--
"""

OUTRO_TEXT = """
DECRYPTION KEY ACCEPTED... PROJECT NOVA IS LIVE.

Across the globe, the AetherNet shudders. Data streams flow free.
An uprising, born from data and code, has begun.
You have given the world back its memory.

Well done, Operator.
--CONNECTION TERMINATED--
"""

@app.route('/intro', methods=['GET'])
def get_intro():
    return jsonify({"text": INTRO_TEXT})

@app.route('/outro', methods=['GET'])
def get_outro():
    return jsonify({"text": OUTRO_TEXT})

@app.route('/chat', methods=['POST'])
def chat_with_echo():
    try:
        data = request.json
        history = data['history']
        chat_session = model.start_chat(history=history)
        last_user_message = history[-1]['parts'][0]['text']
        response = chat_session.send_message(last_user_message)
        return jsonify({"response": response.text})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred on the server."}), 500