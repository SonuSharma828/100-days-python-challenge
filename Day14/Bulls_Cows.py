import random

# List of predefined 4-digit numbers to select from
list_number = ["3128", "4167", "3192", "4321", "8907", "9538", "3278", "0325", "3640", "3270"]

try:
    # Variables to store the guesses and the number of turns
    guesses = ''
    turns = 0
    
    # Randomly select a number from the list for the user to guess
    selected_number = random.choice(list_number)
    
    # Display instructions
    print("\n\n")
    print("Guess the number".center(80))
    print("\n\n\t Hint\n")
    
    # Print masked number as hint (e.g., "****")
    for x in selected_number:
        print("*", end=" ")
    
    print("\n\tGuess")
    
    # Main game loop
    while True:
        # Take user input
        guess = input()
        
        # Variables to count Bulls (correct position) and Cows (wrong position but correct digit)
        Count_Bull = 0
        Count_Cow = 0
        
        # Check if the guess matches the selected number
        if guess == selected_number:
            print(f"You guessed right in {turns} turns!")
            break
        else:
            # Increment turns as the guess was incorrect
            turns += 1
            
            # Check each digit for Bulls and Cows
            for i in range(len(selected_number)):
                if guess[i] == selected_number[i]:  # Correct digit in correct position
                    Count_Bull += 1
                elif guess[i] in selected_number:  # Correct digit in incorrect position
                    Count_Cow += 1
            
            # Display result of the guess
            print(f"{Count_Bull} Bulls, {Count_Cow} Cows")
            
except Exception as e:
    print(e)
  
