import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

# Initialize the voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Female voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning! I am Hexa.")
    elif 12 <= hour < 18:
        speak("Good Afternoon! I am Hexa.")
    else:
        speak("Good Evening! I am Hexa.")
    speak("How can I help you today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")
    except Exception as e:
        print("Sorry, could not understand. Please say that again.")
        return "None"
    return command

def main():
    wish_user()
    while True:
        command = take_command()

        if 'wikipedia' in command:
            speak("Searching Wikipedia...")
            query = command.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif 'time' in command:
            time_str = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time_str}")

        elif 'exit' in command or 'stop' in command:
            speak("Goodbye! Have a great day!")
            break

        else:
            speak("Sorry, I didn't get that. Please try again.")

if __name__ == "__main__":
    main()
