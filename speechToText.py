import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load audio file
with sr.AudioFile("sample.flac") as source:
    audio_data = recognizer.record(source)

try:
    print("I think you said " + recognizer.recognize_vosk(audio_data))
except sr.UnknownValueError:
    print("I didn't understand, sorry.")
except sr.RequestError as e:
    print("Error: {0}".format(e))