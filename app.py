from time import time
import streamlit as st
from datetime import datetime
from streamlit_chat import message as st_message

import cv2
import numpy as np


# def get_user_input():
#     # st.set_page_config(layout="wide")
#     st.header('Smart Troubleshooter')
#
#     input_text = st.text_input(label='Please explain more about your issue')
#     input_image = None
#
#     # message("Hi! How may I help you?")
#     #
#     # # # Process the input image to get text
#     # image_text = get_image_text(input_image)
#     #
#     # final_text = input_text + ' ' + image_text
#     #
#     # # # Call Fine-tuned GPT
#     # gpt_response = get_gpt_response(final_text)
#     #
#     # # while True:
#     # #     message(input_sentence, is_user=True)
#     #
#     # # return

def generate_response():
    # Save the
    user_message = st.session_state.input_text

    # Get the response from chatgpt
    message_bot = 'bot response'

    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": message_bot, "is_user": False})

    return


def get_user_input():
    # Initialize the session state if not present
    if "history" not in st.session_state:
        st.session_state.history = []

    # Set the title of the page
    st.title("Smart Troubleshooter")

    # Function to support file input, on upload calls generate_response
    st.file_uploader('Add images for the issue!', accept_multiple_files=False, on_change=generate_response,
                     label_visibility="visible")

    # Function to support text input
    st.text_input("Please give more info on your issue", key="input_text", on_change=generate_response)

    # Print the conversation history so far in the current session
    for i, chat in enumerate(st.session_state.history):
        st_message(**chat, key=str(i))


if __name__ == '__main__':
    get_user_input()
