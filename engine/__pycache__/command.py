import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    print(voices)
    engine.setProperty('voice', voices[0].id)  # kerak bo‘lsa voices[1] qilib ko‘ring
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()

@eel.expose

def takecomand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        eel.displayMessage()
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.displayMessage2(query)
        speak(query)
        eel.showHood()
    except Exception as e:
        
        return "None"
    return query.lower()    

text = takecomand()


speak("text")