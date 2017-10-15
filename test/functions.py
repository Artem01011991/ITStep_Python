# functions' file
from random import shuffle
from random import randint
from os import system
from time import sleep

def init_player():

    while True:
        try:
            player_account = int(input('Enter your amount money:'))
            if  player_account == 0:
                print("(Enter number bigger than null)")
                continue
            system('cls')
            return player_account
        except ValueError:
            print(('Number, please.'))


def deck_shuffle():
    deck = ['J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10] * 4 * 4
    shuffle(deck)
    return deck

#total points sum function
def sum_card(temp_hand):
    hand = temp_hand.copy()
    color_card = {'A':(11, 1),'J': 10, 'Q': 10, 'K': 10}
    count_A = hand.count('A')

    for i in hand:
        for j in color_card:
            if  i == j:
                if i == 'A':
                    hand[hand.index(i)] = color_card.get(j)[0]
                    break
                hand[hand.index(i)] = color_card.get(j)
                break

    result = sum(hand)

    if  result > 21 and count_A != 0:
        return result - (count_A * 11) + count_A

    return result

#main function runs the game
def game():
    player = init_player()
    deck = deck_shuffle()

#bet block
    bet = None
    while True:
        while True:
            try:
                print("Your account equal: ", player)
                bet = int(input('\nEnter your bet:'))
                if  bet > player or bet == 0 or bet < 0:
                    print("(Incorrect bet. Your account: ",player,")")
                    continue
                break
            except ValueError:
                print('(Number, please.)')
        system('cls')

        hand = [deck.pop(randint(0, len(deck) - 1)) for _ in range(2)]
        Dealer_hand = [deck.pop(randint(0, len(deck) - 1))]

#Start a game with 21 BLACK
        if  sum_card(hand) == 21 and Dealer_hand[0] not in {'A','J','Q','K',10}:
            print("BLACK JACK")
            player += (bet * 3)
            print("Your account equal: ", player)
            sleep(3)
            system('cls')
            quit_game = input("If you want to leave type in 'exit':")
            system('cls')
            if quit_game.upper() == 'EXIT':
                break
            continue
        elif sum_card(hand) == 21 and Dealer_hand[0] in {'A','J','Q','K',10}:
            print("Your hand: ", ' '.join([str(i) for i in hand]), end='\t\t\t')
            print("Dealer hand: ", str(Dealer_hand[0]))
            print("\n\nYou have BLACK JACK. But Dealer maybe as well.\n"
                  "Would you like take a gain 1 to 1 (Press 1)\n"
                  "If Dealer doesn't have you would win 3 to 2(Press any key)")
            if(input() == '1'):
                player += bet
                print("Your account equal: ", player)
                sleep(2)
                system('cls')
                continue
            else:
                Dealer_hand += [deck.pop(randint(0, len(deck) - 1))]
                if (Dealer_hand[0] in {'J','Q','K',10} and Dealer_hand[1] == 'A') or \
                    (Dealer_hand[0] in 'A' and Dealer_hand[1] == {'J','Q','K',10}):
                    system('cls')
                    print("Your hand: ", ' '.join([str(i) for i in hand]), end='\t\t\t')
                    print("Dealer hand: ", ' '.join([str(i) for i in Dealer_hand]))
                    print("Dealer has BLACK JACK.")
                    sleep(3)
                    system('cls')
                    continue
#END BLACK JACK BLOCK

        print("Your hand: ",' '.join([str(i) for i in hand]), end ='\t\t\t')
        print("Dealer hand: ", str(Dealer_hand[0]))

#Taking cards
        choice = {1:'more', 2:'enough'}

        print("\n\n\n1. take a card.\n"
              "2. complete taking cards")
        while True:
            try:
                if  choice.get(int(input())) == 'more':
                    hand += [deck.pop(randint(0, len(deck) - 1))]
                    if sum_card(hand) > 21:
                        system('cls')
                        print("Your hand: ", ' '.join([str(i) for i in hand]))
                        print("Bust!!!")
                        player -= bet
                        print("\n\nYour account equal: ", player)
                        break
                else:
                    break
                system('cls')
                print("Your hand: ", ' '.join([str(i) for i in hand]), end ='\t\t\t')
                print("Dealer hand: ", str(Dealer_hand[0]))
            except ValueError:
                system('cls')
                print("Your hand: ", ' '.join([str(i) for i in hand]), end='\t\t\t')
                print("Dealer hand: ", str(Dealer_hand[0]))
                print("\n\n\n1. take a card.\n"
                      "2. complete taking cards")
                print("(Only 1 or 2)")
#END BLOCK TAKING CARDS

#Dealer taking cards
        sleep(2)
        system('cls')
        if sum_card(hand) <= 21:
            while sum_card(Dealer_hand) < 17:
                Dealer_hand += [deck.pop(randint(0, len(deck) - 1))]
                print("Your hand: ", ' '.join([str(i) for i in hand]), end ='\t\t\t')
                print("Dealer hand: ", ' '.join([str(i) for i in Dealer_hand]))
                sleep(2)
                system('cls')

#Winner checking
            if sum_card(Dealer_hand) > 21:
                print("Your hand: ", ' '.join([str(i) for i in hand]), end='\t\t\t')
                print("Dealer hand: ", ' '.join([str(i) for i in Dealer_hand]))
                print("\nYou won!!!")
                player += bet
            elif sum_card(Dealer_hand) == sum_card(hand):
                print("Your hand: ", ' '.join([str(i) for i in hand]), end='\t\t\t')
                print("Dealer hand: ", ' '.join([str(i) for i in Dealer_hand]))
                print("\nDraw!!!")
            elif sum_card(Dealer_hand) > sum_card(hand):
                print("Your hand: ", ' '.join([str(i) for i in hand]), end='\t\t\t')
                print("Dealer hand: ", ' '.join([str(i) for i in Dealer_hand]))
                print("\nDealer won!!!")
                player -= bet
            elif sum_card(Dealer_hand) < sum_card(hand):
                print("Your hand: ", ' '.join([str(i) for i in hand]), end='\t\t\t')
                print("Dealer hand: ", ' '.join([str(i) for i in Dealer_hand]))
                print("\nYou won!!!")
                player += bet
            print("\n\nYour account equal: ",player)

#exit
        if player <= 0:
            print("You have wasted all your money!!!")
            sleep(3)
            break

        quit_game = input("If you want to leave type in 'exit':")
        system('cls')
        if quit_game.upper() == 'EXIT':
            break