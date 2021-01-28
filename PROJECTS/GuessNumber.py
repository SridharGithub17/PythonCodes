#/usr/bin/python3
#Number guessing game

import sys
import random

def PlayGame(num):
    TypeOfOperation = input( "Do you want to attempt system generated attempts or custom, Insert 'S' OR 'C' : ")
    if TypeOfOperation.upper() == 'C':
        N = int(input("Enter number of Attempts : "))
    else:
        N = random.randint(0,10)
    print("## You will have {0} attempts to guess the number between the range selected ## ".format(N))
    i= 1
    while i <= N:
        CNum = int(input("Enter the number for {0} attempt ".format(i)))
        if CNum == int(num) :
            print("Congradulations you did it in {0} attempts ".format(i))
            print("Press Enter to exit the program")
            sys.exit(0)
        else:
            i+= 1
    print(" All the attempts failed ..Try again ")
        
def main():
    print(" ########## Number Guessing Game ################")

    low = int( input(" Enter the lowest value in the range  : "))
    high= int( input(" Enter the highest value in the range : "))
    digit = random.randint(low, high)

    print("Random Number Generated :", digit)    
    PlayGame(digit)



if __name__ == "__main__":
    main()
