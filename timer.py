#!/usr/bin/python3 

import time
import os


class colors:
    BLACK = '\033[30;'
    GREEN = '\033[92;'
    RED = '\033[31;'
    BLUE = '\033[34;'
    MAGENTA = '\033[35;'
    YELLOW = '\033[93;'
    RESET = '\033[0m'


class bcolors:
    BLUE = '44m'
    BLACK = '0m'
    RED = '41m'
    MAGENTA = '45m'
    YELLOW = '43m'
    PURPLE = '45m'
    WHITE = '107m'

def flush():
    os.system("clear")

def countdown(sec, text, color, bcolor, comming_up):
    while sec:
        print('\033[1m' + str(sec) + colors.RESET + '\t' + color + bcolor + text + colors.RESET)
        print('\t\033[100mCOMMING UP: ' + comming_up + colors.RESET)
        sec -= 1
        time.sleep(1)
        flush()
    
def switch(comming_up):
   countdown(5, "SWITCH", colors.BLACK, bcolors.WHITE, comming_up)

def rest(sec, comming_up):
   countdown(sec, "REST", colors.BLACK, bcolors.BLUE, comming_up)

def monday_training():
    heavy_leg_workout = [["BULGARIAN SQUATS - LEFT LEG", 2],["BULGARIAN SQUATS - RIGHT LEG", 2],["SQUAT JUMPS", 2],["REVERSE LUNGES", 2],["ALTERNATING INCLINE HIP THRUSTS", 2]]
    light_chest_workout = [["PUSH UPS", 2], ["EXPLOSIVE PUSH UPS", 2], ["90 DEGREE HOLD", 2]]
    core_A_workout = [["HIP LIFTS", 2], ["SIDE PLANK - LEFT SIDE", 2] , ["SIDE PLANK - RIGHT SIDE", 2], ["RUSSIAN TWISTS", 2]]
    
    warmup(heavy_leg_workout[0][0])
   
    #MAIN WORKOUT
    cycles = 3
    while cycles > 1:
        cycle(heavy_leg_workout, light_chest_workout[0][0], colors.RED, bcolors.YELLOW)
        cycle(light_chest_workout, heavy_leg_workout[0][0], colors.BLACK, bcolors.MAGENTA)
        rest(3, heavy_leg_workout[0][0])
        cycles -= 1    
    
    cycle(heavy_leg_workout, light_chest_workout[0][0], colors.RED, bcolors.YELLOW)
    cycle(light_chest_workout, core_A_workout[0][0], colors.BLACK, bcolors.MAGENTA)

    
    # CORE WORKOUT
    cycles = 3
    while cycles > 1:
        cycle(core_A_workout, core_A_workout[0][0], colors.GREEN, bcolors.BLACK)
        rest(3, core_A_workout[0][0])
        cycles -= 1    
    cycle(core_A_workout, "COOLDOWN", colors.GREEN, bcolors.BLACK)

    cooldown()

def wednesday_training():
    pass

def friday_training():
    pass

def warmup(comming_up):
    warmup_exercises = [["ROPE JUMPING", 2],["DYNAMIC STRETCH", 2]]
    cycle(warmup_exercises, comming_up, colors.BLUE, bcolors.BLACK)
    switch(comming_up)

def cooldown():
   countdown(300, "COOLDOWN", colors.BLACK, bcolors.BLUE, comming_up)

def cycle(exercises_table, first_exercise_in_next_cycle, color, bcolor): 
    for exercise, index in zip(exercises_table, range(len(exercises_table))):
        if index+1 < len(exercises_table):
            countdown(exercise[1],  exercise[0] , color, bcolor, exercises_table[index+1][0])
            switch(exercises_table[index+1][0])
        else:
            countdown(exercise[1], exercise[0] , color, bcolor, first_exercise_in_next_cycle)

flush()
monday_training()
