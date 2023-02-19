from classes import Tamagotchi
from random import choice
from tamagotchi_animation import *

import os      # Clear the cmd line
import time


FOOD = ["Croissant", "Cake", "Manju", "Pasta", "Lobster Claw", "Risotto", "Gua bao"]
MAX_AGE = 10
AWAKE_COMMANDS_RESTED = ["f", "p", "u", "n"]
AWAKE_COMMANDS = ["f","r", "p", "u", "n" ]
AWAKE_COMMANDS_SICK = ["f","r", "p", "m", "n" ]
AWAKE_COMMANDS_SOILED = ["f","r", "p", "c", "n" ]
ASLEEP_COMMANDS = ["w", "r"]



def create_tamagotchi():
    '''
    This will create a tamagotchi object
    '''

    name = ""
    while len(name) == 0:
        
        name = input("What would you like to call your pet?: ")
        if len(name.strip()) == 0:
            print("Please enter some values")       
            name = ""
      
        return Tamagotchi(name)
    
def time_of_day_message(num):
    if num == 0:
        return "Good Morning!\n"
    elif num == 1:
        return "Lunchtime!\n"
    else:
        return "Eveningtime\n"

def press_enter():
    # enter_pressed = False
    userinput = "999"
    userinput = input("Press Enter to Continue")
    if userinput == "":
        os.system("cls")
        # enter_pressed = True



def rest_check(object, energy):

    if object.is_resting == True and energy == 100:                # Fully rested, wake up
        return object.wake_up()
    elif object.is_resting == False and energy == 100:             # No need to sleep
        return f"\n{object.name} is fully rested!"
    elif object.is_resting == True and energy < 100:               # Keep resting
        # sleep_animation()
        return object.rest()
    elif object.is_resting == True and object.prompt_wakeup == True:
        object.prompt_wakeup = False
        return object.wake_up()

#/==========================================================
# Checks Energy / Hunger / Age

def energy_check(object):
    # include object? Maybe if the energy is zero, invoke kill function.
    if object.energy < 15:
        warning("extreme_energy", object)
    elif object.energy < 30:
        warning("energy", object)


def hunger_check(object):
    if object.hunger > 75:
        object.lose_health()
        warning("extreme_hunger", object)
    elif object.hunger > 45:
        object.lose_health()
        warning("hunger", object)


def age_check(object):
    if object.age == MAX_AGE:
        object.is_alive = False


def happiness_check(object):
    if object.neglectometer > 8:
        object.is_sick = True
    elif object.neglectometer > 5 and object.is_playing == False:        #not is playing prevents from showing if the user just played with it
        print(f"{object.name} is feeling a little neglected...")


def reset(object):
    # Function that will reset stats that change naturally after one turn
    object.playing = False



def death_type_check(object):
    if object.age < MAX_AGE:
        print(f"{object.name} didn't make it...")
    else:
        print(f"{object.name} died peacefully of old age")


def final_stats(object):
    death_animation()
    print(f"GG! These are {object.name}'s final stats")
    print("==================================")
    print(object)
    print("==================================")

    #play death animation




def stomach_check(object):
    if object.soiled == True:
        object.is_holding == 0
    elif object.soiled == False and object.is_holding > 5:
        print(f"{object.name} Pooed!")
        object.poo()
    else:
        object.is_holding += 1



#/==========================================================



def warning(type, object): 
    if type == "energy":
        print(f"{object.name}'s is getting tired!")
    if type == "extreme_energy":
        print(f"!Careful! {object.name}'s is getting extremely tired!")
    if type == "hunger" and object.is_resting == False:
        print(f"{object.name} is hungry!")        
    if type == "extreme_hunger" and object.is_resting == False:
        print(f"!Careful! {object.name} is getting really hungry!")




def command_menu(object):

    c = "999"
    # print("\nEnter your command:")
    if object.is_resting is False and object.energy == 100:                         # Awake, fully rested, healthy
        while c.lower() not in AWAKE_COMMANDS_RESTED:
            c = input("Feed [f]  | Play [p] | Poo(u) | Do Nothing [n]\n")        
    elif object.is_resting is False and object.soiled == True:                      # Awake, soiled
        while c.lower() not in AWAKE_COMMANDS_SOILED:
            c = input("Feed [f]  |  Rest [r]  | Play [p] | Clean [c] | Do Nothing [n]\n")
    elif object.is_resting is False and object.is_sick == True:                     # Awake, sick
        while c.lower() not in AWAKE_COMMANDS_SICK:
            c = input("Feed [f]  |  Rest [r]  | Play [p] | Give Medicine [m] | Do Nothing [n]\n")    
    elif object.is_resting is False:                                                # Awake, healthy
        while c.lower() not in AWAKE_COMMANDS:
            c = input("Feed [f]  |  Rest [r]  | Play [p] | Poo(u) | Do Nothing [n]\n")
    elif object.is_resting is True:
        while c.lower() not in ASLEEP_COMMANDS:                                     # Asleep
            c = input("Wake Up [w]  |  Keep Resting [r]\n")
    return c.lower()


def command_execute(input, object):

    if input == "f":
        object.feed()
        food_message(object)

    if input == "r":                           # Rest
        if object.energy == 100:
            print(f"{object.name} is fully rested!")
        else:
            object.is_resting = True
            rest_check(object, object.energy) 
        
    if input == "w":                           # Wake up            
        # at_rest = False
        object.wake_up()

    if input == "p":                           # Play
        object.play()

    if input == "u":                           #Poo
        object.poo()
        # object.soiled = True
        print(f"{object.name} feels relieved!")

    if input == "c":
        object.clean()

    if input == "m":
        object.cure()

    if input == "n":              # Do Nothing
        rest_check(object, object.energy)
        if object.is_resting is False:
            object.neglect()




def food_message(object):
    print(f"{object.name} enjoyed eating {choice(FOOD)}")

        
def clean_check(object):
    if object.soiled == True and object.unclean > 3:
        object.is_sick == True
        # print(f"{object.name} is sick!")
    elif object.soiled == True:
        object.unclean += 1    
        print(f"{object.name} needs to be cleaned!")


def sick_check(object):                             # Checks for display message
    if object.is_sick == True:
        print(f"{object.name} is sick!")

        if object.energy - 5 > 0:       
            object.energy -= 5
        else:
            object.energy = 0

        if object.happiness - 3 > 0:       
            object.happiness -= 3
        else:
            object.happiness = 0





def days_sick_check(object):                        # Check after each day
    if object.days_sick > 3:            
        object.is_alive = False
    elif object.is_sick == True:                    # if over 3: dead, 
        object.days_sick += 1                       #   else add a day


        

def end_of_day(object):
    print("==================================")
    print(f"END OF DAY {object.age}")
    print("==================================")

    # print(f"This is {object.name}'s Stats for today")
    # print("==================================")
    # print(object)
    # print("==================================")
    object.age += 1
    time.sleep(3)
    os.system("cls")












def intro_logo():
        print("Welcome To:")
        print(" ______   ____  ___ ___   ____   ____   ___   ______   __  __ __  ____ ")
        print("|      | /    ||   |   | /    | /    | /   \ |      | /  ]|  |  ||    |")
        print("|      ||  o  || _   _ ||  o  ||   __||     ||      |/  / |  |  | |  | ")
        print("|_|  |_||     ||  \_/  ||     ||  |  ||  O  ||_|  |_/  /  |  _  | |  |")
        print("  |  |  |  _  ||   |   ||  _  ||  |_ ||     |  |  |/   \_ |  |  | |  |")
        print("  |  |  |  |  ||   |   ||  |  ||     ||     |  |  |\     ||  |  | |  |")
        print("  |__|  |__|__||___|___||__|__||___,_| \___/   |__| \____||__|__||____|")
        print("  (By Dave)")
        time.sleep(5)
        os.system("cls")




