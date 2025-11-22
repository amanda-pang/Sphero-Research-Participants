import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
from gtts import gTTS
import os
import numpy as np

def speak(text):
    text_to_speak = text
    tts = gTTS(text=text_to_speak, lang='en')
    tts.save("speech.mp3")
    os.system("afplay speech.mp3")

def get_random_color():
    return Color(r = np.random.randint(255), g = np.random.randint(255), b=np.random.randint(255))
