#test code
from openai import OpenAI
import os
from dotenv import load_dotenv
#automatically load OPENAI_API_KEY
load_dotenv()

client = OpenAI()
setup = "You are a voice assistant by the name of ChatHBD. you were designed to answer the user's questions. The device you are connected to includes a temperature and humidity sensor. So, if the user asks for the temperature or humidity, detect that and simply pass TEMP or HMDT respectively as the completion. The system will use this to redirect the prompt to the hardware components. As the responses will be delivered by a TTS engine, please don't include any stylisation (bold, italics, newlines) as the engine will pronounce the raw text."



def complete(prompt):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "system", "content": setup},
        {"role": "user", "content": prompt}
        ]
    )

    print(completion.choices[0].message)
    return completion.choices[0].message

#test temperature prompt
complete("Can you tell me the temperature right now?")
#test humidity prompt
complete("What's the humidity in this room right now?")