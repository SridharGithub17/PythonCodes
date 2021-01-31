#!/usr/bin/python
import random

def PlayGame(players):
    n= int(input("Enter number of times to play the game : "))
    player1 = players[0]
    player2 = players[1]
    for i in range(n):
        PL1 = int(input("Who wants to play first ?????\n"
                  "1: COMPUTER\n" 
                  "2: INDIVIDUAL\n"))
        NUM = str(random.randint(0, 999999999))
        print("Random Number to guess is : ",NUM)
        attempts = input( "Enter number of attempts to guess the number : ")
        for j in range(int(attempts)):
            GuessedNumber = Guess()
            if int(GuessedNumber) == int(NUM):
                print( "Great you've become a Mastermind! ")
                print( "It took you only {0} tries!".format(j+1))
                if PL1 == 1:
                    print("Winner of master mind game is  : {0}".format(player2))                    
                else:
                    print("Winner of master mind game is  : {0}".format(player1))
            else:
                count, countN = 0,0
                for g in range(len(str(GuessedNumber))):
                    for r in range(len(str(NUM))):
                        # print(GuessedNumber[g]  ,  NUM[r], count)
                        if (( GuessedNumber[g] == NUM[r]) and (countN == 0 )) :
                            count+= 1
                            countN+= 1
                        else:
                            continue
                    countN =0
                print( "Not quite the number ! But you did get {0} digit(s) correct! ".format(count))
    input("Press Enter to exit the MindGame .................")


def Guess():
    num= input( " Guess the number : ")
    return str(num)

def main():
    print("************* MASTER MIND GAME ****************")
    players = ["Computer","Individual"]
    PlayGame(players)
    print("************* END OF MASTER MIND GAME*************")


if __name__ == "__main__":
    main()