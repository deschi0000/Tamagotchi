import os      
import time    
from classes import *
from tamagotchi_functions import *


# t1 = Tamagotchi("DK")           #Debugging Instance
t1 = intro()

while t1.is_alive:

    for i in range(0,3):    # Morning, Day and Night

        print("==================================")
        print(f"DAY {t1.age}")
        print(time_of_day_message(i))
        print("==================================")

        print(t1)
        # print("COMMANDS:")
        print("What would you like to do?")
        reset(t1)
                       
        command = command_menu(t1)
        os.system("cls")                # Do we like clearing the menu? less confusing?

        command_execute(command, t1)

        #/==========================================================
        # CHECKS!
        energy_check(t1)
        hunger_check(t1)
        age_check(t1)
        holding_check(t1)
        sick_check(t1)
        clean_check(t1)
        happiness_check(t1)
        depleter(t1)
        sleep_roll(t1)
        treasure_hunt_roll(t1)

    days_sick_check(t1)

    #  END OF DAY -> get full rest + Increment Age    
    end_of_day(t1)

    #press_enter()       #--> Using sleep command instead of enter...

death_type_check(t1)
final_stats(t1)
