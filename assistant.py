import datetime
import subprocess
import jdatetime
import pickle
import datetime
import random
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import cv2
import numpy as np
import matplotlib.pyplot as plt
"""
   ...: img = cv2.imread('wp2.png')
   ...: b,g,r = cv2.split(img) 
   ...: img2 = cv2.merge([r,g,b]) 
   ...: plt.subplot(121);plt.imshow(img) # expects distorted color 
   ...: plt.subplot(122);plt.imshow(img2) # expect true color 
   ...: plt.show() 
   ...:  
   ...: cv2.imshow('bgr image',img) # expects true color 
   ...: cv2.imshow('rgb image',img2) # expects distorted color 
   ...: cv2.waitKey(0) 
   ...: cv2.destroyAllWindows()  
"""
def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            time.sleep(20)

    return said

class Cal:
    class jalali:
        def hour():
            print(f'it is {jdatetime.datetime.now().strftime("%H:%M")}')
            speak(jdatetime.datetime.now().strftime("%H %M"))
        def day():
            print(jdatetime.datetime.now().strftime("%dام"))
            speak(jdatetime.datetime.now().strftime("%d"))
        def month():
            print(jdatetime.datetime.now().strftime("%m"))
            print(jdatetime.datetime.now().strftime("%h"))
            speak(jdatetime.datetime.now().strftime("%h"))
        def year():
            print(jdatetime.datetime.now().strftime("%Y"))
            speak(jdatetime.datetime.now().strftime("%Y"))
        def today():
            print(jdatetime.date.today())
            speak(jdatetime.date.today())
        def all():
            print(jdatetime.datetime.now())
            speak(jdatetime.datetime.now())
        def week():
        	print(datetime.datetime.now().strftime("%a"))
        	print(datetime.datetime.now().strftime("%a"))

    class Miladi:
        def all():
            print(datetime.datetime.now().strftime("%F"))
            speak(datetime.datetime.now().strftime("%F"))
        def month():
            print(datetime.datetime.now().strftime("%m"))
            print(datetime.datetime.now().strftime("%h"))
            speak(datetime.datetime.now().strftime("%h"))
        def week():
            print(datetime.datetime.now().strftime("%a"))
            print(datetime.datetime.now().strftime("%a"))


def run(name):
    try:
        #print(f"Opening {name.lower()}")
        speak(f"opening {name}")
        subprocess.Popen(name.lower())
    except:
        speak("An Error has oucurred")
        print("An Error has oucurred")
def open_file(filename):
    try:
        speak(f"Opening {filename}")
        print(f"Opening {filename} .....")
        subprocess.Popen(["nano", filename])
        print(f'Opened {filename}')
        speak(f'Opened {filename}')
    except:
        print("file not found")
        speak("file not found")
def show(img):
    img = cv2.imread(img)
    b,g,r = cv2.split(img)
    img2 = cv2.merge([r,g,b])
    plt.subplot(121) # plt.imshow(img)  expects distorted color
    plt.subplot(122) # plt.imshow(img2) # expect true color
    #plt.show()
    cv2.imshow('bgr image',img) # expects true color
    # cv2.imshow('rgb image',img2) # expects distorted color
    cv2.waitKey(0)
    cv2.destroyAllWindows()


while True:
        text = get_audio()
        print(f"you: {text}")
        if "hello" in text:
            speak("Hi. How are you today?. how can i help you?")
            print("ai: Hi. How are you today?. how can i help you?")
        elif text.startswith("run") or "run" in text:
            app_name = text.split()[1]
            print(f"Opening {app_name} ...")
            run(app_name)
            print(f"Opened {app_name}")
        elif text.startswith("open") or "open" in text:
            file_name = text.split()[1]
            file_ex = text.split()[2]
            open_file(f"{file_name}.{file_ex}")
        elif text.startswith("what time is it") or "what time is it" in text:
        	Cal.jalali.hour()
        elif text.startswith("what date is it") or "what date" in text:
        	Cal.Miladi.all()
        elif text.startswith("what month is it") or "what month" in text:
        	Cal.Miladi.month()
        elif text.startswith("what day is it") or "what day" in text:
        	Cal.Miladi.week()
        elif text.startswith("show") or "show" in text:
                show(f'{text.split()[1]}.{text.split()[2]}')
