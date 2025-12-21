import pyttsx3

def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    print(voices)
    engine.setProperty('voice', voices[0].id)  # kerak bo‘lsa voices[1] qilib ko‘ring
    engine.setProperty('rate', 174)

    engine.say(text)
    engine.runAndWait()

speak("Hello, I am J.A.R.V.I.S")