import os
import speech_recognition as sp
import sounddevice
import datetime
import wikipedia


os.system("clear")


def file_read(audio):
    file = open('read.txt', 'w') 
    file.write(audio) 
    file.close()

def speak(audio):
    print("AI : ",audio)
    file_read(audio)
    os.system("cat read.txt | festival --tts")
    os.remove("read.txt")
    

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
        file_read(query)

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
    welcome()
    condition = True
    while condition:
        query=r_voice().lower()

        if "goodbye" in query:
            speak("Good bye sir...")
            condition = False

        if "wikipedia" in query:
            speak("searching in wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            speak(results)
            