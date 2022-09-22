import pyttsx3
import speech_recognition as sr
import datetime
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import speedtest
import wikipedia
import webbrowser
 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",150)
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

'''def Pass(pass_inp):

    password = "Akshar"
    passss = str(password)

    if passss==str(pass_inp):
        speak("Access Granted.")
    else:
        speak("Access is not Granted.")
        exit()

if  __name__  == "__main__":
    speak("This Paticular File IS Password Protected.")
    speak("Kindly Provide The Password To Access.")
    passss=input("Enter The Password : ")
    Pass(passss)''' 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=8 and hour<12:
        speak("Good Morning!") 
    
    elif hour>=12 and hour<16:
        speak("Good Afternoon!") 

    elif hour>=16 and hour<20:
        speak("Good Evening!")   

    else:
        speak("Good Night!")   

    speak("I am Jarvis Sir, Please tell me how may I help you!") 

def takeCommand():

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        r.energy_threshold = 300
        audio= r.listen(source,0,3)

    try:
        print("Reconizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please...")
        return"None"   
    return query


if  __name__  == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        if "go to sleep" in query:
            speak("Ok sir,you can call any time.")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open map' in query:
            webbrowser.open("https://maps.google.com")
            
        elif "open" in query:   
            query = query.replace("open","")
            query = query.replace("jarvis","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(1)
            pyautogui.press("enter")

        elif "internet speed" in query:
            wifi  = speedtest.Speedtest()
            upload_net = wifi.upload()/1048576          #Megabyte = 1024*1024 Bytes
            download_net = wifi.download()/1048576
            print("Wifi Upload Speed is", upload_net)
            print("Wifi download speed is ",download_net)
            speak(f"Wifi Upload speed is {upload_net}")
            speak(f"Wifi download speed is {download_net}")

        elif "play a game" in query:
            from game import game_play
            game_play()

        elif "screenshot" in query:
            import pyautogui 
            im = pyautogui.screenshot()
            im.save("ss.jpg")

        elif "click my photo" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("SMILE")
            pyautogui.press("enter")

        elif "open" in query:
            from dictapp import openappweb
            openappweb(query)

        elif "close" in query:
            from dictapp import closeappweb
            closeappweb(query)

        elif "volume up" in query:
            from keyboard import volumeup
            speak("Turning volume up,sir")
            volumeup()

        elif "volume down" in query:
            from keyboard import volumedown
            speak("Turning volume down, sir")
            volumedown()
        
        elif 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play music' in query:
            webbrowser.open("https://music.amazon.in/my/playlists/51ca2b45-94d4-430a-bbd0-c78527349d24")

        elif 'play movies' in query:
            url ="https://music.amazon.in/my/playlists/51ca2b45-94d4-430a-bbd0-c78527349d24"
            open(url)

        elif "temperature" in query:
            search = "temperature in mehsana"
            url = f"https://www.google.co.in/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp =data.find("div", class_ ="BNeawe").text
            speak(f"current {search} is {temp}.") 
            
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the rime is {strTime}")


        elif "finally sleep" in query:
            speak("Going to sleep,sir")
            exit()

        elif "shutdown the system" in query:
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")
            else:
                speak(" Not a Problem!")

