# RecordSpeech.py
import sounddevice as sd
import numpy as np
import audioop
import wave
import time
from calibrate import calibrate_silence_threshold

from config import SILENCE_DURATION, CHUNK_DURATION, SAMPLE_RATE


filename = "audio/prompt.wav"

def record(SILENCE_THRESHOLD):
    
    frames = []
    silent_time = 0.0

    chunk_size = int(CHUNK_DURATION * SAMPLE_RATE)
    print("please speak now")

    def callback(indata, frames_, time_, status):
        nonlocal silent_time, frames

        #convert to 16 bit
        raw_data = indata.copy().astype(np.int16).tobytes()
        frames.append(raw_data)

        #calculate volume using root mean square
        rms = audioop.rms(raw_data, 2)

        #check every chunk. if the chunk's volume is below the silence threshold, add its duration to the total silent time. 
        #once the total silent time has exceeded SILENCE_DURATION, stop the recording.
        if rms < SILENCE_THRESHOLD:
            silent_time += CHUNK_DURATION
        else:
            silent_time = 0.0

        if silent_time >= SILENCE_DURATION:
            print("silence detected. recording stopped")
            raise sd.CallbackStop()

    try:
        with sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype='int16',
            callback=callback,
            blocksize=chunk_size
        ) as stream:
            while stream.active:
                time.sleep(0.1)
    except sd.CallbackStop:
        pass

    print("saving audio...")

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2) 
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(b"".join(frames))

    print(f"Saved to {filename}")
