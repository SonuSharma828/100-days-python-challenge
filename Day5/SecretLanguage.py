import random  # Importing the random module to select random characters

# Defining the alphabets, both lowercase and uppercase
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Two empty lists to hold the randomly chosen characters
list1 = []
list2 = []

# Picking 4 random characters from the alphabet and adding them to list1
for i in range(4):
    a = random.choice(alpha)
    list1.append(a)

# Picking 4 random characters from the alphabet and adding them to list2
for i in range(4):
    a = random.choice(alpha)
    list2.append(a)

# Function to encode the message
def encode_msg(msg):
    if len(msg) >= 3:
        # Move the first character to the end of the message
        msg = msg[1:] + msg[0]
        # Add random characters from list1 and list2 around the modified message
        msg = list1[0] + list1[1] + list1[2] + msg + list2[0] + list2[1] + list2[2]
        print(msg)
    else:
        # Reverse the message if it is less than 3 characters
        msg = msg[::-1]
        print(msg)

# Function to decode the encoded message
def decode_msg(msg):
    if len(msg) >= 3:
        # Remove the random characters from list1 and list2
        msg = msg[3:-3]
        # Move the last character to the beginning to reverse the encoding
        msg = msg[-1] + msg[:-1]
        print(msg)
    else:
        # Reverse the message if it is less than 3 characters
        msg = msg[::-1]
        print(msg)

# Main block to run the encode/decode program
if __name__ == "__main__":
    while True:
        print("CYBERICA".center(45))  # Display program title
        print(" 1. Encode".center(15))  # Option to encode
        print(" 2. Decode".center(15))  # Option to decode
        print("3. Exit".center(15))  # Option to exit
        choice = int(input("\nEnter your choice: "))  # User input for choice

        if choice == 1:
            # Input message to encode
            msg = input("Enter the message to encode: ")
            encode_msg(msg)
        elif choice == 2:
            # Input message to decode
            msg = input("Enter the message to decode: ")
            decode_msg(msg)
        elif choice == 3:
            # Exit the program
            break
        else:
            # Invalid input
            print("Invalid choice")
