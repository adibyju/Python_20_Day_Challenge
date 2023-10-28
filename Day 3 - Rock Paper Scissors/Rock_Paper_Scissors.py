import random

# function to evaluate the game
def rock_paper_scissors_game():
    userChoice = input("Input 'r' for rock, 'p' for paper, and 's' for scissors (or 'e' for exiting the game): ") # taking user input

    if userChoice not in ['r', 'p', 's', 'e']: # input validation
        print("Invalid entry, try again!")
        return 0, 0

    computerChoice = random.choice(['r', 'p', 's']) # generating computer choice through random library

    if userChoice == 'e': # quit app if 'e' is entered
        quit()

    # return appropriate scores by checcking  user and computer choices
    if (userChoice == 'r' and computerChoice == 's') or (userChoice == 'p' and computerChoice == 'r') or (userChoice == 's' and computerChoice == 'p'):
        print("You win!")
        return 1,0
    elif userChoice == computerChoice:
        print("It's a tie")
        return 0,0
    else:
        print("You lose :(")
        return 0,1


userScore, computerScore = 0, 0 # keep track of user and computer scores
while(1):    
    temp1, temp2 = rock_paper_scissors_game()

    # Update user and computer scores
    userScore += temp1
    computerScore += temp2
    print(f'Current user score: {userScore}, Current computer score: {computerScore}') 