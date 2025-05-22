import speech_recognition
import pyttsx3
import pyaudio

ACTIVATION_WORD = "hey chat"

recognizer = speech_recognition.Recognizer()
# TTS is text to speech
TTS_engine = pyttsx3.init()

def speak(text):
    TTS_engine.say(text)
    TTS_engine.runAndWait()

def detect_wake_word():
    try:
        with speech_recognition.Microphone() as mic:
            print("Listening for activation word")
            audio = recognizer.listen(mic, phrase_time_limit=5)

            text = recognizer.recognize_google(audio).lower()
            print(text)

            if ACTIVATION_WORD in text:
                print("Activation word detected!")
                speak("Hello, how can I assist you?")
                return True
            return False

    except speech_recognition.UnknownValueError:
        print("Could not understand audio.")
        return False
    
    except speech_recognition.RequestError as e:
        print(f"Could not request results; {e}")
        return False
