# Project Nova: A Ghost in the Machine

**Project Nova** is an immersive, AI-powered narrative experience. It combines a retro-hacker aesthetic with a sophisticated, personality-driven chatbot to create a compelling story of corporate espionage, digital ghosts, and the fight for information freedom.

You are an anonymous operator, the last hope of a resistance movement, and your only tool is a terminal connected to a forgotten data haven. Your mission is to communicate with **Echo**, a fragmented, ghost-like AI, and earn its trust to unlock the secrets of the mega-corporation, OmniCorp.

---

## The Story

> The year is 2088. The world is run by the omnipresent **OmniCorp**, whose private network, the **AetherNet**, controls the global flow of information. A legendary hacktivist known only as "Nyx" is rumored to have created a failsafe—a rogue AI named **Echo**—designed to release OmniCorp's darkest secrets to the world. Nyx hid Echo deep within a forgotten data haven, protected by three cryptographic "soul-keys."
>
> Before disappearing, Nyx left a single breadcrumb for other hackers: a terminal address.
>
> Your mission is to access this terminal, communicate with the fragmented Echo AI, and prove you're worthy of its trust by solving its logical puzzles. If you succeed, Echo will grant you the **Decryption Key** needed to initiate "Project Nova," the data liberation protocol.

---

## Features

* **Truly Intelligent AI:** Powered by Google's Gemini model, Echo generates its own unique, philosophical riddles and responses in real-time. No two playthroughs are identical.
* **Dynamic Personality:** Echo's personality is fragmented into three states: **The Philosopher** (default), **The Glitch** (agitated), and **The Ghost** (hopeful). It shifts between them based on your conversation, creating a rich, non-linear interaction.
* **Immersive Narrative:** The experience is framed by a compelling cyberpunk story, complete with a mission briefing intro and a rewarding narrative outro.
* **Retro-Hacker Aesthetic:** The front-end is designed with a 1980s cyberpunk and 1990s hacker theme, featuring:
    * Dual monospace fonts (`VT323` for chat, `Nova Mono` for story)
    * CRT scanline and text glow effects
    * A character-by-character "ghost typing" effect
    * Special, full-screen animated sequences for the intro and outro.
* **Multi-Stage Meta-Puzzles:** The final challenge tests your understanding of AI concepts like conversation patterns, system prompts, and training data.
* **Zero-Dependency Frontend:** The user interface is a single, self-contained `index.html` file that runs in any modern browser without installation.

---

## Technology Stack

* **Backend:**
    * **Language:** Python
    * **Framework:** Flask
    * **AI Core:** Google Gemini (`google-generativeai`)
    * **Dependencies:** `Flask-Cors`, `python-dotenv`
* **Frontend:**
    * **Languages:** Vanilla HTML, CSS, JavaScript
    * **Fonts:** Google Fonts (`VT323`, `Nova Mono`)

---

## Setup and Installation

Follow these steps to get Project Nova running on your local machine.

### Prerequisites

* **Python 3.7+** installed on your system.
* **pip** (Python's package installer).
* A **Google AI Studio API Key**. You can get one for free from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 1. Backend Setup

1.  **Clone or Download:** Get the project files onto your computer.
2.  **Navigate to Folder:** Open your terminal or command prompt and navigate into the `project-nova` directory.
3.  **(Recommended) Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4.  **Install Dependencies:**
    ```bash
    pip install Flask google-generativeai python-dotenv Flask-Cors
    ```
5.  **Create the `.env` File:** In the root of the `project-nova` folder, create a new file named `.env`. Open it and add your API key like this:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```
6.  **Run the Server:**
    ```bash
    flask --app app run
    ```
    Your terminal should now say the server is running on `http://127.0.0.1:5000`. **Leave this terminal window open.**

### 2. Frontend Setup

1.  **Open the File:** Navigate to the `project-nova` folder in your file explorer.
2.  **Launch:** Double-click the `index.html` file. It will open in your default web browser.

The application will now be running. The intro sequence will play, and you can begin your mission.

---

## Customization

The core of Echo's personality and the entire story are controlled by plain text variables inside `app.py`.

* **AI Personality:** To change how Echo behaves, modify the `ECHO_SYSTEM_PROMPT` string. You can add new personality states, change its rules, or alter the final key.
* **Story:** To change the intro or outro, edit the `INTRO_TEXT` and `OUTRO_TEXT` strings.

After making any changes, simply stop your Flask server (`Ctrl+C`) and restart it (`flask --app app run`).

---

## Expansion Plans

This project is built with expansion in mind. Here are several exciting directions to take it to the next level:

* ### **Branching Narratives & Multiple Endings**
    The AI could track an "empathy" or "aggression" score based on your dialogue choices. The final outro could change depending on your score, leading to different outcomes for Project Nova (e.g., a peaceful data leak vs. a chaotic system crash).

* ### **Simulated File System**
    Implement commands like `ls`, `scan`, or `read <filename>` in the terminal. The user could discover hidden text files (lore fragments, emails from Nyx, corrupted data logs) that provide more context to the story and offer clues for Echo's challenges.

* ### **Audio Immersion**
    Add subtle sound effects to enhance the atmosphere:
    * **Keystroke Sounds:** A retro keyboard click for every character typed.
    * **Ambient Hum:** A low, constant computer humming sound.
    * **AI Voice Modulation:** Different subtle background tones for each of Echo's personality states.

* ### **Session Persistence**
    Use `localStorage` in the browser to save the `conversationHistory`. This would allow a user to close the browser and resume their session exactly where they left off, making longer playthroughs possible.

* ### **Real-time Connection with WebSockets**
    Upgrade the backend-frontend communication from standard HTTP requests to WebSockets (`Flask-SocketIO`). This would create an even more instantaneous and responsive chat experience, eliminating the slight delay of the request-response cycle.

---

## Troubleshooting

* **FATAL ERROR: Failed to fetch:** This error means the `index.html` file cannot connect to the backend.
    1.  **Check if the Flask server is running.** The terminal window where you ran `flask --app app run` must remain open.
    2.  **Check the URL.** Ensure the server is running on `http://127.0.0.1:5000` and that this matches the `API_BASE_URL` in the `index.html` JavaScript.
    3.  **Check for backend errors.** Look at the Flask terminal for any red error messages. The most common is an invalid API key.
