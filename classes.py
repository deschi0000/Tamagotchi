import time
from random import choice
from tamagotchi_animation import *

PLAY = [
    "playing volleyball", 
    "playing in the grass", 
    "listening to Metallica", 
    "playing Gamecube", 
    "playing on a slide",
    "going for a swim", 
    "playing hide-and-seek", 
    "catching a frisbee", 
    "wakeboarding",
    "playing in a cardboard box"
    ]

FOOD = [
    "croissant", 
    "cake", 
    "manju", 
    "pasta", 
    "lobster claw", 
    "risotto", 
    "gua bao", 
    "a banana", 
    "a sandwich",  
    "potato chips", 
    "a pretzel"
    ]


class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.asleep = False
        self.hunger = 10
        self.energy = 90                    # Start level: 75
        self.health = 100
        self.happiness = 45
        self.neglectometer = 0
        self.is_resting = False
        self.is_alive = True
        self.is_playing = False

        # Do checks for just pooed, and check against the counter
        self.soiled = False
        self.is_holding = 0

        self.unclean = 0
        self.is_sick = False
        self.days_sick = 0

        self.number_of_times_sick = 0
        self.number_of_times_happy = 0


    def put_to_bed(self):

        if self.energy + 35 < 100:
            self.energy += 35
        else:
            self.energy = 100


    def __str__(self):
        # return f"\nName: {self.name}\nAge: {self.age}\nEnergy: {self.energy}\nHunger: {self.hunger}\nHealth: {self.health}\nHappiness: {self.happiness}\nUnclean: {self.unclean}\nDays Sick: {self.days_sick}\nNumber of times sick: {self.number_of_times_sick}\nNeglectometer: {self.neglectometer}\nIs alive: {self.is_alive}\n"
        return f"\nName: {self.name}\nAge: {self.age}\nEnergy: {self.energy}\nHunger: {self.hunger}\nHealth: {self.health}\nHappiness: {self.happiness}\n"


    def intro(self):
        return f"\n{self.name}. It is {self.age} years old.\n"



    def neglect(self):
        self.happiness -= 3
        self.neglectometer += 3
        # if self.soiled is False and self.is_sick is False:
        doing_nothing_animation()
        
        print("You did nothing.")
        press_enter()

    def lose_health(self):
        if self.health -5 > 0:
            self.health -= 5
        else:
            self.health = 0


    def rest(self, own_volition=False):

        self.is_resting = True          # Set the resting state to true

        if self.energy + 5 < 100:       # Hunger cannot go below 0 and rest/energy cannot go above 100
            self.energy += 15
        else:
            self.energy = 100

        if self.hunger + 2 < 100:       # Get hungrier, longer you sleep
            self.hunger += 2
        else:
            self.hunger = 100

        if self.happiness + 2 < 100:
            self.happiness += 2
        else:
            self.happiness = 100

        if self.health + 7 < 100:
            self.health += 7
        else:
            self.health = 100        


        
        if self.energy == 100:            
            self.wake_up()
            press_enter()
            # wake_up_animation()
        elif own_volition is True:
            sleep_animation()
            print(f"{self.name} randomly fell asleep!")
            press_enter()
        elif own_volition is False:
            print(f"{self.name} is resting.")
            press_enter()
        

    def play(self):
        play_animation()
        if self.energy - 20 > 0:       
            self.energy -= 20
        else:
            self.energy = 0          # Tamagotchi dies?? 

        if self.hunger + 3 < 100:       
            self.hunger += 3
        else:
            self.hunger = 100

        if self.happiness + 5 < 100:
            self.happiness += 5
        else:
            self.happiness = 100

        if self.neglectometer - 1 > 0:
            self.neglectometer -= 1
        else:
            self.neglectometer = 0

        self.is_playing = True
        print(f"{self.name} is having fun {choice(PLAY)}!")
        press_enter()


    def feed(self):
        eat_animation()
        if self.hunger - 15 > 0:
            self.hunger -= 15
        else:
            self.hunger = 0

        if self.energy < 100:
            self.energy += 5
        else:
            self.energy = 100

        if self.health < 100:
            self.health += 7
        else:
            self.health = 100

        if self.happiness < 100:
            self.happiness += 5
        else:
            self.happiness = 100

        if self.neglectometer - 1 > 0:
            self.neglectometer -= 1
        else:
            self.neglectometer = 0

        print(f"{self.name} enjoyed eating {choice(FOOD)}")
        press_enter()


    def wake_up(self):
        self.is_resting = False
        wake_up_animation()
        print(f"{self.name} Woke up! Energy: {self.energy}")
        press_enter()

    def cure(self):
        self.unclean = 0                      #cleaning the object here, or else will keep getting sick despite medicine.       
        self.is_sick = False
        self.neglectometer -=2
        if self.happiness + 2 < 100:
            self.happiness += 2
        else:
            self.happiness = 100
        cured_animation()
        print(f"You gave {self.name} medicine.")        
        print(f"{self.name} is feeling better!") 
        press_enter()

    def unchi(self, could_not_hold = False):
        
        # if self.just_pooed == True and self.unclean > 3:
        #     self.is_sick == True
        #     print(f"{self.name} got sick!")

        self.is_holding = 0
        unchi_animation()
        if self.hunger <100:
            self.hunger +=10
        else:
            self.hunger = 100

        if self.energy - 5 > 0:       
            self.energy -= 5
        else:
            self.energy = 0    

        if self.happiness + 2 < 100:
            self.happiness += 2
        else:
            self.happiness = 100

        self.unclean += 1
        self.soiled = True
        if could_not_hold is True:
            print(f"{self.name} couldn't hold it! It feels relieved now")
            press_enter()        
        else:
            print(f"{self.name} feels relieved!")
            press_enter()

    def clean(self):
        clean_animation()
        self.unclean = 0
        self.soiled = False
        print(f"{self.name} is all clean now")
        press_enter()


def press_enter():
    # enter_pressed = False
    userinput = "999"
    userinput = input("Press Enter to Continue")
    if userinput == "":
        os.system("cls")
        # enter_pressed = True