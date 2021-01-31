#!/usr/bin/python

def Play21Game(players):
    player1 = players[0]
    player2 = players[1]
    
    print(" {0} will play first, {1} will play next ". format(player1 , player2))
    inputPlayerName= input("Who Wants to play first ???? ")
    
    for n in range(21+1):
        if n==21 and inputPlayerName == player1:
            return player1
        elif n==21 and inputPlayerName == player2:
            return player2
    
def main():
    players = ['Computer','Individual']
    winner = Play21Game(players)
    print(" Winner of the game is : {0}".format(winner))


if __name__ == "__main__":
    main()