from time import *  # Import all functions from the time module
import random as r  # Import the random module for selecting random test phrases
global error  # Declare a global variable to track errors

# Function to calculate the number of errors between the test paragraph and user input
def calculateError(testpara, userpara):
    error = 0  # Initialize error counter to 0
    for x in range(len(testpara)):  # Loop through the characters in the test paragraph
        try:
            # Compare characters in the test paragraph and user input
            if testpara[x] != userpara[x]:
                error += 1  # Increment error count if characters don't match
        except Exception as e:
            error += 1  # Handle any exceptions and increment error count
    return error  # Return total number of errors

# Function to calculate typing speed based on input time and user input length
def calculateSpeed(time1, time2):
    timeF = round(endTime - startTime, 2)  # Calculate and round time difference
    speed = len(userInput) / timeF  # Calculate speed as characters per second
    return round(speed)  # Return rounded speed

# Sample test paragraph for the typing test
test = ["Python is an interpreted, object-oriented, high-level programming language with dynamic semantics."]
test_1 = r.choice(test)  # Randomly select a test paragraph

# Display instructions for the typing speed test
print("Typing Speed Test".center(100))
print("\n\n")
print(test_1)  # Print the selected test paragraph
print("\n\nStart typing....\n\n")

# Record start time
startTime = time()
userInput = input()  # Capture the user's typing input
# Record end time
endTime = time()

# Calculate and display the number of errors
print("Error = ", calculateError(test_1, userInput))
# Calculate and display the typing speed
print("Speed = ", calculateSpeed(startTime, endTime))
