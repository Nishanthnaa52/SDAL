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
from tkinter import *
import customtkinter as ctk 
from PIL import Image, ImageTk

#Every time clear the screen.
os.system("clear")


#GUI application function.

#Voice recognise function.
def r_voice():
    r=sp.Recognizer()
    with sp.Microphone() as mp:
        print("Hearing...")
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

    
    ctk.set_default_color_theme('./themes/dark-blue.json')

    root = ctk.CTk()

    #set a screen width, height.
    screen_width = 500
    screen_heigth = 500

    #set some window element.
    root.geometry(f"{screen_width}x{screen_heigth}")
    root.title("SDAL")

    #function seting section.
    def callback(event):
        webbrowser.open_new(event.widget.cget("text"))

    def GUI_text(query):
        info_label.configure(text=query)       

    voice_icon = ctk.CTkImage(
                            light_image=Image.open('./image/voice_icon.png'), 
                            dark_image=Image.open('./image/voice_icon.png'), 
                            size=(80, 100 )
                        )

    main_table = ctk.CTkTabview(
                            master=root,
                            width=400, 
                            height=400, 
                            corner_radius=10
                        )
    main_table.pack()
    main_table.add("Home")
    main_table.add("About")
    main_table.set('Home')

    button = ctk.CTkButton(
                            master=main_table.tab('Home'), 
                            text='', 
                            image=voice_icon, 
                            anchor='center', 
                            width=150,
                            height=150,
                            command=r_voice
                            ) 
    button.pack(pady=10)
    query=button

    About_label = ctk.CTkLabel(
                            master=main_table.tab('About'),
                            text='''
    This is my Basics desktop assistant Project.

    I used many modules in this project. 
    it's full python based basics disktop assistant Projesct.

    list of modules:
    1.os
    2.datetime
    3.sounddevice
    4.speech_recognition
    5.wikipedia
    6.webbrowser
    7.pywhatkit
    8.pyautogui
    9.time

    More check below and get source code

    '''
                            ,).pack()

    link_label = ctk.CTkLabel(master=main_table.tab("About"), text=r"https://github.com/Nishanthnaa52/SDAL", text_color="blue", cursor="hand2")
    link_label.pack()
    link_label.bind("<Button-1>", callback)


    exit_button = ctk.CTkButton(master=root, text='EXIT', command=root.destroy)
    exit_button.pack(pady=20)

    text = open('./read.txt', 'r')
    info_label = ctk.CTkLabel(master=main_table.tab("Home"), text=f'''{text}''', font=("Arial", 20))
    info_label.pack(pady=20)
    root.mainloop()






    while False:

        welcome()
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

#kill_terminal()