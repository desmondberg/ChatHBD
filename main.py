from ActivationWord import detect_activation_word
from SpeechRecognition import recognize_speech
from config import mic
from config import recognizer


print("ChatHBD up and running")

print("calibrating microphone... please wait")
with mic as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print(f"set silence threshold to: {recognizer.energy_threshold}")

if detect_activation_word():
    command = recognize_speech()
    if command:
        print(f"Command received: {command}")
