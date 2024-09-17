import pyttsx3
import datetime
import speech_recognition as sr
import wikipediaapi
import webbrowser as wb
import os
import random
import pyautogui
from googletrans import Translator

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tomorrow")
    
    speak("Jarvis at your service sir, please tell me how may I help you.")
    print("Jarvis at your service sir, please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    directory = "C:\\Users\\sudik\\Pictures\\Screenshots"
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    img.save(directory + "screenshot.png")  

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
        "Why did the computer go to therapy? It had too many bytes of emotional baggage!",
        # Add more jokes to the list as needed
    ]

    joke = random.choice(jokes)
    print(joke)
    speak(joke)

if __name__== "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm JARVIS and I'm a desktop voice assistant.")
            print("I'm JARVIS and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query or "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia","")
                wiki_wiki = wikipediaapi.Wikipedia('en')
                result = wiki_wiki.page(query)
                if result.exists():
                    summary = result.summary[:200]  # Considering first 200 characters of the summary
                    print(summary)
                    speak(summary)
                else:
                    speak("Can't find this page sir, please ask something else")
            except Exception as e:
                print("Error:", e)
                speak("Can't find this page sir, please ask something else")

        elif "open youtube" in query:
            wb.open("youtube.com") 

        elif "open google" in query:
            wb.open("google.com") 
   
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "play music" in query:
            song_dir = "C:\\Users\\sudik\\Music"
            songs = os.listdir(song_dir)
            print(songs)
            x = len(songs)
            y = random.randint(0,x)
            os.startfile(os.path.join(song_dir, songs[y]))

        elif "open chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
            
        
        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken a screenshot, please check it")

        elif "offline" in query:
            quit()

        elif "tell me a joke" in query or "joke" in query:
            tell_joke()

        # Translation functionality
        elif "translate" in query:
            speak("What would you like me to translate?")
            print("What would you like me to translate?")
            text_to_translate = takecommand()
            
            speak("To which language would you like to translate?")
            print("To which language would you like to translate?")
            target_language = takecommand()
            
            translator = Translator()

            try:
                translated_text = translator.translate(text_to_translate, dest=target_language).text
                print(f"Translated text: {translated_text}")
                speak(f"The translation is: {translated_text}")
            except Exception as e:
                speak("Sorry, I couldn't perform the translation. Please try again.")
                print(f"Translation Error: {e}")
