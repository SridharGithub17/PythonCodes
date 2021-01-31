#!/usr/bin/python
import random

def GuessWord(words, name ):
    print("{0} , you have 20 attempts to prepare the word from the given list".format(name))
    NewStr = ""
    n=0
    string = random.choice(words)
    print("Random choice string from the list is : ", string)

    while n < 20:
        c= input ("Enter a charecter {0} attempt :  ".format(n+1))
        NewStr = NewStr + str(c)
        print(" New String is  :", NewStr)
        
        for i in range(len(words)):
            if NewStr == words[i]:
                print("Congradulations {0}, you matched the random word {1} in the list ".format(name, string))
                exit()
            else:
                continue
        n+= 1
        print( " Please try again ................")

def main():
    name = input(" Enter your name : " )
    print(" Good Luck  : ", name )
    words = ['rainbow', 'computer', 'science', 'programming', 
         'python', 'mathematics', 'player', 'condition', 
         'reverse', 'water', 'board', 'geeks']
    print(words)
    GuessWord(words, name )

if __name__ == "__main__":
    main()