# Fun Fact Generator

This Fun Fact Generator application is a simple Python-based web application that uses the PyWebIO library to display a random fun fact to users. By clicking the "Click me" button, users can load a new fun fact from an API with each click.

## Features

- Fetches a new fun fact from an API.
- Displays the fun fact in a styled format.
- Refreshes the fun fact on each button click.

## Requirements

- Python 3.x
- `requests` library
- `pywebio` library

## Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
    
2. Navigate to the project directory:
   ```bash
   cd FunFactGenerator
   ```
3. Install required libraries:
   ```bash
   pip install requests pywebio
   ```

## Usage

1. Run the server:
   ```bash
   python FunFacts.py
   ```
2. Open a web browser and go to `http://localhost:6979` to view the application.

## How It Works

- When the application starts, it displays a "Fun Fact Generator" title with an icon and a button.
- On clicking the button, the application fetches a random fun fact from the [uselessfacts API](https://uselessfacts.jsph.pl/) and displays it in blue text.
- The "Click me" button allows users to fetch a new fact each time it's clicked.

## License

This project is open-source and free to use under the MIT license.
