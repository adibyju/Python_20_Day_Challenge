from Words import words
import random

# Function to evaluate the game
def hangman_game():
    noLives = 7 # number of lives at the start of the game

    # Choose a word
    word = random.choice(words)
    while ' ' in word or '_' in word:
        word = random.choice(words)
    
    currGuess=['_']*len(word) # current guess of the word by user
    guessedCharList = [] # list of already guessed characters
    validChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Run the while loop until the word is guessed correctly or the user runs out of life
    while "".join(currGuess)!=word:     
        print("\nThe word to be guessed is:", " ".join(currGuess))
        print("Characters that have been guessed till now:", guessedCharList)
        print("Current number of lives:", noLives)

        guess = input("Enter character guess: ") # record user guess
        while guess not in validChar:
            guess = input("Enter valid character: ")
            
        guessedCharList.append(guess)        

        # Reduce the number of lives by 1 if the guess is not present in the word
        if guess not in word:
            noLives-=1
        if noLives==0: 
            print("\nGame over! You have run out of lives :(")
            print("The word to be guessed was:", word)
            return

        # Replace letters of currGuess with guess
        for i in range(0, len(word)):
            if word[i]==guess:
                currGuess[i]=guess
        
    print("You have guessed the word correctly!")
    print("The word was:", word)
    return 
    

hangman_game()
