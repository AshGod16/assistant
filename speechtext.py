import speech_recognition as sr
import webbrowser as wb
import requests
from text_to_speech import speak

def capitalize(s):
    for i, ch in enumerate(s):
        if ch.isalpha():
            return s[:i] + s[i].upper() + s[i+1:]

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    audio = r1.listen(source)

if 'video' in r2.recognize_google(audio):
    print('Video:\n')
    # engine.say("Say a keyword related to the video.")
    # engine.runAndWait()
    speak("Say a keyword related to the video.")
    url = 'https://youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('\tKeyword:')
        audio = r2.listen(source, timeout=10, phrase_time_limit=15)
        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new_tab(url+get)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if 'stock price' in r2.recognize_google(audio):
    print('Stock Price:\n')
    speak("Say the stock symbol of the company")
    while True:
        with sr.Microphone() as source:
            audio = r2.listen(source, timeout=10, phrase_time_limit=5)
            try:
                get = r2.recognize_google(audio)
                url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}'.format(get.upper(), 'LFNDIKWU7OTALNHD')
                result = requests.get(url)
                data = result.json()

                if not data.get("Global Quote"):
                    break
                
                speak("{} is valued at ${:.2f}".format(data["Global Quote"]["01. symbol"], float(data["Global Quote"]["05. price"].strip())))
                speak("See more information in the terminal.")
                for key, value in data["Global Quote"].items():
                    print("\t{}: {}".format(capitalize(key), value))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        # LFNDIKWU7OTALNHD
            
        
        speak("Say another stock symbol or say quit to exit.")
