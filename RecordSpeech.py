import speech_recognition as sr
import time
import wave
import audioop

from config import mic
from config import recognizer
from config import SILENCE_DURATION
from config import SILENCE_THRESHOLD
from config import CHUNK_DURATION


def record():
    frames = []
    silent_time = 0
    print("Recording... Speak into the mic.")

    with mic as source:

        while True:

            audio = recognizer.record(source, duration=CHUNK_DURATION)
            raw_data = audio.get_raw_data()
            frames.append(raw_data)


            rms = audioop.rms(raw_data, 2)  

            if rms < SILENCE_THRESHOLD:
                silent_time += CHUNK_DURATION
            else:
                silent_time = 0

            if silent_time >= SILENCE_DURATION:
                print("Silence detected. Stopping recording.")
                break

    print("Saving audio...")

    #save result as WAV
    with wave.open("audio/prompt.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2) 
        wf.setframerate(16000)
        wf.writeframes(b''.join(frames))

    print("Saved to prompt.wav")
