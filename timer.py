#!/usr/bin/python3 

import time
import os


class colors:
    pass

class bcolors:
    pass


def flush():
    os.system("clear")

def countdown(sec, text, color):
    while sec:
        print(str(sec) + color +  " - " + text, flush = True + colors)
        sec -= 1
        time.sleep(1)
        flush()
    
def switch():
    sec = 5
    print("SWITCH!!", flush = True)
    while sec:
        print(sec)
        sec -= 1
        time.sleep(1)   
        flush()

def monday_training():
    warmup()

def wednesday_training():
    pass

def friday_training():
    pass

def warmup():
    countdown(10, "ROPE JUMP")
    switch()
    countdown(10, "DYNAMIC STRETCH")
    switch()

def cooldown():
    pass

def hard_legs_workout():
    pass

def light_legs_workout():
    pass

def hard_chest_workout():
    pass

def light_chest_workout():
    pass

def hard_core_workout():
    pass


#flush()
#monday_training()
print("\033[45;0mTEST\033[0m")
