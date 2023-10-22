import os
import speech_recognition as sp
import sounddevice
import datetime
import wikipedia


os.system("clear")

def speak(audio):
    print("AI : ",audio)
    os.system("echo '''%s''' | festival --tts"%(audio))
    

def r_voice():
    r=sp.Recognizer()
    with sp.Microphone() as mp:
        print("Recogning...")
        r.pause_threshold=0.8
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
    if(hour >= 1 and hour < 12):
        speak("Good morning sir...")
    elif(hour >= 12 and hour < 4):
        speak("Good afternoon sir...")
    else:
        speak("Good evening sir...")
    speak("How can i help you sir...")

if __name__ == "__main__":
    #welcome()
    while True:
        query=r_voice().lower()

        if "goodbye" in query:
            os.system("exit")

        if "wikipedia" in query:
            speak("searching in wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            