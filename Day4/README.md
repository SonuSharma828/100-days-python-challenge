# PDF Reader and Speaker with gTTS

This Python program reads the content of a PDF file and converts it into speech using **gTTS** (Google Text-to-Speech) library. The user can choose to read either a single page or a range of pages from the PDF file, and the program will speak the content aloud.

## Features
- Convert text from PDF to speech.
- Choose between reading a single page or multiple pages.
- Output the text from the PDF in the console.
- Playback of generated speech via an installed media player (e.g., mpv).

## Prerequisites
- Python 3.x
- Required Python modules:
  - `gTTS`
  - `PyPDF2`
  - `os`
  - `time`

You can install the necessary modules using the following commands:
```bash
pip install gtts
pip install PyPDF2

You also need a media player installed on your system that can be invoked via command-line. For example, you can use mpv, vlc, or any other suitable player. Make sure to change the command to match your player (e.g., os.system("vlc speech.mp3") if you use VLC).

## Usage

1. Place the PDF file you want to read in the same directory as this script. Rename it to StoryBook.pdf or change the file name in the script.

2. Run the script:
    python AudioBook.py
3.Choose whether to read a single page (s) or multiple pages (m).

4. Follow the prompts to input the page number(s).

5. The program will read the PDF content and convert it to speech.

##Example

To read and speak the contents of page 2, choose the single page option and enter 2. For multiple pages, choose the range you wish to read.

s/m: s
Page number: 2

## Notes

-Ensure your media player can be invoked from the command line.
-You can modify the program to support different languages by changing the language code in gTTS initialization.

tts = gTTS(text=text, lang='en')  # Change 'en' to desired language code

-Add error handling for file access and user input if needed.

## License

This project is open-source and free to use.

Let me know if you'd like any further improvements!

