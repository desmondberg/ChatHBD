import speech_recognition as sr

# GLOBAL VARIABLES 

# SETTINGS
SILENCE_THRESHOLD = 1000 
SILENCE_DURATION = 5    
CHUNK_DURATION = 0.5    

# DEVICES
recognizer = sr.Recognizer()
mic = sr.Microphone()
