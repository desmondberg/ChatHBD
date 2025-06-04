from ActivationWord import detect_activation_word
from SpeechRecognition import recognize_speech
from config import SAMPLE_RATE, sd
import audioop
from PromptAPI import complete
from TTSEngine import speak
from GetTemperatureAndHumidity import getTemperature,getHumidity
from calibrate import calibrate_silence_threshold
from RecordSpeech import record


SILENCE_THRESHOLD = calibrate_silence_threshold()
command = None
print("ChatHBD up and running")

#once activation word was detected and the user's prompt was received, send user's prompt to recognize_speech()
if detect_activation_word(SILENCE_THRESHOLD):
    while True:
        record(SILENCE_THRESHOLD)
        command = recognize_speech("./audio/prompt.wav")
        if command:
            print(f"prompt received: {command}")
            if(command=="stop"):
                break
            print("sending prompt to API...")
            response = complete(command)
            #if response content is TEMP or HMDT, check the temperature or humidity sensors respectively
            if response.content == "TEMP":
               temperature = getTemperature()
               print(temperature)
               speak(temperature)
            elif response.content == "HMDT":
                humidity = getHumidity()
                print(humidity)
                speak(humidity)
            else:
                speak(response.content)
        speak("Do you have another request? say stop if you want to exit the interaction.")
        
