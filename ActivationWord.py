# voice_activation.py
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

from config import recognizer,SAMPLE_RATE
from SpeechRecognition import recognize_speech 
from RecordSpeech import record
from TTSEngine import speak

ACTIVATION_GREETINGS = ["hi", "hey", "hello"]
ACTIVATION_NAMES = ["chat", "chad", "cha", "ch"]

filename = "prompt.wav"

def deconstruct(text):
    return set(word for word in text.strip().split())

def detect_activation_word(SILENCE_THRESHOLD):
    try:
        print("Listening for activation word...")

        #we were previously using SpeechRecognition's Microphone class to record audio. however, Microphone depends on pyaudio, which we couldn't make work on linux, so we switched to sounddevice
        audio = sd.rec(int(5 * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
        sd.wait()
        sf.write(filename, audio, SAMPLE_RATE)

        with sr.AudioFile(filename) as source:
            audio_data = recognizer.record(source)
            text = deconstruct(recognizer.recognize_google(audio_data).lower())

        if any(greeting in text for greeting in ACTIVATION_GREETINGS) and \
           any(name in text for name in ACTIVATION_NAMES):
            print("Activation word detected!")
            speak("Hi!")
            return True
        return False

    except sr.UnknownValueError:
        print("sorry, i didn't understand")
        return False

    except sr.RequestError as e:
        print(f"request failed: {e}")
        return False
