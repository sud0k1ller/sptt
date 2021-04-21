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
    exercise(5, "SWITCH", colors.BLACK, bcolors.WHITE, comming_up)

def rest(sec, comming_up):
    exercise(sec, "REST", colors.BLACK, bcolors.BLUE, comming_up)

def training(cycles_list):
    training_time = count_training_time(cycles_list)

    exercise(5, "COUNTDOWN", colors.BLACK, bcolors.WHITE, cycles_list[0][0][0][0])
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
        os.system('\a')     
        exercise(exercise_table[exercise_number][1], exercise_table[exercise_number][0], colors.RED, bcolors.YELLOW, exercise_table[exercise_number + 1][0])
        os.system('\a')     
        switch(exercise_table[exercise_number + 1][0])
    os.system('\a')     
    exercise(exercise_table[-1][1], exercise_table[-1][0], colors.RED, bcolors.YELLOW, "REST")
    os.system('\a')     

def exercise(exercise_time, exercise_name, color, bcolor, comming_up):
    while exercise_time:
        flush()
        print('\033[1m' + str(exercise_time) + colors.RESET + '\t' + color + bcolor + exercise_name + colors.RESET)
        print('\t\033[100mCOMMING UP: ' + comming_up + colors.RESET)
        print("\nTIME IN TRAINING:")
        print(str(datetime.timedelta(seconds = int(time.time() - start_time))))
        print("\n\nTIME TO FINISH:")
        print(str(datetime.timedelta(seconds = int(training_time - (time.time() - start_time - 1)))))
        print("\n\nTOTAL TRAINING TIME:")
        print(str(datetime.timedelta(seconds = training_time)))
        #print("\n\n[SPACE] Pause/Resume")
        exercise_time -= 1
        time.sleep(1)

def count_training_time(cycles_list):
    training_time = 5                                                       # Initial Countdown Time 
    for cycle in cycles_list:
        cycle_repetitions_count = int(cycle[2]) 
        training_time += cycle[1] * cycle_repetitions_count                 # Rests Times 
        training_time += 5 * (len(cycle[0]) - 1) * cycle_repetitions_count   # Switch Times
        for exercise in cycle[0]:   
            training_time += exercise[1] * cycle_repetitions_count          # Exerises Times
    return training_time 

##MAIN
warmup_exercises =      [["ROPE JUMPING", 120],
                        ["DYNAMIC STRETCH", 180]]

monday_workout = 	    [["BULGARIAN SQUATS - LEFT LEG", 60],
				        ["BULGARIAN SQUATS - RIGHT LEG", 60],
				        ["SQUAT JUMPS", 60],
				        ["REVERSE LUNGES", 60],
				        ["ALTERNATING INCLINE HIP THRUSTS", 60],
                        ["PUSH UPS", 60], 
				        ["EXPLOSIVE PUSH UPS", 40], 
				        ["90 DEGREE HOLD", 20]]
    
   
back_and_arms_workout = [["SUPERMANS", 60], 
			            ["TOWEL PULL UPS", 60], 
				        ["TYI", 60], 
				        ["ONE HANDED DOORPOST ROWS - RIGHT SIDE", 30], 
				        ["ONE HANDED DOORPOST ROWS - LEFT SIDE", 30],
				        ["DIAMOND PUSH UPS", 60], 
				        ["REVERSE PUSH UPS", 60],
				        ["PIKE PUSH UPS", 60]]

core_A_workout = 		[["HIP LIFTS", 60], 
				        ["SIDE PLANK - LEFT SIDE", 30], 
				        ["SIDE PLANK - RIGHT SIDE", 30], 
				        ["RUSSIAN TWISTS", 60]]
    
core_B_workout = 		[["KNEE TO ELBOW IN PLANK", 60], 
				        ["SCISSORS", 60], 
				        ["STRAIGHT LEGS LIFTS", 60]]

cooldown =              [["COOLDOWN", 300]]


short_debug_cycle =     [["EX1", 5],
                        ["EX2", 5],
                        ["EX3", 5]]

short_debug_cooldown =  [["COOLDOWN", 5]]

short_debug_training =  [[short_debug_cycle, 2, 2],
                        [short_debug_cooldown, 0, 1]]



#MONDAY TRAINING
monday_training =   [[warmup_exercises, 15, 1],
                    [monday_workout, 60, 3],
                    [core_A_workout, 30, 3],
                    [cooldown, 0 , 1]]

#WEDNESDAY TRAINING
wednesday_training =   [[warmup_exercises, 15, 1],
                        [back_and_arms_workout, 60, 3], 
                        [core_B_workout, 30, 3], 
                        [cooldown, 0, 1]]

training_list = [   "[~45 min] Hard Legs + Light Chest + ABS Training",
                    "[~45 min] Back + Arms + ABS Training"]

training_choosen = False
while not training_choosen:
    flush()
    print("\n")
    for training_name, number in zip(training_list, range(1,len(training_list)+1)):
        print("[" + str(number) + "]\t" + training_name)
    
    training_number = input("\nSelect Training Number: ")
    if training_number == "1":
        training_cycles = monday_training
        training_choosen = True
    if training_number == "2":
        training_cycles = wednesday_training
        training_choosen = True

start_time = time.time()
training_time = count_training_time(training_cycles)
training(training_cycles)
input(colors.GREEN + bcolors.WHITE +  '\nNice Job!\nYou have done it!' + colors.RESET + '\nPress [Enter] to quit')
