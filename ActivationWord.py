import speech_recognition
from config import mic
from config import recognizer

from SpeechRecognition import recognize_speech, audiofile_to_audiodata
from RecordSpeech import record
from TTSEngine import speak

#broke this up into two parts-
#greetings - hi, hey, hello
#names - chat, chad (to account for the speech recognizer misinterpreting the user)

ACTIVATION_GREETINGS = ["hi","hey","hello"]
ACTIVATION_NAMES = ["chat","chad","cha","ch"]

#split the text up into a set containing each of its words in order to find matches with the activation greetings and names.
def deconstruct(text):
    return set(word for word in text.strip().split())

def detect_activation_word():
    try:
        print("Listening for activation word")
        #listen for 5 seconds
        with mic as source:
            audio = recognizer.listen(source, phrase_time_limit=5)

        text = deconstruct(recognize_speech(audio=audio).lower())
        #print(text)

        #check if the initial prompt contains any combination of the greetings and names defined above
        if any(greeting in text for greeting in ACTIVATION_GREETINGS) and any(name in text for name in ACTIVATION_NAMES):
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
