# -*- coding: utf-8 -*-

# pre defined libraries
import subprocess

def check_requirements():
    print("Checking requirements / installing...")
    subprocess.call('pip install pyttsx3', shell = True)
    subprocess.call('pip install speechRecognition', shell = True)
    subprocess.call('pip install wikipedia', shell = True)
    subprocess.call('pip install beautifulsoup4', shell = True)


#check_requirements()

# pre defined modules
import datetime
import webbrowser
import sys, time, os
import random

# third party modules
import pyttsx3
import speech_recognition as sr
import wikipedia

# microsoft speech api
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def animate(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)

def output(response):
    animate(response)
    speak(response)
    os.system("cls")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        output("Waiting for response...")
        r.pause_threshold = 1 # pause_threshold is seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        output("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        output(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        output("Say that again please...")
        return "None"
    return query


def wishMe():
    output("Hi!")
    hour = int(datetime.datetime.now().hour)
    if(hour >= 6 and hour < 12):
        output("Good Morning!")
    elif(hour >= 12 and hour < 15):
        output("Good noon!")
    elif(hour >= 15 and hour < 18):
        output("Good afternoon!")
    else:
        output("Good evening!")
    output("How may I help you?")


def query_wikipedia(query):
    output("Searching wikipedia...")
    webbrowser.open("https://en.wikipedia.org/wiki/"+query.replace("wikipedia", ""))
    try:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        output("According to wikipedia..."+results)
    except Exception as e:
        # print(e)
        output("Your query is very confusing...")


def query_google(query):
    webbrowser.open("https://www.google.com/")


def search_google(query):
    webbrowser.open("https://www.google.com/search?q="+query.replace("search google", ""))


def query_facebook(query):
    webbrowser.open("https://www.facebook.com/")


def query_youtube(query):
    webbrowser.open("https://www.youtube.com/")


def search_youtube(query):
    webbrowser.open("https://www.youtube.com/results?search_query="+query.replace("search youtube",""))


def play_music():
    fileHandler = open ("music_directories.txt", "r")

    listOfLines = fileHandler.readlines()

    fileHandler.close()
    directory_list = []

    for line in listOfLines:
        directory_list.append(line.strip())

    for x in range(1):
        rindex = random.randint(1,len(directory_list))
    music_dir = directory_list[rindex]

    #music_dir = "D:\\Music"
    songs = os.listdir(music_dir)
    # print(songs)
    for x in range(1):
        rindex = random.randint(1,len(songs))
    os.startfile(os.path.join(music_dir, songs[rindex]))


def query_mail():
    webbrowser.open("https://mail.google.com/mail/")


def query_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    output(f"the time is {time}")


def open_calculator():
    pass


if __name__ == "__main__":
    wishMe()
    while(True):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            query_wikipedia(query)
        elif "open youtube" in query:
            query_youtube(query)
        elif "search youtube" in query:
            search_youtube(query)
        elif "open google" in query:
            query_google(query)
        elif "search google" in query:
            search_google(query)
        elif "open facebook" in query:
            query_facebook(query)
        elif "play music" in query:
            play_music()
        elif "the time" in query:
            query_time()
        elif "open calculator" in query:
            open_calculator()
        elif "open mail" in query:
            query_mail()
        elif "close" in query:
            quit()
