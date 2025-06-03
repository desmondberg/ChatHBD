import speech_recognition
import pyaudio
import pyttsx3

from config import recognizer

#convert an audio file to an AudioData object to pass as audio argument
def audiofile_to_audiodata(path):
    with speech_recognition.AudioFile(path) as source:
        audio = recognizer.record(source) 
        return audio


def recognize_speech(path = None, audio = None):
    try:
        #if the user provided a path to an audio file instead of an AudioData object, convert it to AudioData first
        if path:
            audio = audiofile_to_audiodata(path)
        text = recognizer.recognize_google(audio)
        text = text.lower()

        print(f"Recognized {text}")
        #TODO - pass text to ChatGPT
        return text
             
    except speech_recognition.UnknownValueError as e:
            print(f"Sorry, I could not understand the audio. {e}")
            return ""
    except speech_recognition.RequestError as e:
        print(f"Could not request results. {e}")
        return ""
    