# 🎙️ Hexa - Your Voice Assistant in Python

Hexa is a basic voice assistant built using Python. It listens to your voice commands and performs actions like searching Wikipedia, telling the time, and opening popular websites like Google and YouTube.

## 🚀 Features

- ✅ Greets the user based on the time of day
- ✅ Listens to your voice using the microphone
- ✅ Converts speech to text and responds using voice
- ✅ Tells the current time
- ✅ Searches on Wikipedia and reads summaries aloud
- ✅ Opens websites like Google and YouTube

## 🛠️ Technologies Used

- Python 3
- `speech_recognition` – for voice input
- `pyttsx3` – for text-to-speech
- `wikipedia` – to fetch summaries
- `webbrowser` – to open websites
- `datetime` – for time-based features

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/hexa-voice-assistant.git
   cd hexa-voice-assistant
Install the required libraries:

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not available, install manually:

bash
Copy
Edit
pip install SpeechRecognition pyttsx3 wikipedia
pip install pipwin
pipwin install pyaudio
💡 For Mac/Linux users: use brew install portaudio before installing pyaudio.

▶️ Usage
Run the script using:

bash
Copy
Edit
python hexa.py
Hexa will greet you and start listening. Try commands like:

"What time is it?"

"Search Elon Musk on Wikipedia"

"Open YouTube"

"Stop" or "Exit" to quit

📁 File Structure
bash
Copy
Edit
hexa-voice-assistant/
│
├── hexa.py           # Main voice assistant code
├── README.md         # Project documentation
└── requirements.txt  # Python libraries list (optional)
💡 Future Enhancements (Optional Ideas)
Add weather updates

Send emails using voice

Play local music

Perform Google searches directly

Add jokes and fun responses

📜 License
This project is for educational purposes. Feel free to modify and enhance it!

Made with 💻 and 🎤 by Isha
