import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import json
import requests
import pywhatkit


print('Your Personal Assistant Jarvis,Sir ')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak(" Your personal Assistant Jarvis,Sir ")
wishMe()

if __name__=='__main__':


    while True:
        speak("What i can help you,sir ")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if 'wikipedia' in statement:
            speak('Opening Wikipedia sir')
            webbrowser.open_new_tab("https://www.wikipedia.org")
            time.sleep(1)
           

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now,sir")
            time.sleep(1)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Now ,Google chrome open sir")
            time.sleep(1)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(1)


        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am your AI personal assistant jarvis  ')
            print('I am your AI personal assistant jarvis  ')

        elif "who made you" in statement or "who created you" in statement:
            speak("I was made by Adarsh sir")
            print("I was made by Adarsh sir")
        
        elif "play song" in statement:
            webbrowser.open_new_tab("https://open.spotify.com/playlist/3Kb1tdLeM8DxXnVp6ipBJd")
            speak('playing sir')
            time.sleep(1)


    

