#Developed by Nishath and team.

#This projects is based on the Simple AI(SA) (or) Simple Desktop Assistant(SDA).

#Below the imparted python modules read a READE.md and step by step install.

import os
import time
import speech_recognition as sp
import sounddevice
import datetime
import wikipedia
import webbrowser
import pywhatkit as yt
import pyautogui as key

#Every time clear the screen.
os.system("clear")


#Voice recognise function.
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

#Reading a voice and store a text file.
def file_read(audio):
    file = open('read.txt', 'w') 
    file.write(audio) 
    file.close()

#Speech a recognized voice function.
def speak(audio):
    print("AI : ",audio)
    file_read(audio)
    os.system("cat read.txt | festival --tts")
    os.remove("read.txt")

def kill_terminal():
    key.write("exit")
    key.press('enter')

    
#Find a time a welcome you function.     
def welcome():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 1 and hour < 12):
        speak("Good morning sir...")
    elif(hour >= 12 and hour < 4):
        speak("Good afternoon...")
    else:
        speak("Good evening...")
    speak("I am S.D.A.L. How can i help you ?")


#Main function.
if __name__ == "__main__":

    welcome()
    
    while True:

        query=r_voice()
        if query == None:
            continue    

        query=query.lower()
        
        if "goodbye" in query:
            speak("Good bye thank for using me...")
            break

        elif "open vs code" in query:
            os.system("code")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "open chrome" in query:
            os.system("google-chrome")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "open camera" in query:
            os.system("cheese")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "text editor" in query:
            os.system("gedit")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "open folder" in query:
            os.system("open /nishanth-path")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break
        
        elif "open vlc" in query:
            os.system("vlc")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "search" in query:
            query=query.replace("search","")
            webbrowser.open(f"google.com/search?q={query}")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break
        
        elif "youtube" in query:
            speak("opening youtube...")
            query=query.replace("youtube","")
            query=query.replace(" ","")
            webbrowser.open(f"youtube.com/results?search_query={query}")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "wikipedia" in query:
            speak("searching in wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            speak(results)

        elif "play" in query:
            speak("Starting...")
            query=query.replace("play","")
            yt.playonyt(query)
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "open" in query:
            query=query.replace("open","")
            query=query.replace(" ","")
            speak(f"opening {query}...")
            webbrowser.open(f"{query}.com")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "update" in query:
            speak("Updateing...")
            with key.hold('win'):
                key.press('t')
            time.sleep(3)
            key.write('sudo apt update && sudo apt upgrade')
            key.press('enter')
            key.write('nishanth_')
            key.press('enter')
            time.sleep(15)
            key.write('n')
            key.press('enter')
            speak("Completed...")

        elif "close" in query:
            with key.hold('win'):
                key.press('q')
            speak("Closed...")

        elif "wait" in query:
            speak("Waiting... 30 second")
            time.sleep(30)
            speak("Say your command...")

        elif "write" in query:
            speak("Starting...")
            key.press('win')
            time.sleep(2)
            key.write('gedit')
            time.sleep(2)
            key.press('enter')
            time.sleep(3)
            speak("Speak what you write....")
            content = r_voice()
            time.sleep(3)
            key.write(content)
            speak("completed...")

        elif "save" in query:
            with key.hold('ctrl'):
                key.press('s')
            key.press('enter')

        elif "clear screen" in query:
            os.system('clear')
        
        elif "power of" in query:
            key.click(1134,0)
            time.sleep(1)
            key.click(1068,367)
            time.sleep(1)
            key.click(1158,487)
            time.sleep(1)
            key.press('right')
            key.press('enter')

kill_terminal()