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
    choice = 0
    
    print("Choose the mode of the game:")
    print("1. Singl Player.")
    print("2. Multy Player.")

    while 1 > choice or choice > 2 :
        try:
            choice = int(input())
            system('cls')
            if 1 > choice or choice > 2:
                print("(Please, type in 1 or 2)")
            continue
        except ValueError:
            system('cls')
            print("(Please, type in 1 or 2)")

    system('cls')
    return choice

def game_process(result):
    compname = 'Comp'

    if result == 1:
        playername = input("Enter your name:")

        print("Enter amount money for", playername)
        playeraccount = -1
        while playeraccount <= 0 :
            try:
                playeraccount = int(input())
                if playeraccount <= 0:
                    print("(Enter a value > 0)")
                continue
            except ValueError:
                print("(Only integer value)")
        system('cls')

        print("Enter amount money for", compname)
        compaccount = -1
        while compaccount <= 0:
            try:
                compaccount = int(input())
                if compaccount <= 0:
                    print("(Enter a value > 0)")
                continue
            except ValueError:
                print("(Only integer value)")
        system('cls')
#player makes a bet
        playerbet = -1
        while playerbet <= 0:
            try:
                playerbet = int(input("Type in your bet:"))
            except ValueError:
                print("(Only integer value)")
        playeraccount -= playerbet
        system('cls')
#comp makes a bet
        compbet = randint(1, compaccount)
        compaccount -= compbet
        print(compname,"is betting", compbet)