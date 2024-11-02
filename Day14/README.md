# Bulls and Cows Game

Bulls and Cows is a classic guessing game where players try to guess a secret 4-digit number. The player receives clues in the form of "Bulls" and "Cows" after each guess:
- **Bull**: A digit is correct and in the correct position.
- **Cow**: A digit is correct but in the wrong position.

The goal is to guess the correct number within the fewest turns possible.

## How to Play

1. Run the script in a Python environment.
2. You will see a prompt to "Guess the number," along with a hint represented by `****` (masking the number).
3. Enter a 4-digit number.
4. After each guess, you will receive feedback on how many Bulls and Cows were in your guess:
   - For example, if the secret number is `3128` and you guess `1234`, you might see "2 Bulls, 1 Cow" if two digits are correct and in the correct position, and one digit is correct but in the wrong position.
5. Continue guessing until you match the secret number.

## Requirements

- Python 3.x

## Running the Game

1. Clone the repository or download the `Bulls_Cows.py` file.
2. Open a terminal, navigate to the directory containing the file, and run:
   ```bash
   python Bulls_Cows.py
   
