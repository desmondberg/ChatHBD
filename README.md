# ChatHBD
a raspberry pi chat assistant

This is how the voice assistant's algorithm will work -
1. Detect microphone audio and check if the activation word was said
2. ⁠Record user's speech until nothing has been detected for 5 seconds
3. ⁠The recording gets parsed into text
4. ⁠The text is fed to the ChatGPT API and the API generates a response
5. ⁠use gTTS to output the response through the speakers
