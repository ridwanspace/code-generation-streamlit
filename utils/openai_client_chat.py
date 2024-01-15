from openai import OpenAI
import os


def openai_chat(messages):
    """
    Generates a function comment for the given function body.

    Args:
        messages (List[Dict[str, str]]): The list of messages in the chat.

    Returns:
        OpenAIResponse: The response from the OpenAI chat completions.create method.
    """
    # Define the OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_KEY"))
    # create response by calling the OpenAI chat completions.create method
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=512,
        messages=[
                {"role": m["role"], "content": m["content"]}
                for m in messages
        ],
        stream=True,
    )
    
    return response