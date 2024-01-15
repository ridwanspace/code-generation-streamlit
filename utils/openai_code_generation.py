import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def generate_code(user_input):
        """
        Generate the code based on the user input.

        Parameters:
            user_input (str): The input provided by the user.

        Returns:
            str: The generated code based on the user input.
        """
        # Define the prompt
        prompt = PromptTemplate(
            input_variables=["code"],
            template="Write a code about {code}",
        )
        
        # Define the LLM
        llm = ChatOpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_KEY"))
        # pass llm to LLMChain
        chain = LLMChain(llm=llm, prompt=prompt)
        # Generate the code
        output = chain.run(user_input)
        
        return output