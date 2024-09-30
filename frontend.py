
# import streamlit as st 
# import Backend as glib 

# st.set_page_config(page_title="Chatbot") 
# st.title("Chatbot 🤖") 


# if 'memory' not in st.session_state:
#     st.session_state.memory = glib.get_memory()


# if 'chat_history' not in st.session_state: 
#     st.session_state.chat_history = [] 

# for message in st.session_state.chat_history: 
#     with st.chat_message(message["role"]): 
#         st.markdown(message["text"]) 


# input_text = st.chat_input("Chat with your bot here") 

# if input_text: 
    
#     with st.chat_message("user"): 
#         st.markdown(input_text) 
    
#     st.session_state.chat_history.append({"role":"user", "text":input_text}) 
    
#     chat_response = glib.get_chat_response(input_text=input_text, memory=st.session_state.memory) 
    
#     with st.chat_message("assistant"): 
#         st.markdown(chat_response) 
    
#     st.session_state.chat_history.append({"role":"assistant", "text":chat_response}) 


import streamlit as st
import Backend as glib

# Set up the page title and layout
st.set_page_config(page_title="Chatbot 🤖", layout="centered")
st.title("Chatbot 🤖")

# Initialize session state for memory and chat history
if 'memory' not in st.session_state:
    st.session_state.memory = glib.get_memory()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat history on the page
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

# Input field for the user to chat with the bot
input_text = st.chat_input("Chat with your bot here")

# Check if input_text is not empty and process the response
if input_text:
    # Display user's message
    with st.chat_message("user"):
        st.markdown(input_text)

    # Append user's message to the chat history
    st.session_state.chat_history.append({"role": "user", "text": input_text})

    # Call the backend to get the chatbot response
    try:
        chat_response = glib.get_chat_response(input_text=input_text, memory=st.session_state.memory)
    except Exception as e:
        chat_response = f"Error occurred: {e}"

    # Display the chatbot's response
    with st.chat_message("assistant"):
        st.markdown(chat_response)

    # Append chatbot's response to the chat history
    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})

# Add a reset button to clear the chat history if needed
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.session_state.memory = glib.get_memory()  # Reset memory as well
