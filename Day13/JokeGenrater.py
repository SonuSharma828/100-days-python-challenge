# Import necessary libraries
import json
import requests
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

# Function to fetch and display a fun fact
def get_fun_fact(_):
    clear()  # Clears previous content on the screen
    
    # Display the title with a smiley image from an external URL
    put_html('<p align="left">'
             '<h2><img src="https://png.pngtree.com/element_our/20190529/ourmid/pngtree-smiling-illustration-cartoon-expression-image_1200038.jpg" width="7%"> Fun Fact Generator</h2>'
             '</p>')
    
    # Define the URL for the API that provides a random fun fact
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    # Send a GET request to the API and parse the response as JSON
    response = requests.get(url)
    data = json.loads(response.text)
    
    # Extract the fun fact from the JSON data
    useless_fact = data['text']
    
    # Display the fun fact in blue text with a larger font size
    style(put_text(useless_fact), 'color:blue; font-size: 30px')
    
    # Add a button that, when clicked, fetches a new fun fact
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )

# Main content function that displays the initial layout
def content():
    # Display the initial heading and image for the Fun Fact Generator
    put_html(
        '<p align="left">'
        '<h2><img src="https://png.pngtree.com/element_our/20190529/ourmid/pngtree-smiling-illustration-cartoon-expression-image_1200038.jpg" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )
    
    # Add a button to start generating fun facts on click
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact  # The button triggers the get_fun_fact function
    )
    hold()  # Keeps the server running and holds the session

# Start the server on port 6979 and load the content function
if __name__ == '__main__':
    start_server(content, port=6979)
  
