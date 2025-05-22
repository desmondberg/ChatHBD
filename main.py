from ActivationWord import detect_activation_word
from SpeechRecognition import recognize_speech

if detect_wake_word():
    command = recognize_speech()
    if command:
        print(f"Command received: {command}")
