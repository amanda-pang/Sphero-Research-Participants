import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
from gtts import gTTS
import os
from utils.utils import *
import numpy as np
from utils.sphero_activities import *
import random
import asyncio

def main(behavior = 'social'):
    activities = [0,1,2,3]
    keys = list(tips.keys())
    toy = scanner.find_toy() #toy_name="SB-69F1"
    with SpheroEduAPI(toy) as droid:
        # randomly shuffle the order of activities
        random.shuffle(activities)
        activity_order = activities[:]
        i = 0
        while True:
            time.sleep(1200)
            # time.sleep(5)
            # await asyncio.sleep(5)
            speak("It is time to take a break, let's get up and stretch")
            # pick an activity
            tip = keys[activity_order[i]]
            speak(tips[tip])
            # if behavior == 'social':
                # social group
            time.sleep(1)
            if tip == 'eyes':
                eyes(droid,behavior)
            elif tip == 'cross':
                stretch(droid,behavior)
            elif tip == "shake":
                shake(droid,behavior)
            elif tip == 'yoga':
                yoga(droid,behavior)
                
            speak("Now let's get back to work!")
            if i == 3:
                i = 0
            else:
                i += 1
if __name__ == '__main__':
    main()
