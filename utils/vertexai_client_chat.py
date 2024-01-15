# import libraries
import os
import vertexai
from google.oauth2 import service_account
from dotenv import load_dotenv
from vertexai.language_models import CodeChatModel
import streamlit as st

# initiate service account (authentication)
json_path = os.getenv('VERTEXAI_SA')
credentials = service_account.Credentials.from_service_account_file(json_path)
# start Vertex AI
load_dotenv()
vertexai.init(project=os.environ["PROJECT_ID"], # replace with your own project
              credentials=credentials)

def vertexai_chat():
    """
    Generates a function comment for the given function body.

    Args:
        messages (List[Dict[str, str]]): The list of messages in the chat.

    Returns:
        OpenAIResponse: The response from the OpenAI chat completions.create method.
    """
    # Define the Vertex AI code chat model
    model = CodeChatModel.from_pretrained("codechat-bison@002")
    # start code chat
    code_chat = model.start_chat(max_output_tokens=512)
    # pass prompt to code chat
    # response = code_chat.send_message(prompt).text

    return code_chat

@st.cache_resource
def get_model():
    chat_model = CodeChatModel.from_pretrained("codechat-bison@002")
    start_chat = chat_model.start_chat()
    return start_chat


def get_code_chat(prompt="", **parameters):
    generation_model = get_model()
    response = generation_model.send_message(prompt, **parameters)

    return response.text
