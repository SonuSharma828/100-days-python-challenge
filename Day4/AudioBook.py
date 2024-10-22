from gtts import gTTS  # Import Google Text-to-Speech module
import os  # Import os module to interact with the operating system
import PyPDF2 as pf  # Import PyPDF2 to work with PDF files
import time  # Import time module to add delays

def speak(text):
    """Use gTTS to convert text to speech and play the audio."""
    try:
        # Convert the given text to speech in English language
        tts = gTTS(text=text, lang='en')
        # Save the generated speech as an mp3 file
        tts.save("speech.mp3")
        print("Audio file saved as 'speech.mp3'. Playing now...")
        # Play the saved mp3 file using 'mpv' or another media player installed
        os.system("mpv speech.mp3")
    except Exception as e:
        # Print any errors encountered during speech generation or playback
        print(f"Error using gTTS: {e}")

# Speak a message before opening the PDF file
speak("Opening PDF file, please wait....")
time.sleep(1)  # Delay for 1 second

# Open the PDF file in read-binary mode
file = open("StoryBook.pdf", mode="rb")
pdf_reader = pf.PdfReader(file)  # Create a PDF reader object
pages = len(pdf_reader.pages)  # Get the total number of pages in the PDF

# Speak the number of pages in the PDF file
speak(f"There are a total of {pages} pages in this file")
speak("How many pages do you want to read? Single or multiple. Choose 's' for single and 'm' for multiple.")

# Get user input to decide whether to read a single or multiple pages
ch = input("s/m ")

if ch == 's':
    # If single page mode is selected
    speak("Enter page number here...")
    num_page = input("Page number: ")  # Get the page number to read
    speak("Preparing to speak...")
    time.sleep(2)
    speak("Ok! Let's start")
    time.sleep(1)
    page = pdf_reader.pages[int(num_page)]  # Get the requested page
    text = page.extract_text()  # Extract the text from the page
    print(text)  # Print the extracted text
    speak(text)  # Speak the extracted text
    time.sleep(1)
    speak("That's it.")
    print("Finished..")

elif ch == 'm':
    # If multiple pages mode is selected
    speak("Enter the page number from where you want to start reading.")
    snum = input("Starting Page Number: ")  # Get the starting page number
    speak("Enter the last page number where you want to end reading.")
    lnum = input("End Page Number: ")  # Get the ending page number
    s = int(lnum)  # Convert the ending page number to an integer
    for i in range(int(snum), s + 1):
        # Loop through the range of pages from start to end
        page = pdf_reader.pages[i]
        text = page.extract_text()  # Extract text from each page
        text1 = text.strip()  # Strip leading/trailing whitespace from the text
        print("Preparing to speak...")
        time.sleep(1)
        speak(text1)  # Speak the extracted and cleaned text
        time.sleep(1)
        print("Finished....")
else:
    # If the user input is invalid
    speak("Please choose one of the following...")
    print("s/m")
  
