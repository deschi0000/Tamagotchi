import time
import os
from frame_functions import *

def death_animation():
    for i in range(0, 2):
        os.system("cls")
        ghost_1()
        time.sleep(0.9)
        os.system("cls")
        ghost_2()
        time.sleep(0.9)
        os.system("cls")
        ghost_1()

def eat_animation():
    for i in range(0, 2):
        os.system("cls")
        eat_1()
        time.sleep(0.6)
        os.system("cls")
        eat_2()
        time.sleep(0.6)

def sleep_animation():
    for i in range(0, 2):
        os.system("cls")
        sleep_1()
        time.sleep(0.8)
        os.system("cls")
        sleep_2()
        time.sleep(0.8)
        os.system("cls")
        sleep_1()

def unchi_animation():
    for i in range(0, 2):
        os.system("cls")
        unchi_1()
        time.sleep(0.9)
        os.system("cls")
        unchi_2()
        time.sleep(0.9)

def happy_animation2():
    os.system("cls")
    happy_1()
    time.sleep(3)

def happy_animation():
    for i in range(0, 2):
        os.system("cls")
        happy_1()
        time.sleep(0.9)
        os.system("cls")
        happy_2()
        time.sleep(0.9)

def wake_up_animation():
    os.system("cls")
    wake_up1()
    time.sleep(1)

def unclean_animation2():
    os.system("cls")
    unclean_3()
    time.sleep(3)

def unclean_animation():
    for i in range(0, 2):
        os.system("cls")
        unclean_1()
        time.sleep(0.9)
        os.system("cls")
        unclean_2()
        time.sleep(0.9)
        os.system("cls")
        unclean_1()

def sick_animation2():
    os.system("cls")
    sick_1()
    time.sleep(3)

def sick_animation():
    for i in range(0, 2):
        os.system("cls")
        sick_2()
        time.sleep(0.7)
        os.system("cls")
        sick_3()
        time.sleep(0.7)
        os.system("cls")
        sick_2()

def cured_animation():
    for i in range(0, 3):
        os.system("cls")
        cure_1()
        time.sleep(0.5)
        os.system("cls")
        cure_2()
        time.sleep(0.5)
        os.system("cls")
        cure_1()

def play_animation():
    for i in range(0, 2):
        os.system("cls")
        play_1()
        time.sleep(0.7)
        os.system("cls")
        play_2()
        time.sleep(0.7)
        os.system("cls")
        play_1()

def clean_animation():
    for i in range(0, 2):
        os.system("cls")
        clean_1()
        time.sleep(0.7)
        os.system("cls")
        clean_2()
        time.sleep(0.7)
        os.system("cls")
        clean_1()

def sad_animation():
    os.system("cls")
    sad_1()

def birth_animation():
        os.system("cls")
        birth_1()
        time.sleep(2)
        os.system("cls")
        birth_2()
        time.sleep(2)
        os.system("cls")
        birth_3()
        time.sleep(2)
        os.system("cls")
        birth_4()
        time.sleep(3)
        os.system("cls")
        birth_5()
        time.sleep(3)
        os.system("cls")

def naming_animation():
    os.system("cls")
    naming_1()

def doing_nothing_animation():
    os.system("cls")
    doing_nothing_1()

def treasure_found_animation():
    for i in range(0, 3):
        os.system("cls")
        teasure_find_1()
        time.sleep(0.5)
        os.system("cls")
        teasure_find_2()
        time.sleep(0.5)
        os.system("cls")
        teasure_find_1()

# Debug away
# treasure_found_animation()
# birth_animation()
# cured_animation()
# play_animation()
# eat_animation()
# death_animation()
# sleep_animation()
# unchi_animation()
# happy_animation()
# sick_animation()
# sick_animation2()
# wake_up_animation()
# unclean_animation()
# clean_animation()
