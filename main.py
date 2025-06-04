from ActivationWord import detect_activation_word
from SpeechRecognition import recognize_speech
from config import mic
from config import recognizer
from PromptAPI import complete
from TTSEngine import speak
from GetTemperatureAndHumidity import getTemperature,getHumidity

print("ChatHBD up and running")

print("calibrating microphone... please wait")
with mic as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print(f"set silence threshold to: {recognizer.energy_threshold}")


#once activation word was detected and the user's prompt was received, send user's prompt to recognize_speech()
if detect_activation_word():
    while True:
        command = recognize_speech("./audio/prompt.wav")
        if command:
            print(f"prompt received: {command}")
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
        speak("Do you have another request?")
        
