import streamlit as st
from streamlit_chat import message as st_message

from modules import image_ocr
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
    
    # if (st.session_state.input_image != None):
        # image_text = image_ocr.get_image_text(st.session_state.input_image)
        # st.session_state["image_text"] = image_text
        # Get the response from chatgpt
        # gpt_response = get_gpt_response(image_text, st.session_state.history)

        # st.session_state.history.append({"message": image_text, "is_user": True})
        # st.session_state.history.append({"message": gpt_response, "is_user": False})

    return

def generate_response():
    if (st.session_state["input_image"] is not None):
        image_text = image_ocr.get_image_text(st.session_state.input_image)
        st.session_state["image_text"] = image_text
    
    image_text = ""
    if (st.session_state["input_image"] is not None):
        image_text = st.session_state.image_text
    input_text = st.session_state.input_text
    final_input = input_text + " " + image_text
    if (input_text != "" or input_text is not None):
        st.session_state.history.append({"message": input_text, "is_user": True})
    if (image_text != ""):
        st.session_state.history.append({"message": "Image text: "+image_text, "is_user": True})
    gpt_response = get_gpt_response(final_input, st.session_state.history)
    st.session_state.history.append({"message": gpt_response, "is_user": False})
    
    print("FINAL TEXT", final_input)
    
    st.session_state["input_text"] = ""
    st.session_state["image_text"] = ""

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
    st.file_uploader('Add images for the issue!', accept_multiple_files=False, type= ['png', 'jpg'], 
                     key="input_image", label_visibility="visible", on_change=generate_image_response)

    # Function to support text input
    st.text_input("Please give more info on your issue", key="input_text")
    
    st.button("Submit", on_click=generate_response)
    # Print the conversation history so far in the current session
    for i, chat in reversed(list(enumerate(st.session_state.history))):
        st_message(**chat, key=str(i))

    return


if __name__ == '__main__':
    get_user_input()
