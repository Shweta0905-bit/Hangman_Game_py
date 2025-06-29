import random

def hangman():
    # Predefined list of words
    words = ["python", "development", "hangman", "programming", "challenge"]
    # Randomly select a word from the list
    word_to_guess = random.choice(words)
    letters_guessed = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    word_display = "_" * len(word_to_guess)

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")
    print(" ".join(word_display))

    while incorrect_guesses < max_incorrect_guesses and "_" in word_display:
        guess = input("Guess a letter: ").lower()

        # Check if the guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter was already guessed
        if guess in letters_guessed:
            print("You already guessed that letter.")
            continue
        
        letters_guessed.append(guess)

        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            # Update the displayed word
            word_display = "".join(
                letter if letter in letters_guessed else "_" for letter in word_to_guess
            )
        else:
            incorrect_guesses += 1
            print(f"Oops! '{guess}' is not in the word. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        print("Current word: " + " ".join(word_display))

    # Game over conditions
    if "_" not in word_display:
        print("Congratulations! You've guessed the word:", word_to_guess)
    else:
        print("Sorry, you've run out of guesses. The word was:", word_to_guess)

# Start the game
hangman()
