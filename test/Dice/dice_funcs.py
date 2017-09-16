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
    print(dice1, dice2, sep = ' ')
    sleep(4)
    system('cls')

    return dice1 + dice2


def throw_dice_comp():
    dice1 = 0
    dice2 = 0

    for i in range(1, 40):
        print(randint(1, 6), randint(1, 6), sep=' ')
        sleep(0.2)
        system('cls')

    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    print(dice1, dice2, sep=' ')
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

def game_setting_single():
    compname = 'Comp'
    playername = input("Enter your name:")
    system('cls')

    print("Enter amount money for", playername)
    playeraccount = -1
    while playeraccount <= 0:
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

    return playername, playeraccount,  compname, compaccount

def game_run_singl(from_game_set):
    playername, playeraccount, compname, compaccount = from_game_set

# player makes a bet
    answer = ''

    while answer.upper() != 'NO' and playeraccount != 0 and compaccount != 0:
        playerbet = -1
        while playerbet <= 0 or playerbet > playeraccount:
            print("You have", playeraccount,"money and Comp has", compaccount)
            try:
                playerbet = int(input("Type in your bet:"))
            except ValueError:
                print("(Only integer value)")
        playeraccount -= playerbet
        system('cls')
# comp makes a bet
        compbet = randint(1, compaccount)
        compaccount -= compbet
        print(compname, "is betting", compbet)
# Check for whether equal bets
        if playerbet < compbet:
            answer = ''

            while answer.upper() != 'YES' and answer.upper() != 'NO':
                answer = input('Would you like to equal the bets? (Yes/No)')
            if answer.upper() == 'YES':
                if playeraccount + playerbet >= compbet:
                    playeraccount += playerbet
                    playerbet = compbet
                    playeraccount -= playerbet
                else:
                    print("You have no money")
                    sleep(2)
                    compaccount += compbet
                    compbet = playerbet
                    compaccount -= compbet
                    print(compname,"is betting", compbet)
            else:
                print("Sorry, you lose")
                sleep(2)
                exit(0)
        if playerbet > compbet:
            if compbet + compaccount >= playerbet:
                compaccount += compbet
                compbet = playerbet
                compaccount -= compbet
                print(compname,"is betting", compbet)
            else:
                print("Comp have'nt enough money")
                playeraccount += playerbet
                playerbet = compbet
                playeraccount -= playerbet
                print("Your bet is", playerbet,"in this case")
        system("cls")
#Throw dice
        playerscore = 0
        compscore = 0
        while playerscore < 21 and compscore < 21:
            print(playername,"score =", playerscore,"\t", compname,"score =", compscore)
            playerscore += throw_dice()
            if playerscore > 21 or (playerscore < 21 and compscore == 21):
                print("You lost your money!")
                compaccount += compbet + playerbet
                break
            print("Comp's turn")
            sleep(2)
            compscore += throw_dice_comp()
            if compscore > 21 or (compscore < 21 and playerscore == 21):
                print("Poor compy!")
                playeraccount += compbet + playerbet

        answer = input("Continue play? (anythig else equal = 'yes' / no)")
    print("Bye")

def game_setting_mult():
    player1 = input("Enter your name(player1):")
    player2 = input("Enter your name(player2):")
    system('cls')

    print("Enter amount money for", player1)
    playeraccount = -1
    while playeraccount <= 0:
        try:
            playeraccount = int(input())
            if playeraccount <= 0:
                print("(Enter a value > 0)")
            continue
        except ValueError:
            print("(Only integer value)")
    system('cls')

    print("Enter amount money for", player2)
    player2account = -1
    while player2account <= 0:
        try:
            player2account = int(input())
            if player2account <= 0:
                print("(Enter a value > 0)")
            continue
        except ValueError:
            print("(Only integer value)")
    system('cls')

    return player1, playeraccount, player2, player2account

def game_run_mult(from_game_set):
    playername, playeraccount, player2, player2account = from_game_set

# player1 makes a bet
    answer = ''

    while answer.upper() != 'NO' and playeraccount != 0 and player2account != 0:
        playerbet = -1
        while playerbet <= 0 or playerbet > playeraccount:
            print(playername,"has", playeraccount,"money and",player2  ,"has", player2account)
            try:
                print(playername, "Type in your bet")
                playerbet = int(input())
            except ValueError:
                print("(Only integer value)")
        playeraccount -= playerbet
        system('cls')
# player2 makes a bet
        player2bet = -1
        while player2bet <= 0 or player2bet > player2account:
            print(player2,"has", player2account,"money and",playername  ,"has", playeraccount)
            try:
                print(player2,"Type in your bet")
                player2bet = int(input())
            except ValueError:
                print("(Only integer value)")
        playeraccount -= playerbet
        system('cls')
# Check for whether equal bets
        if playerbet < player2bet:
            answer = ''

            while answer.upper() != 'YES' and answer.upper() != 'NO':
                print(playername,"Would you like to equal the bets? (Yes/No)")
                answer = input()
            if answer.upper() == 'YES':
                if playeraccount + playerbet >= player2bet:
                    playeraccount += playerbet
                    playerbet = player2bet
                    playeraccount -= playerbet
                else:
                    print("You have no money")
                    sleep(2)
                    player2account += player2bet
                    player2bet = playerbet
                    player2account -= player2bet
                    print(player2,"is betting", player2bet)
            else:
                print("Sorry, you lose")
                sleep(2)
                exit(0)

            if playerbet > player2bet:
                while answer.upper() != 'YES' and answer.upper() != 'NO':
                    print(player2,"Would you like to equal the bets? (Yes/No)")
                    answer = input()
                    if answer.upper() == 'YES':
                        if player2bet + player2account >= playerbet:
                            player2account += player2bet
                            player2bet = playerbet
                            player2account -= player2bet
                            print(player2,"is betting", player2bet)
                        else:
                            print(player2,"has'nt enough money")
                            playeraccount += playerbet
                            playerbet = player2bet
                            playeraccount -= playerbet
                            print(playername," bet is", playerbet,"in this case")
                    else:
                        print("Sorry, you lose")
                        sleep(2)
                        exit(0)
                system("cls")
#Throw dice
        playerscore = 0
        player2score = 0
        while playerscore < 21 and player2score < 21:
            print(playername,",your turn")
            print(playername,"score =", playerscore,"\t", player2,"score =", player2score)
            playerscore += throw_dice()
            if playerscore > 21 or (playerscore < 21 and player2score == 21):
                print(playername,"lost money!")
                player2account += player2bet + playerbet
                break
            print(player2,"turn")
            sleep(2)
            player2score += throw_dice()
            if player2score > 21 or (player2score < 21 and playerscore == 21):
                print(player2,"lost money!")
                playeraccount += player2bet + playerbet

        answer = input("Continue play? (anythig else equal = 'yes' / no)")
    print("Bye")

def game_process(result):
    if result == 1:
        game_run_singl(game_setting_single())
    else:
        game_run_mult(game_setting_mult())
