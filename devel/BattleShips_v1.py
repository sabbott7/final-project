#Battleships
#Final Project
#by Sean Abbott 
#
from random import randint

#initialize the board
board = []

for x in range(5):
    board.append(["O"] * 5)

def printBoard(board):
    for row in board:
        print(" ".join(row))

#starting the game and printing the board
print ("Let's play Battleship! Action Stations!")
printBoard(board)

#place the ship using random co-ordinates
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#get co-ordinates from user
for strike in range(4):
    guess_row = int(input('Guess Row(0-4):'))
    guess_col = int(input('Guess Col(0-4):'))

    # if the user's right, the game ends
    if guess_row == ship_row and guess_col == ship_col:
        print ('BRAVO! You sunk my battleship! You GOT ME !!')
        print ('My Ship Row = '+str(ship_row))
        print ('My Ship Col = '+str(ship_col))
        break
    else:
        #validate the ship can be placed at given coordinates
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Ouch, that's not even in the ocean.")
        
        #warning if the guess was already made
        elif(board[guess_row][guess_col] == "X"):
            print ('You guessed that one already.')
        
        #if the guess is wrong, mark the point with an X and start again
        else:
            print ('You missed my battleship!')
            board[guess_row][guess_col] = "X"
        
        # Print strike and board again here
        print ('Strike ' + str(strike+1) + ' out of 4.')
        printBoard(board)

#if the user has made 4 tries, it's game over
if strike >= 3:
    print ('Game Over. You lost. Hard luck buddy!!')
    print ('My Ship Row = '+str(ship_row))
    print ('My Ship Col = '+str(ship_col))
   
#end
