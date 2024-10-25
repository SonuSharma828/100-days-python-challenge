import time
import random

# List of all questions along with options and correct answers
question = [
    {
        'questions': 'Among whom of the following does the Indian Constitution permit to take part in the proceedings of Parliament?',
        'option': ['A. Solicitor General', 'B. Attorney General', 'C. Cabinet Secretary', 'D. Chief Justice'],
        'answer': 'B'
    },
    {
        'questions': 'Who is the first Prime Minister of India?',
        'option': ['A. Jawaharlal Nehru', 'B. Sardar Patel', 'C. Mahatma Gandhi', 'D. Lal Bahadur Shastri'],
        'answer': 'A'
    },
    {
        'questions': 'Which of the following is the capital of Arunachal Pradesh?',
        'option': ['A. Itanagar', 'B. Dispur', 'C. Imphal', 'D. Panaji'],
        'answer': 'A'
    },
    {
        'questions': 'Which of the following is the national flower of India?',
        'option': ['A. Lotus', 'B. Rose', 'C. Sunflower', 'D. Lily'],
        'answer': 'A'
    },
    {
        'questions': 'Which of the following is the national animal of India?',
        'option': ['A. Lion', 'B. Tiger', 'C. Elephant', 'D. Cow'],
        'answer': 'B'
    },
    {
        'questions': 'Who, in 1978, became the first person to be born in the continent of Antarctica?',
        'option': ['A. Emilio Palma', 'B. James Weddell', 'C. Nathaniel Palmer', 'D. Charles Wilkes'],
        'answer': 'A'
    },
    {
        'questions': 'Which colonial power ended its involvement in India by selling the rights of the Nicobar Islands to the British on October 16, 1868?',
        'option': ['A. Belgium', 'B. Italy', 'C. Denmark', 'D. France'],
        'answer': 'C'
    },
    {
        'questions': 'Which of these is not a dance of South India?',
        'option': ['A. Kathakali', 'B. Kathak', 'C. Manipuri', 'D. Bharatanatyam'],
        'answer': 'B'
    },
    {
        'questions': 'Which of these is not a part of Indian constitution?',
        'option': ['A. Power of attorney', 'B. Power of cabinet', 'C. Power of judiciary', 'D. Power of court'],
        'answer': 'A'
    },
    {
        'questions': 'Who is the first woman to successfully climb K2, the world’s second-highest mountain peak?',
        'option': ['A. Junko Tabei', 'B. Wanda Rutkiewicz', 'C. Tamae Watanabe', 'D. Chantal Mauduit'],
        'answer': 'B'
    },
    {
        'questions': 'Which of these is not a state of India?',
        'option': ['A. Tamil Nadu', 'B. Kerala', 'C. Andhra Pradesh', 'D. Karnataka'],
        'answer': 'C'
    }
]

# Function to start the quiz game
def questionaire():
    print("Welcome To KBC!".center(43))
    time.sleep(1)
    print("Let's Start The Game!\n")
    time.sleep(1)

    # Loop through each question in the list
    for i in question:
        print(i['questions'], "\n")
        
        # Display options for the current question
        for j in i['option']:
            print(j, "\n")
        
        # Get user's answer and check correctness
        user_answer = input("Enter Your Answer: ")
        if user_answer.upper() == i['answer']:
            print("\nCorrect Answer!")
            time.sleep(1)
            print("\nYou Won Rs.1000\n")
            time.sleep(2)
        else:
            print("\nWrong Answer!")
            time.sleep(1)
            print("\nYou Lost The Game!\n")
            break  # End game on the first wrong answer

# Run the game
questionaire()
  
