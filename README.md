# Voice-Activated Chatbot

A Python voice assistant. Listens for a spoken command, transcribes it with Google's speech recognition API, and responds with synthesized speech.

## Features

- Voice input via microphone (`speech_recognition`) and voice output (`pyttsx3`)
- Wikipedia lookups
- Opens web pages (e.g. "open Google")
- Tells the current time
- Saves spoken notes to a text file
- Shutdown/restart commands
- Time-of-day greeting on startup

## Tech Stack

Python, `speech_recognition` (Google Speech API backend), `pyttsx3` (offline TTS), `wikipedia-api`, `pyaudio`.

## Setup

```bash
python3 -m venv voicebot-env
source voicebot-env/bin/activate
pip install -r requirements.txt
```

PyAudio needs PortAudio installed first on Linux:

```bash
sudo apt install portaudio19-dev python3-pyaudio
```

## Usage

```bash
python main.py
```

Speak a command after the greeting — e.g. "what's the time", "open Google", "search Wikipedia for photosynthesis", "take a note".

## Limitations

Speech recognition depends on Google's API (requires an internet connection) and works best with clear English input. There's no wake-word detection — it listens for a single command per run rather than continuously.
