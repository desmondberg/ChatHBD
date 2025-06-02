from gtts import gTTS
import os

language = "en"
#text = "Hello world"

#speech = gTTS(text=text, lang=language, slow=False, tld="com.au" )
#speech.save("textToSpeech.mp3")
def speak_text(text, lang='en'):
    # Convert text to speech
    tts = gTTS(text=text, lang=lang)
    
    # Save the audio file
    filename = "response.mp3"
    tts.save(filename)
    
    # Play the audio
    os.system(f"mpg123 {filename}")