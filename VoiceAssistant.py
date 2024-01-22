import speech_recognition as sr
import os
import webbrowser
import random
import datetime
import pyttsx3
import wikipedia
chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"Hrutik: {query}\n Jarvis: "
    response_text = f"Simulated response for: {query}"
    say(response_text)
    chatStr += f"{response_text}\n"
    return response_text

def say(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(f"Error: {e}")
            return "Some Error Occurred. Sorry from Jarvis"

def process_query(query):
        try:
            result = wikipedia.summary(query, sentences=1)
            return result
        except wikipedia.exceptions.DisambiguationError as e:
            return "Multiple results found. Please be more specific."
        except wikipedia.exceptions.PageError as e:
            return "No information found. Please try a different query."
        
if __name__ == '__main__':
    print('Welcome to our A.I')
    say("Welcome to our AI")
    print("Tasks:")
    print("For opening any website say \"Open _Websitename_\"")
    print("For any information say who \"_question_ or what _question_\" ")
    print("For Opening notepad say \"open notepad\"")
    print("For checking time Say \"Time\"")
    print("For Opening notepad say \"open notepad\"")
    print("For searching anything say \"search _thing to be searched_\"")
    print("For playing song say \"music\"")
    print("For listing joke say \"Tell me a joke\"")   
    print("Say \"wish me\" for wishing ")
    print("Say \"Exit\" for exit")
    while True:
        
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "music" in query:
            musicPath = r"E:\\RCOEM MCA\\Python\\01 - Tere Hoke Rehengay - DownloadMing.SE.mp3"
            os.system(f"start {musicPath}")
        elif "time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hours {min} minutes")
        elif "open notepad".lower() in query.lower():
            os.system("start /B /WAIT notepad.exe") 
        elif "search" in query.lower():
            query = query.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif "tell me a joke" in query.lower():
            jokes = ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!", "Why did the coffee file a police report? It got mugged!"]
            say(random.choice(jokes))
        elif "wish me" in query.lower():
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                say("Good Morning!")
            elif hour>=12 and hour<18:
                 say("Good Afternoon sir !")   
            else:
                say("Good Evening sir!")
        elif query.lower().startswith("who is") or query.lower().startswith("what is"):
            result=process_query(query)
            print(result)
            say(result)
        elif "Exit".lower() in query.lower():
            exit()
        
        else:
            print("Chatting...")
            chat(query)
