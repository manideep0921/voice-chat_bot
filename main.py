import speech_recognition as sr
import pyttsx3
import datetime
import wikipediaapi
import webbrowser
import os
import subprocess

# Initialize engine
engine = pyttsx3.init()
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='VoiceBot/1.0 (manideep@example.com)'
)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        print("Could not understand. Please say again...")
        return "None"
    return query.lower()


def handleCommand(command):
    if 'wikipedia' in command:
        topic = command.replace("wikipedia", "").strip()
        page = wiki_wiki.page(topic)
        if page.exists():
            summary = page.summary[:200]
            speak(f"According to Wikipedia, {summary}")
        else:
            speak("Sorry, I couldn't find that on Wikipedia.")
    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'what is the time' in command:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
    elif 'shutdown' in command:
        speak("Shutting down the system")
        os.system("shutdown /s /t 1")
    elif 'restart' in command:
        speak("Restarting the system")
        os.system("shutdown /r /t 1")
    elif 'note' in command:
        speak("What should I write in the note?")
        content = takeCommand()
        with open("note.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {content}\n")
        speak("Note saved.")
    else:
        speak("I didn't understand that. Please try again.")


if __name__ == "__main__":
    wishMe()
    while True:
        command = takeCommand()
        if command == "none":
            continue
        if 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            break
        handleCommand(command)

