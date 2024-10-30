import zipfile

# Function to crack password from a given password list file
def crack_password(password_list, obj):
    idx = 0  # Counter for the number of attempts
    # Open password list file in binary mode
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    # Try to extract the zip file using the current password
                    obj.extractall(pwd=word)
                    print("Password found at position", idx)
                    print("Password is", word.decode())  # Decode and print the password
                    return True  # Return True if password is found
                except:
                    continue  # Continue if the password is incorrect
    return False  # Return False if password is not found

# Specify the name of the zip file and the password list file
zip_file = "gfg.zip"
password_list = "password_list.txt"

# Create a ZipFile object for the zip file
obj = zipfile.ZipFile(zip_file)

# Count the total number of passwords in the password list
cnt = len(list(open(password_list, 'rb')))
print("There are", cnt, "passwords to test")

# Call the function to crack the password and print appropriate message
if crack_password(password_list, obj) == False:
    print("Password not found")
