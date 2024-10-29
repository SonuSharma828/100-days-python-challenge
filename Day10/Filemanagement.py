import os
import time

# Function to create a new file
def create_file(filename):
  try:
    # Attempt to create a file with the specified filename
    with open(filename, 'x') as f:
      print("Creating file, please wait....")
      time.sleep(3)
      print(f"File '{filename}' created successfully")
  except FileExistsError:
    # Error if the file already exists
    print("File already exists")
  except Exception as e:
    # General exception handling for unexpected errors
    print("Error creating file:", e)

# Function to read content from a file
def read_file(filename):
  try:
    # Attempt to open the file in read mode
    with open(filename, 'r') as f:
      print("Fetching file, please wait...")
      time.sleep(3)
      print(f.read())
  except FileNotFoundError:
    # Error if the file does not exist
    print("File not found")
  except Exception as e:
    print("Error reading file:", e)

# Function to append content to an existing file
def update_file(filename):
  try:
    # Open file in append mode
    with open(filename, 'a') as f:
      content = input("Enter content to append: ")
      print("Appending your data, please wait...")
      time.sleep(2)
      f.write(content + "\n")
      print("Data appended successfully")
  except FileNotFoundError:
    print("File not found")
  except Exception as e:
    print("Error updating file:", e)

# Function to delete a specified file
def delete_file(filename):
  try:
    print("Fetching file to remove...")
    time.sleep(2)
    os.remove(filename)
    print(f"File '{filename}' deleted successfully")
  except FileNotFoundError:
    print("File not found")
  except Exception as e:
    print("Error deleting file:", e)

# Function to list all files in the current directory
def list_files():
  try:
    files = os.listdir()
    if len(files) == 0:
      print("No files found")
    else:
      print("Files in current directory:")
      for file in files:
        print(file)
  except Exception as e:
    print("Error listing files:", e)

# Function to write new content to a file (overwriting if exists)
def write_file(filename):
  try:
    with open(filename, 'w') as f:
      content = input("Enter content to write: ")
      print("Writing your data, please wait...")
      time.sleep(2)
      f.write(content)
      print("Data written successfully")
  except FileNotFoundError:
    print("File not found")
  except Exception as e:
    print("Error writing file:", e)

# Main function to handle user inputs for file operations
def main():
  while True:
    print("\n")
    msg = " FILE MANAGEMENT SYSTEM "
    print(msg.center(40, "*"))
    print("\nFile Operations Menu:\n")
    print("1. Create a file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delete a file")
    print("5. List files")
    print("6. Write to a file")
    print("7. Exit")
    choice = input("\nEnter your choice (1-7): ")

    # Execute selected file operation
    if choice == '1':
      filename = input("Enter file name: ")
      create_file(filename)
    elif choice == '2':
      filename = input("Enter file name: ")
      read_file(filename)
    elif choice == '3':
      filename = input("Enter file name: ")
      update_file(filename)
    elif choice == '4':
      filename = input("Enter file name: ")
      delete_file(filename)
    elif choice == '5':
      list_files()
    elif choice == '6':
      filename = input("Enter file name: ")
      write_file(filename)
    elif choice == '7':
      print("Exiting program...")
      time.sleep(2)
      break
    else:
      print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
  main()
