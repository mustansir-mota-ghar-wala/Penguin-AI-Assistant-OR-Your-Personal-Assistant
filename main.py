import pyttsx3
import speech_recognition as sr
import webbrowser
import time
import datetime
import wikipedia

recognizer = sr.Recognizer()


# Stable speak function
def speak(text):
    try:
        print(f"Penguin: {text}")

        engine = pyttsx3.init()
        engine.setProperty('rate', 160)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

        time.sleep(0.3)

    except Exception as e:
        print("Speech Error:", e)


# Listen function
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text.lower()

        except:
            return ""

    except Exception as e:
        print("Mic Error:", e)
        return ""


# Main command processor
def process_command(command):

    try:
        # 🔹 OPEN ANY WEBSITE
        if command.startswith("open"):
            site = command.replace("open", "").strip()
            url = f"https://www.{site}.com"
            speak(f"Opening {site}")
            webbrowser.open(url)

        # 🔹 PLAY YOUTUBE SEARCH
        elif command.startswith("play"):
            song = command.replace("play", "").strip()
            speak(f"Playing {song}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

        # 🔹 TIME
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        # 🔹 DATE
        elif "date" in command or "today" in command:
            today = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {today}")

        # 🔹 WIKIPEDIA SEARCH
        elif command.startswith("who is") or command.startswith("what is"):
            query = command.replace("who is", "").replace("what is", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak(result)
            except:
                speak("Sorry, I couldn't find information.")

        # 🔹 BASIC CHAT
        elif "how are you" in command:
            speak("I am fine Mustansir, how can I help you?")

        elif "your name" in command:
            speak("I am Penguin, your personal assistant.")

        # 🔹 EXIT
        elif command in ["exit", "stop", "bye"]:
            speak("Goodbye Mustansir. Have a great day!")
            exit()

        else:
            speak("Sorry, I did not understand.")

    except Exception as e:
        print("Command Error:", e)
        speak("Something went wrong.")


# MAIN LOOP
if __name__ == "__main__":
    speak("Initializing Penguin AI Assistant")

    while True:
        word = listen()

        if "penguin" in word:
            speak("Yes Mustansir, how can I help you?")
            command = listen()

            if command:
                process_command(command)