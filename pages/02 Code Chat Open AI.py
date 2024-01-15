import streamlit as st
from utils.openai_client_chat import openai_chat

st.title("Code Chat Assistant - ChatGPT-like")
st.markdown("Powered by OpenAI API :sunglasses:")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Hi I am Coding Assistant powered by OpenAI API. Ask me anything."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # pass chat messages to OpenAI client
        for response in openai_chat(st.session_state.messages):
            # update full_response
            full_response += (response.choices[0].delta.content or "")
            # update message_placeholder
            message_placeholder.markdown(full_response + "▌")
        # update full_response    
        message_placeholder.markdown(full_response)
    # update session_state
    st.session_state.messages.append({"role": "assistant", "content": full_response})