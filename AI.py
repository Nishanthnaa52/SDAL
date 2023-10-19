import pyttsx3

engine = pyttsx3.init("espeak")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[17].id)
print(voices[17].id)

def speak(audio): 
    engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello nishanth, how are you!")