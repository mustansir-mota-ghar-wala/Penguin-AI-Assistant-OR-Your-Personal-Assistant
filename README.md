# 🐧 Penguin AI Assistant

A simple voice-controlled AI assistant built using Python.  
This assistant can listen to your voice, understand commands, and respond using speech.

## 🚀 Features
 🎤 Voice Recognition (Speech to Text),
 🔊 Text-to-Speech Response,
 🌐 Open Websites (e.g., Google, YouTube),
 🎵 Play YouTube Searches,
 ⏰ Tell Current Time,
 📅 Tell Current Date,
 📚 Fetch Information from Wikipedia,
 💬 Basic Conversation (e.g., "How are you?"),
 🛑 Exit Command

## 🛠️ Technologies Used
 Python 3.11.9 (Recommended for best compatibility),
 Virtual Environment (venv)

### Libraries Used:
 pyttsx3 (Text-to-Speech),
 SpeechRecognition (Voice Input),
 wikipedia (Information fetching),
 datetime (Time & Date),
 webbrowser (Open websites)
 
## 🧠 How It Works
The assistant listens for the wake word "Penguin".
After activation, it listens for user commands.
It processes commands and performs actions like: Opening websites, Playing videos, Providing information, Speaking responses

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
git clone https://github.com/your-username/Penguin-AI-Assistant.git
cd Penguin-AI-Assistant

### 2️⃣ Create Virtual Environment
python -m venv venv

### 3️⃣ Activate Virtual Environment
Windows:
venv\Scripts\activate,  
Mac/Linux:
source venv/bin/activate

### 4️⃣ Install Dependencies
pip install -r requirements.txt

### 5️⃣ Run the Project
python main.py

## ⚠️ Important Notes
Python 3.11.9 is recommended for stable performance.
Virtual environment is used to manage dependencies.
Internet connection is required for:
Speech recognition,
Wikipedia search
