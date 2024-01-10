import streamlit as st

from utils.code_generation import generate_code

# page config
st.set_page_config(
    page_title="Code Generation - OpenAI",
    page_icon="🦜",
)

st.markdown("# Code Generation Using Langchain - OpenAI 🦜🔗")
st.markdown("""
This is a tool for AI based code generation. 
It uses Open AI for code generation and code completion. 
""")


# Define the Streamlit app
prompt = st.text_area(label="Enter your prompt here", height=300)

if st.button("Generate code"):
    code = generate_code(prompt)
    st.markdown(code)