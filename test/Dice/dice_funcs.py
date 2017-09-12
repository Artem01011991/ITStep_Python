#functions' file
from random import randint
from os import system
from time import sleep

def throw_dice ():
    dice1 = 0
    dice2 = 0
    
    input("Please 'Enter' for throw dice")

    for i in range(1, 40):
        print(randint(1, 6),randint(1, 6),sep = ' ')
        sleep(0.2)
        system('cls')

    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    print(dice1,\
          dice2, sep = ' ')
    sleep(4)
    system('cls')

    return dice1 + dice2

def game_begin ():
    chice = 0
    
    print("Choose the mode of the game:")
    print("1. Singl Player.")
    print("2. Multy Player.")

    choice = int(input())
    system('cls')
    while 2 > choice < 1:
        try:
            print("Choose the mode of the game:")
            choice = int(input())
            system('cls')
        except ValueError:
            print("Choose the mode of the game:")
            choice = int(input())
            system('cls')
            
    return choice

def game_process(result = 1):
    compname = 'comp'
    #ОСТАНОВИЛСЯ ТУТ!!!
    if result == 1:
        playername = input("Enter your name:")
        print("Enter amount money for ", playername)
        playeraccount = int(input())
        compaccount = int(input("Enter money for "))

game_process()
