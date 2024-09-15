import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # You can switch to voices[1] if you want a different voice


# Function to make the assistant speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to greet the user based on the time of the day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Suprahat")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hi, I am Jarvis. How can I help you today?")


# Function to take microphone input and recognize it as text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Could you please say that again?")
        return "None"
    return query


# Function to send an email
def sendEmail(to, content):
    try:
        # Ensure you generate an App Password for this if using Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-app-password')  # Use App Password instead of regular password
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        speak("Email has been sent successfully!")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't send the email.")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Wikipedia search
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Open YouTube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        # Open Google
        elif 'open google' in query:
            webbrowser.open("google.com")

        # Open StackOverflow
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        # Play music from the specified directory
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'  # Update to your music directory
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No songs found in the directory")
            else:
                speak("Music directory not found")

        # Tell the current time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        # Open Visual Studio Code
        elif 'open code' in query:
            codePath = "C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Update to your VS Code path
            os.startfile(codePath)

        # Send email
        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "recipientemail@gmail.com"  # Update the recipient email
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")

        # Default response for unrecognized commands
        else:
            speak("Sorry, I didn't understand that command.")
