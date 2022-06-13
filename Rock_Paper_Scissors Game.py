import random

#game is initialised
print("*******************************")
print("Welcome to Rock-Paper-Scissors")
print("*******************************")

#defining game options 
R = 'Rock'  
P = 'Paper'
S = 'Scissors'

while True:
    #player makes their move   
    userMove = input("Please make your move\n 'R' for Rock\n 'P' for Paper\n 'S' for Scissors\n").upper()            
    
    def userChoice():
        if userMove == 'R':
            return R
        elif userMove == 'P':
            return P
        elif userMove == 'S':
            return S
            
    def invalidOption():
        if userMove != R or userMove != P or userMove != S:            
            return userMove
    # computer counters player's move
    def computerMove():
        possibleOptions = [R, P, S] 
        computerMove = random.choice(possibleOptions)
        return computerMove

    userChoice = userChoice()
    invalidOption = invalidOption()
    computerMove = computerMove()

    print(f"Player ({userChoice}) : CPU ({computerMove})")

        
    #rules of the game
    if userChoice == computerMove:
        print("It's a tie. Please Try Again")        
    elif userChoice == R:
        if computerMove == S:
            print("Rock Crushes Scissors! Player Wins!")
        else:
            print("Paper Covers Rock! CPU Wins!")
    elif userChoice == P:
        if computerMove == R:
            print("Paper Covers Rock! Player Wins!")
        else:
            print("Scissors Cuts Paper! CPU Wins!")
    elif userChoice == S:
        if computerMove == P:
            print("Scissors Cuts Paper! Player Wins!")
        else:
            print("Rock Crushes Scissors! CPU Wins!")
    else:
        print(f"[{invalidOption}] is not a valid game option. Please try again.")
        continue
#player receives prompt to replay the game
    replay = input("Would you like to play another round? [Y/N]:").upper()
    if replay != 'Y':
        break

