import streamlit as st
from chatbot import chatbot_response

st.title("🤖 ChatBuddy - Your Friendly Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", "")

if user_input:
    response = chatbot_response(user_input)
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

# Display messages
for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**🧍 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")
