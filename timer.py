#!/usr/bin/python3 

import time
import os
import datetime

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
    GREEN = '42m'
    CYAN = '46m'

def flush():
    os.system("clear")

def switch(comming_up):
    exercise(1, "SWITCH", colors.BLACK, bcolors.WHITE, comming_up)

def rest(sec, comming_up):
    exercise(sec, "REST", colors.BLACK, bcolors.BLUE, comming_up)

def training(cycles_list):
    exercise(5, "COUNTDOWN", colors.BLACK, bcolors.WHITE, "WARMUP")
    
    for cycle_number in range(0, len(cycles_list) - 1):
        cycle_repetitions = cycles_list[cycle_number][2]
        for repetition in range(cycle_repetitions - 1):
            training_cycle(cycles_list[cycle_number][0], colors.RED, bcolors.YELLOW)            
            rest(cycles_list[cycle_number][1], cycles_list[cycle_number][0][0][0])
        training_cycle(cycles_list[cycle_number][0], colors.RED, bcolors.YELLOW)            
        rest(cycles_list[cycle_number][1], cycles_list[cycle_number + 1][0][0][0]) 
    training_cycle(cycles_list[-1][0], colors.RED, colors.YELLOW)

def training_cycle(exercise_table, color, bcolor):
    for exercise_number in range(len(exercise_table) - 1):
        exercise(exercise_table[exercise_number][1], exercise_table[exercise_number][0], colors.RED, bcolors.YELLOW, exercise_table[exercise_number + 1][0])
        switch(exercise_table[exercise_number + 1][0])
    exercise(exercise_table[-1][1], exercise_table[-1][0], colors.RED, bcolors.YELLOW, "REST")


def exercise(exercise_time, exercise_name, color, bcolor, comming_up):
    while exercise_time:
        #handle_pause()
        print('\033[1m' + str(exercise_time) + colors.RESET + '\t' + color + bcolor + exercise_name + colors.RESET)
        print('\t\033[100mCOMMING UP: ' + comming_up + colors.RESET)
        exercise_time -= 1
        print("\nTRAINING TIME:")
        print(str(datetime.timedelta(seconds=int(time.time() - start_time))))
        print("\n\nTIME LEFT:")
        print("00:00:00")
        print("\n\n[SPACE] Pause/Resume")
        time.sleep(1)
        flush()    

def count_training_time(cycles_list):
    training_time = 0

    for rest_time in
    pass

##MAIN
warmup_exercises =      [["ROPE JUMPING", 2],
                        ["DYNAMIC STRETCH", 2]]

heavy_leg_workout = 	[["BULGARIAN SQUATS - LEFT LEG", 60],
				        ["BULGARIAN SQUATS - RIGHT LEG", 60],
				        ["SQUAT JUMPS", 60],
				        ["REVERSE LUNGES", 60],
				        ["ALTERNATING INCLINE HIP THRUSTS", 60]]
    
light_chest_workout = 	[["PUSH UPS", 60], 
				        ["EXPLOSIVE PUSH UPS", 40], 
				        ["90 DEGREE HOLD", 20]]
    
   
back_and_arms_workout = [["SUPERMANS", 2], 
			            ["TOWEL PULL UPS", 2], 
				        ["TYI", 2], 
				        ["ONE HANDED DOORPOST ROWS - RIGHT SIDE", 2], 
				        ["ONE HANDED DOORPOST ROWS - LEFT SIDE", 2],
				        ["DIAMOND PUSH UPS", 2], 
				        ["REVERSE PUSH UPS", 2],
				        ["PIKE PUSH UPS", 2]]

core_A_workout = 		[["HIP LIFTS", 60], 
				        ["SIDE PLANK - LEFT SIDE", 30] , 
				        ["SIDE PLANK - RIGHT SIDE", 30], 
				        ["RUSSIAN TWISTS", 60]]
    
core_B_workout = 		[["KNEE TO ELBOW IN PLANK", 2], 
				        ["SCISSORS", 2], 
				        ["STRAIGHT LEGS LIFTS", 2]]

cooldown =              [["COOLDOWN", 300]]

start_time = time.time()
flush()

#cycle_name, rest_time, cycle_repetition_count
training([[warmup_exercises, 15, 1],[back_and_arms_workout, 3, 3], [core_B_workout, 3, 3], [cooldown, 0, 1])

