import pyttsx3  # Text-to-speech conversion library
import speech_recognition as sr  # Speech recognition (voice to text)
import webbrowser  # To open websites in browser
import time  # For delays
import datetime  # To fetch current time and date
import wikipedia  # To get information from Wikipedia

# Initialize recognizer object (used for voice input)
recognizer = sr.Recognizer()


# Stable speak function (converts text to speech)
def speak(text):
    try:
        print(f"Penguin: {text}")  # Print output in console for reference

        # Initialize TTS engine every time (prevents freezing issue)
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)  # Set speaking speed

        engine.say(text)  # Convert text to speech
        engine.runAndWait()  # Wait until speaking is finished
        engine.stop()  # Stop engine to clear queue

        time.sleep(0.3)  # Small delay to avoid mic & speaker conflict

    except Exception as e:
        print("Speech Error:", e)


# Listen function (captures voice input and converts to text)
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            
            # Adjust for background noise for better accuracy
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            # Listen for audio input with timeout limits
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

        try:
            # Convert speech to text using Google API
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text.lower()  # Return in lowercase for easy processing

        except:
            # If speech is not understood
            return ""

    except Exception as e:
        print("Mic Error:", e)
        return ""


# Main command processor (handles user commands)
def process_command(command):

    try:
        # 🔹 OPEN ANY WEBSITE (e.g., "open google")
        if command.startswith("open"):
            site = command.replace("open", "").strip()
            url = f"https://www.{site}.com"
            speak(f"Opening {site}")
            webbrowser.open(url)

        # 🔹 PLAY YOUTUBE SEARCH (e.g., "play song name")
        elif command.startswith("play"):
            song = command.replace("play", "").strip()
            speak(f"Playing {song}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

        # 🔹 TIME (tells current time)
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        # 🔹 DATE (tells today's date)
        elif "date" in command or "today" in command:
            today = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {today}")

        # 🔹 WIKIPEDIA SEARCH (basic information lookup)
        elif command.startswith("who is") or command.startswith("what is"):
            query = command.replace("who is", "").replace("what is", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak(result)
            except:
                speak("Sorry, I couldn't find information.")

        # 🔹 BASIC CHAT RESPONSES
        elif "how are you" in command:
            speak("I am fine Mustansir, how can I help you?")

        elif "your name" in command:
            speak("I am Penguin, your personal assistant.")

        # 🔹 EXIT COMMAND (terminate program)
        elif command in ["exit", "stop", "bye"]:
            speak("Goodbye Mustansir. Have a great day!")
            exit()

        # 🔹 UNKNOWN COMMAND
        else:
            speak("Sorry, I did not understand.")

    except Exception as e:
        print("Command Error:", e)
        speak("Something went wrong.")


# MAIN LOOP (continuous listening system)
if __name__ == "__main__":
    speak("Initializing Penguin AI Assistant")  # Startup message

    while True:
        word = listen()  # Listen for wake word

        # Activate assistant when "penguin" is spoken
        if "penguin" in word:
            speak("Yes Mustansir, how can I help you?")
            command = listen()  # Listen for actual command

            if command:
                process_command(command)  # Process user command