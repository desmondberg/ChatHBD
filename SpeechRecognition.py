import speech_recognition
import pyaudio
import pyttsx3

from config import recognizer


def recognize_speech(audio):
    try:
        text = recognizer.recognize_google(audio)
        text = text.lower()

        print(f"Recognized {text}")
        return text
             
    except speech_recognition.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return ""
    except speech_recognition.RequestError as e:
        print(f"Could not request results; {e}")
        return ""
    