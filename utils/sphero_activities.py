import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.types import Color
from gtts import gTTS
import os
from utils.utils import *
import numpy as np
import random

# all activity tipes
tips = {"eyes":"Do you want to relax your eyes? You can look at something 20 feet away for 20 seconds!",
        "cross":"I know a good strech! Cross your legs and touch your toes.",
        "shake":"Let's play a game called shake shake shake!",
        "yoga":"Are you ready for some yoga?"}

###############################################################
# all functions for Sphero's social and physical behavior
###############################################################

# function for sphero yoga activity
def yoga(droid, behavior = 'social'):
    speak("Start by standing tall, feet grounded, and take a deep breath in.")
    time.sleep(3)
    speak("Now reach your arms up overhead and stretch toward the sky. Don't forget to breathe")
    # droid.spin(45, 0.3)
    # spin(-45, 0.3)
    time.sleep(5)
    speak("Exhale, bend forward slowly, and let your arms hang loose.")
    # roll(180, 40, 1)
    time.sleep(6)
    speak("Now step back into a gentle plank pose.")
    # roll(0, 60, 1.5)
    time.sleep(8)
    speak("Lower your knees and press into child's pose. Breathe deeply.")
    # set_main_led("blue")
    time.sleep(8)
    speak("When you're ready, slowly roll up to a seated position.")

    if behavior == 'social':
        time.sleep(3)
        speak("Bring your hands together at your heart and take one last deep breath in.")
        # set_main_led("white")
        time.sleep(3)
        droid.spin(360, 0.3)
        speak("Great job! This is the end of our yoga session. Namaste.")
        time.sleep(2)
    else:
        speak("Now, let's do a short mindfulness exercise.")
        time.sleep(0.5)
        speak("Close your eyes and take me in your hands. Take a long breath in.")
        time.sleep(4)
        speak("Take a long breath out")
        time.sleep(4)
        speak("As you relax, you can roll me around with your hands! Feel my weight and the texture of my shell. Am I heavy or light? Am I soft or hard?")
        time.sleep(5)
        for _ in range(4):
                droid.set_heading(30)
                droid.set_heading(-30)
        time.sleep(1)
        speak("Do you feel my wiggle?")
        for _ in range(4):
                droid.set_heading(30)
                droid.set_heading(-30)
        time.sleep(2)
        speak("Now, let's take 3 more breath. During each breath, just feel the weight of my body in your hands.")
        for _ in range(3):
            speak("Breathe in deep")
            time.sleep(3)
            speak("Breathe out.")
            time.sleep(3)
        speak("Great job!  I hope you feel the peace and joy from this fun little exercise!")

# function for sphero shake activity
def shake(droid, behavior = 'social'):
    if behavior == 'social':
        speak("Follow my instructions! This is a fun exercise I used to do back at the Sphero Choral Music Society!")
        time.sleep(0.2)
        speak("For each limb, I will count from 1 to a certain number, and you will keep shaking that limb till I finish counting. Ready?")
        time.sleep(0.5)
        speak("ok! Let's get started")
        for i in ['1,2,3,4','1,2,3','1,2','1']:
            droid.set_main_led(get_random_color())
            
            speak("Shake your left arm!" + i)
            droid.set_main_led(get_random_color())
            for _ in range(2):
                droid.set_heading(30)
                droid.set_heading(-30)
            speak("Shake your right arm!" + i)
            droid.set_main_led(get_random_color())
            for _ in range(2):
                droid.set_heading(30)
                droid.set_heading(-30)
            speak("Shake your left leg!" + i)
            droid.set_main_led(get_random_color())
            for _ in range(2):
                droid.set_heading(30)
                droid.set_heading(-30)
            speak("Shake your right leg!" + i)
            for _ in range(2):
                droid.set_heading(30)
                droid.set_heading(-30)
            # time.sleep(0.1)
        time.sleep(0.5)
        speak("That's it. I hope you feel refreshed!")
        droid.spin(360, 0.5)
        droid.set_main_led(Color(r=0, g=0, b=0))
    else:
        speak("Follow my instructions! This is a fun exercise I used to do back at the Sphero Choral Music Society!")
        time.sleep(0.2)
        speak("For each limb, I will count from 1 to a certain number, and you will keep shaking that limb till I finish counting. You will also take me in one of your hands and shake me. Ready?")
        time.sleep(0.5)
        speak("ok! Let's get started")
        for i in ['1,2,3,4','1,2,3','1,2','1']:
            droid.set_main_led(get_random_color())
            speak("Shake your left arm!" + i)
            droid.set_main_led(get_random_color())

            speak("Shake your right arm!" + i)
            droid.set_main_led(get_random_color())

            speak("Shake your left leg!" + i)
            droid.set_main_led(get_random_color())

            speak("Shake your right leg!" + i)

            # time.sleep(0.1)
        speak("Wow I feel so dizzy from all that shaking! Do you?")
        time.sleep(0.5)
        speak("That's it. I hope you feel refreshed!")

        droid.set_main_led(Color(r=0, g=0, b=0))

# function for sphero stretch activity
def stretch(droid, behavior = 'social'):
    speak("Let's stay down here for 5 seconds.")
    for i in range(1,6):
        speak(str(i))
        time.sleep(0.5)
    speak("now slowly come up, vertebrate by vertebrate.")
    droid.spin(360, 0.5)
    droid.set_main_led(get_random_color())

    if behavior == 'social':
        speak("Oh wow do you feel that stretch? Feels so good! Now let's switch to the other side!")
        for i in range(1,6):
            speak(str(i))
            time.sleep(0.5)
        droid.set_main_led(Color(r=0, g=0, b=0))
        speak("Now, slowly come up again, vertebrate by vertebrate. How do you feel?")
    else:
        
        speak("Now let's play a game of chase! I will move around in random directions and you will come and get me! Woohoo!")
        # sphero begins running around
        for _ in range(15):
            droid.roll(np.random.randint(-180, 180), 180, 2.5)
        speak("wow that was quite workout! I feel refreshed! Do you?")
        droid.set_main_led(Color(r=0, g=0, b=0))

# function for eye exercise
def eyes(droid, behavior = 'social'):
    if behavior == 'social':
        speak("What do you see in the distance? Are there any houses or trees? Anything that looks interesting to you?")
        time.sleep(3)
        speak("You know, once when I did this activity, I saw a giant hawk perched right outside of my window. It was magnificent! Do you see a hawk right now?")
        time.sleep(2)
        speak("If not, that's ok. Move your eyes upwards.....then look right as far as you can! Now look downwards towards the ground...Now move your eyes left.....and back up towards the sky!")
        time.sleep(8)
        droid.set_main_led(Color(r=0, g=150, b=0))
        droid.spin(360, 0.5)        
        droid.set_main_led(Color(r=0, g=0, b=0))
    else:
        speak("What do you see in the distance? Are there any houses or trees? Anything that looks interesting to you?")
        time.sleep(3)
        speak("You know, once when I did this activity, I saw a giant hawk perched right outside of my window. It was magnificent! Do you see a hawk right now?")
        time.sleep(2)
        speak("Now let's do something fun! Juggle me between your left and right hands and let your eyes trace my trajectory! We'll do this for 10 seconds.")
        # spehro makes weeeee sound when being juggled

        x,y,z= 0,0,0
        threshold = 50
        max_threshold = 300
        for _ in range(100):
            gyro = droid.get_gyroscope()
            if gyro is not None:
                # print(gyro)
                if abs(gyro['z'] - z) > threshold and abs(gyro['x'] - x)> threshold and abs(gyro['y'] - y)> threshold:
                    if random.randint(1,6) <= 3:
                        speak("Weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                    droid.set_main_led(get_random_color())
                    if abs(gyro['z'] - z) > max_threshold and abs(gyro['x'] - x)> max_threshold and abs(gyro['y'] - y)> max_threshold:
                        speak("Careful don't drop me!")
                x,y,z = gyro['x'],gyro['y'],gyro['z']
            time.sleep(0.2)
        droid.set_main_led(Color(r=0, g=0, b=0))

# this functio is for testing individual activity functions
def individual_testing():
    toy = scanner.find_toy(toy_name="SB-69F1")
    with SpheroEduAPI(toy) as droid:
        # droid.register_event(EventType.on_collision, on_freefall)
        # function to test
        shake(droid,'physical')
        # cross(droid, 'physical')
        # eyes(droid, "physical")
        # yoga(droid, 'physical')
        

if __name__ == '__main__':
    individual_testing()

    