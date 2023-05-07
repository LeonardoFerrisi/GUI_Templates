import streamlit as st
from streamlit._util.keyboard import Key, keyboard_listener

# Define a callback function that will be called when the "Enter" key is pressed
def on_keypress(key):
    if key == Key.ENTER:
        st.write("Enter key pressed")

# Start the keyboard listener
keyboard_listener(on_keypress)

# Add a text input to the app
text_input = st.text_input("Enter some text:")

# Display the text that was entered
st.write("You entered:", text_input)
