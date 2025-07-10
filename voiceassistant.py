import speech_recognition as sr
import pyttsx3
import pyaudio
import webbrowser
import datetime
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    print("assistant",text)
    engine.say(text)
    engine.runAndWait()
def listen():
    with sr.Microphone as source:
        print("listening")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("you said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("sorry I didn't catch that")
        return ""
    except sr.RequestError:
        speak("network error")
        return ""
def process_command(command):
    if "hello" in command:
       speak("hello!,how can I help you?")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"current time is:{now}")

    elif "date" in command:
         today = datetime.date.today().strftime("%B %d,%Y")
         speak(f"today's date is:{today}")

    elif "search" in command:
        speak("what do you want to search?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"here are the results for {query}")

    elif "stop" in command or "exit" in command:
        speak("goodbye!")
        exit()

    else:
        speak("sorry, I couldn't understand the command")

def main():
    speak("voice assistant activated, say something")
    while true:
        command = listen()
        if command:
            process_command(command)
        
if __name__ == "__main__":
    main()
