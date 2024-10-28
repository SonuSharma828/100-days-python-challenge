import random

# List of choices for the game
guess = ['stone', 'paper', 'scissor']
print(' Welcome to the game of stone, paper, and scissor \n')

# Initialize scores for user and computer
user_score = 0
computer_score = 0

# Function to handle the game logic
def game():
    # User input for choice
    user = input('\n Enter your choice (stone, paper, scissor): ')
    # Random choice for computer from the list
    computer = random.choice(guess)
    print(f'\n You chose {user} and computer chose {computer} \n')

    # Conditions to determine the winner or tie
    if user == computer:
        print(' It is a tie')
    elif user == 'stone' and computer == 'paper':
        print('You lose')
        # Uncomment the following line to track computer score
        # computer_score += 1
    elif user == 'stone' and computer == 'scissor':
        print('You win')
        # Uncomment the following line to track user score
        # user_score += 1
    elif user == 'paper' and computer == 'stone':
        print('You win')
        # Uncomment the following line to track user score
        # user_score += 1
    elif user == 'paper' and computer == 'scissor':
        print('You lose')
        # Uncomment the following line to track computer score
        # computer_score += 1
    elif user == 'scissor' and computer == 'stone':
        print('You lose')
        # Uncomment the following line to track computer score
        # computer_score += 1
    elif user == 'scissor' and computer == 'paper':
        print('You win')
        # Uncomment the following line to track user score
        # user_score += 1
    else:
        print('Invalid input')

# Main loop to play the game
while True:
    print("1. Play the game\n")
    print("2. Exit\n")
    choice = int(input("\n Enter your choice: "))
    if choice == 1:
        game()  # Start the game
    elif choice == 2:
        # Display final score and determine the game result
        print("\nThank you for playing\n")
        print("Your score is", user_score)
        if user_score > computer_score:
            print("\nYou Win The Game")
        break
    else:
        print(f"Invalid choice {choice}")
      
