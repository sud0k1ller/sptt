#!/usr/bin/python3 

import time
import os


class colors:
    BLACK = '\033[30;'
    GREEN = '\033[92;'
    RESET = '\033[0m'


class bcolors:
    BLUE = '47m'
    BLACK = '0m'
    PURPLE = '45m'


def flush():
    os.system("clear")

def countdown(sec, text, color, bcolor):
    while sec:
        print('\033[1m' + str(sec) + colors.RESET + '\t' + color + bcolor + text + colors.RESET)
        sec -= 1
        time.sleep(1)
        flush()
    
def switch():
    countdown(5, "SWITCH", colors.GREEN, bcolors.BLACK)
    
def rest(sec):
    countdown(sec, "REST", colors.BLACK, bcolors.BLUE)

def monday_training():
    warmup()

def wednesday_training():
    pass

def friday_training():
    pass

def warmup():
    countdown(120, "ROPE JUMP", colors.GREEN, bcolors.PURPLE)
    switch()
    countdown(180, "DYNAMIC STRETCH", colors.GREEN, bcolors.PURPLE)
    rest(60)

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


flush()
monday_training()
#print(bcolors.BLACK + colors.GREEN + "TEST" + colors.RESET)
