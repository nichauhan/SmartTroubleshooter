import streamlit as st
from streamlit_chat import message as st_message

from modules.image_ocr import get_image_text
from modules.gpt_troubleshoot import get_gpt_response


def generate_text_response():
    """
    Function to process the use input text and return the GPT response
    """
    # Get the user input text data
    input_text = st.session_state.input_text

    # Get the response from chatgpt
    gpt_response = get_gpt_response(input_text, st.session_state.history)

    st.session_state.history.append({"message": input_text, "is_user": True})
    st.session_state.history.append({"message": gpt_response, "is_user": False})

    st.session_state["input_text"] = ""

    return


def generate_image_response():
    """
    Function to extract the text from user input image and return the GPT response
    """
    # Process the user image to extract text
    image_text = get_image_text(st.session_state.input_image)

    # Get the response from chatgpt
    gpt_response = get_gpt_response(image_text, st.session_state.history)

    st.session_state.history.append({"message": image_text, "is_user": True})
    st.session_state.history.append({"message": gpt_response, "is_user": False})

    return


def get_user_input():
    """
    Main function to take user inout text/image and provide response using fine-tuned GPT-3
    """
    st.set_page_config(layout="wide")

    # Initialize the session state if not present
    if "history" not in st.session_state:
        st.session_state.history = [{"message": "Hello! How may I assist you with your Windows issue today?", "is_user": False}]

    # Set the title of the page
    st.title("Smart Troubleshooter")

    # Function to support file input, on upload calls generate_response
    st.file_uploader('Add images for the issue!', accept_multiple_files=False, on_change=generate_image_response,
                     key="input_image", label_visibility="visible")

    # Function to support text input
    st.text_input("Please give more info on your issue", key="input_text", on_change=generate_text_response)

    # Print the conversation history so far in the current session
    for i, chat in reversed(list(enumerate(st.session_state.history))):
        st_message(**chat, key=str(i))

    return


if __name__ == '__main__':
    get_user_input()
