import speech_recognition
from config import mic
from config import recognizer

from SpeechRecognition import recognize_speech, audiofile_to_audiodata
from RecordSpeech import record
from TTSEngine import speak

ACTIVATION_WORD = "hey chat"

def detect_activation_word():
    try:
        print("Listening for activation word")
        #listen for 5 seconds
        with mic as source:
            audio = recognizer.listen(source, phrase_time_limit=5)

        text = recognize_speech(audio=audio).lower()
        print(text)

        if ACTIVATION_WORD in text:
            print("Activation word detected!")
            speak("Hello, how can I assist you?")
            record()
            return True
        return False

    except speech_recognition.UnknownValueError:
        print("Could not understand audio.")
        return False
    
    except speech_recognition.RequestError as e:
        print(f"Could not request results; {e}")
        return False
