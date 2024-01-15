
from utils.vertexai import create_session_state, reset_session
from utils.vertexai_client_chat import get_code_chat
import streamlit as st

st.set_page_config(
    page_title="Vertex AI Code Chat  API",
    page_icon=":robot:",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "# This app shows you how to use Vertex AI Code ChatAPI"
    },
)

# creating session states
create_session_state()



st.title(":red[PaLM 2] :blue[Vertex AI] Code Chat")
st.markdown("""
Codey for Code Chat `(codechat-bison)` is the name of the model that supports code chat. 
It's a foundation model that supports multi-turn conversations that are specialized for code.

Some common used cases for code chat are:

* **Get help about code**: Get help with questions you have about code, such as questions about an API, syntax in a supported programming language, or which version of a library is required for code you're writing.

* **Debugging**: Get help with debugging code that doesn't compile or that contains a bug.

* **Documentation**: Get help understanding code so you can document it accurately.

* **Learn about code**: Get help learning about code you're not familiar with.
""")

with st.sidebar:
   
    st.markdown(
        "<h2 style='text-align: center; color: red;'>Setting Tab</h2>",
        unsafe_allow_html=True,
    )

    st.write("Model Settings:")

    # define the temeperature for the model
    temperature_value = st.slider("Temperature :", 0.0, 1.0, 0.2)
    st.session_state["temperature"] = temperature_value

    # define the temeperature for the model
    token_limit_value = st.slider("Token limit :", 1, 2048, 512)
    st.session_state["token_limit"] = token_limit_value

    # define the temeperature for the model
    # top_k_value = st.slider("Top-K  :", 1, 40, 40)
    # st.session_state["top_k"] = top_k_value

    # # define the temeperature for the model
    # top_p_value = st.slider("Top-P :", 0.0, 1.0, 0.8)
    # st.session_state["top_p"] = top_p_value

    if st.button("Reset Session"):
        reset_session()


with st.container():
    st.write("Current Generator Settings: ")
    # if st.session_state['temperature'] or st.session_state['debug_mode'] or :
    st.write(
        "Temperature: ",
        st.session_state["temperature"],
        " \t \t Token limit: ",
        st.session_state["token_limit"],
        # " \t \t Top-K: ",
        # st.session_state["top_k"],
        # " \t \t Top-P: ",
        # st.session_state["top_p"],
        " \t \t Debug Model: ",
        st.session_state["debug_mode"],
    )

    prompt = st.text_area("Add your prompt: ", height=200)
    # if prompt:
    #     st.session_state["prompt"].append(prompt)
    #     st.markdown(
    #         "<h3 style='text-align: center; color: blue;'>Generator Model Response</h3>",
    #         unsafe_allow_html=True,
    #     )
    #     with st.spinner("PaLM is working to generate, wait....."):
    #         response = get_code_chat(
    #             prompt=prompt,
    #             temperature=st.session_state["temperature"],
    #             max_output_tokens=st.session_state["token_limit"],
    #         )
    #         st.session_state["response"].append(response)
    #         st.markdown(response)


    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt:
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = get_code_chat(
                 prompt=prompt,
                 temperature=st.session_state["temperature"],
                 max_output_tokens=st.session_state["token_limit"],
             )
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})