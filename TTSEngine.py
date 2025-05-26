import pyttsx3

# TTS is text to speech
TTS_engine = pyttsx3.init()

def speak(text):
    TTS_engine.say(text)
    TTS_engine.runAndWait()