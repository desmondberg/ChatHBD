import audioop
from config import sd, SAMPLE_RATE
import numpy as np

def calibrate_silence_threshold(duration=1):
    print("calibrating silence threshold....")
    
    #record a bit of sound
    num_samples = int(SAMPLE_RATE * duration)
    audio = sd.rec(num_samples, samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()

    #convert to 16 bit
    raw_data = audio.astype(np.int16).tobytes()
    rms = audioop.rms(raw_data, 2)

    #set the threshold just above the ambient noise
    threshold = int(rms * 1.6) 

    print(f"set silence threshold to: {threshold}")
    return threshold