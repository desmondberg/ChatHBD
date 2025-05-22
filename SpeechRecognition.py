import speech_recognition
import pyaudio
import pyttsx3

recognizer = speech_recognition.Recognizer()

def recognize_speech():
    try:
        
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

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
    