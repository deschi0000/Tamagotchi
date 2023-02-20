from classes import Tamagotchi
from random import choice, randrange
from tamagotchi_animation import *

import os
import time

MAX_AGE = 10
AWAKE_COMMANDS_RESTED = ["f", "p", "u", "n"]
AWAKE_COMMANDS = ["f","r", "p", "u", "n" ]
AWAKE_COMMANDS_SICK = ["r", "p", "m", "n" ]
AWAKE_COMMANDS_SOILED = ["f","r", "p", "c", "n" ]
ASLEEP_COMMANDS = ["w", "r"]
OBJECTS_TO_FIND = [
    "some string", 
    "ancient buried treasure", 
    "your lost wallet", 
    "a bottlecap",
    "a steam giftcard",
    "a David Hasselhof signed VHS of Knight Rider"
    ]


def create_tamagotchi():
    name = ""
    print("Congratulations on your new pet!")  
    print("What would you like to name it? ", end="") 
    while len(name) == 0:
        name = input("")
        if len(name.strip()) == 0:
            print("Please enter a valid name: ", end="")          
    return Tamagotchi(name)
    

def time_of_day_message(num):
    if num == 0:
        return "Good Morning!"
    elif num == 1:
        return "Lunchtime!"
    else:
        return "Eveningtime"


def press_enter():
    userinput = "999"
    userinput = input("Press Enter to Continue")
    if userinput == "":
        os.system("cls")


def quit():
    userinput = "999"
    print("Press [q] to quit")
    while userinput.lower() != "q":
        userinput = input("")
    os.system("cls")


def rest_check(object, energy):
    if object.is_resting == True and energy == 100:                # Fully rested, wake up
        return object.wake_up()
    elif object.is_resting == False and energy == 100:             # No need to sleep
        return f"\n{object.name} is fully rested!"
    elif object.is_resting == True and energy < 100:               # Keep resting
        sleep_animation()
        return object.rest()
    elif object.is_resting == True and object.prompt_wakeup == True:
        object.prompt_wakeup = False
        return object.wake_up()


def energy_check(object):
    if object.energy < 15:
        warning("extreme_energy", object)
    elif object.energy < 30:
        warning("energy", object)

def depleter(object):
    if object.energy - 7 > 0:
        object.energy -= 7
    else:
        object.energy = 0
    if object.happiness - 2 > 0:
        object.happiness -=2
    else: 
        object.happiness = 0
    if object.health - 3 > 0:
        object.health -=3
    else:
        object.health = 0
    if object.hunger + 4 < 100:
        object.hunger += 4
    else:
        object.hunger = 100


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
    if object.happiness < 20 and object.neglectometer > 7:
        sad_animation()
        print(f"{object.name} is feeling sad...")
        press_enter()
    if object.happiness > 65 and object.soiled is False and object.is_resting is False and object.is_sick is False:
        object.number_of_times_happy += 1
        happy_animation()
        print(f"{object.name} is feeling happy!")
        press_enter()
    if object.neglectometer > 15:
        object.is_sick = True
        sick_animation()
        press_enter()
    elif object.neglectometer > 7 and object.is_playing == False:        #not is playing prevents from showing if the user just played with it
        sad_animation()
        print(f"{object.name} is feeling a little neglected...")
        press_enter()
    

def death_check(object):
    if object.energy < 0 or object.health < 0:
        object.is_alive = False 


def reset(object):
    # Function that will reset stats that change naturally after one turn
    object.playing = False


def death_type_check(object):
    death_animation()
    if object.age < MAX_AGE:
        print(f"{object.name} didn't make it...")
    else:
        print(f"{object.name} died peacefully of old age")


def final_stats(object):
    print(f"GG. Some info on {object.name}'s final stats")
    print("==================================")
    print(f"{object.name} lived to {object.age} years old")
    if object.age < MAX_AGE:
        print("Make sure to take better care of your pet next time!")
    if object.number_of_times_happy > 5:
        print(f"{object.name} was quite happy during his life. Great Job!")
    if object.number_of_times_sick > 2:
        print("Remember to clean your pet so it doesn't get sick as often!")
    print("Thank you for playing!")
    print("==================================\n")
    quit()


def holding_check(object):
    if object.soiled == True:
        object.is_holding == 0
    elif object.soiled == False and object.is_holding > 5 and object.is_resting is False:
        object.unchi(True)
    else:
        object.is_holding += 1


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
    if object.is_resting is False and object.energy == 100:                         # Awake, fully rested, healthy
        while c.lower() not in AWAKE_COMMANDS_RESTED:
            c = input("Feed [f]  | Play [p] | Poo(u) | Do Nothing [n]\n")        
    elif object.is_resting is False and object.is_sick is True:                     # Awake, sick
        while c.lower() not in AWAKE_COMMANDS_SICK:
            c = input("Rest [r]  | Play [p] | Give Medicine [m] | Do Nothing [n]\n")    
    elif object.is_resting is False and object.soiled is True:                      # Awake, soiled
        while c.lower() not in AWAKE_COMMANDS_SOILED:
            c = input("Feed [f]  |  Rest [r]  | Play [p] | Clean [c] | Do Nothing [n]\n")
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
    if input == "r":                         
        if object.energy == 100:
            print(f"{object.name} is fully rested!")
            press_enter()
        else:
            object.is_resting = True
            rest_check(object, object.energy)         
    if input == "w":                                      
        object.wake_up()

    if input == "p":                           
        object.play()

    if input == "u":                           
        object.unchi()

    if input == "c":
        object.clean()

    if input == "m":
        object.cure()

    if input == "n":             
        rest_check(object, object.energy)
        if object.is_resting is False:
            object.neglect()

        
def clean_check(object):
    if object.soiled == True and object.unclean > 3:
        object.is_sick = True
        object.number_of_times_sick += 1
        # sick_animation()                            #added    not needed b/c sick check?
        # print(f"{object.name} is sick!")            #added
        if object.is_resting is False:
            unclean_animation() 
        print(f"{object.name} needs to be cleaned!")
        press_enter()

    elif object.soiled == True:
        object.unclean += 1
        object.happiness -= 5
        if object.is_resting == False:    
            unclean_animation()
        print(f"{object.name} needs to be cleaned!")
        press_enter()


def sick_check(object):                             # Checks for display message
    if object.is_sick == True:
        sick_animation()
        print(f"{object.name} is sick!")
        press_enter()                               # So the next check doesn't clear the cmd

        if object.energy - 5 > 0:       
            object.energy -= 5
        else:
            object.energy = 0
        if object.happiness - 3 > 0:       
            object.happiness -= 3
        else:
            object.happiness = 0
    

def sleep_roll(object):
    # Random sleeping
    if randrange(25) == 7 and object.is_resting is not True:
        object.rest(True)


def treasure_hunt_roll(object):
    if randrange(100) == 42 and object.is_resting is not True:
        if object.happiness + 35 < 100:
            object.happiness += 35
        else:
            object.happiness = 100
        treasure_found_animation()
        print(f"{object.name} found {choice(OBJECTS_TO_FIND)}. It's ecstatic!")
        press_enter()


def days_sick_check(object):                        # Check after each day
    if object.days_sick > 1:            
        object.is_alive = False
    elif object.is_sick is True:                    # if over 3: dead, 
        object.days_sick += 1                       #   else add a day

       
def end_of_day(object):
    print("==================================")
    print(f"END OF DAY {object.age}")
    print("==================================")
    if object.energy + 15 < 100:
        object.energy += 15
    else:
        object.energy = 100
    object.age += 1
    press_enter()   


def intro():
    intro_logo()
    birth_animation()
    naming_animation()
    tamagotchi1 = create_tamagotchi()
    # tamagotchi1 = Tamagotchi("DK")
    os.system("cls")
    naming_animation()
    print(f"Your pet's new name is {tamagotchi1.name}")
    press_enter()
    return tamagotchi1


def intro_logo():
    os.system("cls")
    print("Welcome To:")
    print(" ______   ____  ___ ___   ____   ____   ___   ______   __  __ __  ___ ___ ")
    print("|      | /    ||   |   | /    | /    | /   \ |      | /  ]|  |  ||   |   |")
    print("|      ||  o  || _   _ ||  o  ||   __||     ||      |/  / |  |  ||   |   |")
    print("|_|  |_||     ||  \_/  ||     ||  |  ||  O  ||_|  |_/  /  |  _  ||   |   |")
    print("  |  |  |  _  ||   |   ||  _  ||  |_ ||     |  |  |/   \_ |  |  ||  _|_  |")
    print("  |  |  |  |  ||   |   ||  |  ||     ||     |  |  |\     ||  |  ||       |")
    print("  |__|  |__|__||___|___||__|__||___,_| \___/   |__| \____||__|__||_______|")
    print("  (By Dave)")
    time.sleep(3)
    os.system("cls")




