import pyttsx3 as p
import speech_recognition as sr
import selenium_web as sb
import yt_auto as yt
from news import *
import randfacts
from jokes import *
from weather import *
import datetime


engine=p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices)
# print(rate)
# engine.say("Hello, how are you.")
# engine.runAndWait()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>8 and hour<12:
        return "morning"
    elif hour>=12 and hour<16:
        return"afternoon"
    else:
        return("evening")
r=sr.Recognizer()
today_date = datetime.datetime.now()
speak(f"Hello sir good {wishme()}, I am your voice assistant.")
speak("today is "+ (today_date.strftime("%d")) +"of " + (today_date.strftime("%B")) + "and" + " its currently " + (today_date.strftime("%I")) + ":" + (today_date.strftime("%H")) + ":" + (today_date.strftime("%c")) )
speak(f"temperature in new delhi is {round(temp()-273,1)} degree celsius with {description()}")
speak('what can i do for you.')

with sr.Microphone() as  source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)

if 'what' and 'about' and 'you' in text:
    speak('I am also having a good day sir.')
speak('what can i do for you.')
with sr.Microphone() as  source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio=r.listen(source)
    text2 = r.recognize_google(audio)


if "information" in text2:
    speak("You need to information related to which topic?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
        speak(f"searching {infor} in wikipedia.")

    assist = sb.infow()
    assist.get_info(infor)


elif "play" and "video" in text2:
    speak("What do you want to play??")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
        speak(f"playing {vid} on youtube.")
    yt_play = yt.music()
    yt_play.play(vid)

elif "news" in text2:
    print("sure sir, Now I will read news for you.")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" or "facts" in text2:
    speak("sure sir.")
    x=randfacts.getFact()
    print(x)
    speak("Did you know that,"+x)
elif "joke" or "jokes" in text2:
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])


