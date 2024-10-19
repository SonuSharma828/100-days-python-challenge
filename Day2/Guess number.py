import random as r  # Importing the random module to generate random numbers

while True:  # Infinite loop to keep the program running until the user chooses to exit
    print("\n")  # Print a new line for spacing
    print("Guess The Number".center(80))  # Display the title in the center of the console
    print("\n\t1. Play")  # Option to play the game
    print("\n\t2. Exit")  # Option to exit the game
    ch = input("\n\n\b Enter your choice: ")  # Prompt user to enter their choice

    match ch:  # Using match-case to handle user's choice
        case '1':  # If user chooses to play the game
            lifeline = 10  # Set the number of attempts (lifelines) to 10
            randomNum = r.randint(1, 1000)  # Generate a random number between 1 and 1000

            # Give the user a clue about the number of digits in the random number
            if randomNum >= 100 and randomNum < 1000:
                print("\nIt is a three-digit number. Guess in only 10 lifelines.\n\n")
            elif randomNum >= 10 and randomNum < 100:
                print("\nIt is a two-digit number. Guess in only 10 lifelines.\n\n")
            elif randomNum < 10:
                print("\nIt is a single-digit number. Guess in only 10 lifelines.\n\n")
            else:
                print("\nIt is a four-digit number. Guess in only 10 lifelines.\n\n")

            score = 0  # Initialize the score to 0

            # Start the guessing game with 10 lifelines
            while lifeline > 0:
                print(f"\nLife: {lifeline}".center(120))  # Display the remaining lifelines
                guess = input("\n\n\t Enter Your Guess: ")  # Prompt user to enter their guess

                # Try converting the guess to an integer, if not possible, ask for a valid number
                try:
                    guess = int(guess)
                except ValueError:
                    print("\nPlease enter a valid number.")  # Inform the user to enter a valid number
                    continue

                # Compare the user's guess with the random number
                if guess == randomNum:  # If guessed correctly
                    print("Congrats! You guessed the right number!")  # Congratulate the user
                    score = lifeline * 5  # Calculate the score based on remaining lifelines
                    print(f"Score: {score}")  # Display the score
                    break
                elif guess > randomNum:  # If guessed number is too high
                    lifeline -= 1  # Reduce a lifeline
                    print(f"The Guessed Number is too big")  # Inform the user that the guess was too high
                elif guess < randomNum:  # If guessed number is too low
                    lifeline -= 1  # Reduce a lifeline
                    print(f"The Guessed Number is too small")  # Inform the user that the guess was too low

            # If the user runs out of lifelines
            if lifeline == 0:
                print(f"\nYou've run out of lifelines. The number was {randomNum}.")  # Reveal the random number

            break  # Exit the game after one round

        case '2':  # If the user chooses to exit
            break  # Exit the program

        case _:  # Default case for invalid input
            print("\nInvalid choice. Please choose 1 or 2.")  # Inform the user about invalid input
                  
