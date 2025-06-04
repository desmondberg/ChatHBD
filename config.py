import sounddevice as sd
import speech_recognition as sr

# SETTINGS
SILENCE_DURATION = 2    
CHUNK_DURATION = 0.5    
SAMPLE_RATE = 16000 

# DEVICES
recognizer = sr.Recognizer()

