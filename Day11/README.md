# ZipFileExtracter

## Description
`ZipFileExtracter.py` is a Python script designed to crack the password of a protected zip file by brute-forcing through a list of potential passwords provided in a text file. This program uses the `zipfile` library to attempt extraction with each password until the correct one is found.

## Features
- Attempts to extract a zip file with each password in a given password list.
- Displays the position and the correct password once found.
- Shows the total count of passwords to be tested before starting.

## Requirements
- Python 3.x
- `zipfile` library (standard with Python)

## Usage
1. Prepare a zip file (`gfg.zip`) that is password-protected.
2. Create a text file (`password_list.txt`) containing possible passwords, one per line.
3. Run the script:
   ```bash
   python ZipFileExtracter.py
   
