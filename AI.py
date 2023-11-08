#developed by Nishath and team.

#This projects is based on the Simple AI(SA) (or) Simple Desktop Assistant(SDA).

#below the imparted python modules read a READE.md and step by step install.
import os
import speech_recognition as sp
import sounddevice
import datetime
import wikipedia

#Every time clear the screen.
os.system("clear")


#voice recognise function.
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
        
    
#Find a time a welcome you function.     
def welcome():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 1 and hour < 12):
        speak("Good morning  ")
    elif(hour >= 12 and hour < 4):
        speak("Good afternoon  ")
    else:
        speak("Good evening  ")
    speak("How can i help you  ")


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

        elif "search" in query:
            query=query.replace("search","")
            query=query.replace(" ","")
            os.system("google-chrome google.com/search?q=%s"%(query))
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break

        elif "nishanth" in query:
            speak("Nishanth is on")
            os.system("google-chrome github.com/nishanthnaa52")
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break


        elif "wikipedia" in query:
            speak("searching in wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            speak(results)
            
        elif "youtube" in query:
            speak("opening youtube...")
            query=query.replace("youtube","")
            query=query.replace(" ","")
            os.system("google-chrome youtube.com/results?search_query=%s"%(query))
            condition = input("Are you continue (Y/N):").lower()
            if(condition == 'n'):
                break