

---

### 📄 Voice-Activated AI Chatbot

````
# Voice-Activated AI Chatbot

## 📌 Project Overview
This is a Python-based voice-activated chatbot that listens to your voice, understands commands, and responds with speech. It can search Wikipedia, open Google, tell the current time, take notes, and even execute system-level commands like shutdown or restart.

---

## ✅ Features

- Voice recognition using `SpeechRecognition`
- Speech output using `pyttsx3`
- Wikipedia search with `wikipedia-api`
- Opens web pages like Google
- Tells the current time
- Writes notes to a text file
- Shutdown and restart commands
- Greets user based on time of day
- Error handling for unrecognized commands

---

## 🧠 Technologies Used

- Python 3.8+
- speech_recognition
- pyttsx3
- wikipedia-api
- pyaudio
- Standard libraries: `datetime`, `os`, `webbrowser`, etc.

---

## 🔧 Setup Instructions

### 1. Create and activate a virtual environment (optional but recommended)
```bash
python3 -m venv voicebot-env
source voicebot-env/bin/activate  # Linux/macOS
````

### 2. Install required libraries

```bash
pip install -r requirements.txt
```

If you get an error with PyAudio, install PortAudio first:

```bash
sudo apt install portaudio19-dev python3-pyaudio
```

---

## ▶️ How to Run

Make sure your microphone is working and then run:

```bash
python voice_bot.py
```

You will be greeted with a voice and prompted to speak a command.

---

## 🎙️ Example Commands to Try

* "Wikipedia Albert Einstein"
* "Open Google"
* "What is the time"
* "Write a note"
* "Shutdown"
* "Restart"
* "Exit"

---

## 📁 File Structure

```
voice_chatbot_project/
├── voice_bot.py         # Main Python script
├── requirements.txt     # List of dependencies
└── README.txt           # This file
```


