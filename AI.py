import os
import speech_recognition as sp
import sounddevice
import datetime
import random

os.system("clear")

def speak(audio):
    print("AI : ",audio)
    os.system('''echo '%s' | festival --tts'''%(audio))
    

def r_voice():
    r=sp.Recognizer()
    with sp.Microphone() as mp:
        print("Recogning...")
        r.pause_threshold=1
        audio=r.listen(mp)
    
    try:
        print("wait...")
        query=r.recognize_google(audio,language="en-in")
        print("user side : ",query)

        return query
    except Exception as e:
        print(e)
        speak("Say agin place...")

def welcome():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if(hour >= 1 and hour < 12):
        speak("Good morning sir...")
    elif(hour >= 12 and hour < 4):
        speak("Good afternoon sir...")
    else:
        speak("Good evening sir...")
    speak("How can i help you sir...")

if __name__ == "__main__":
    welcome()
    #ans = r_voice()
    #speak(ans)
    # welcome = "hello how are you! what is your name?"
    # speak(welcome)
    # q = input("enter your name :")
    # name = "hi " + q +"how can i help you."
    # speak(name)
