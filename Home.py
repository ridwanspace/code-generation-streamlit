import streamlit as st

from utils.openai_code_generation import generate_code

# page config
st.set_page_config(
    page_title="Code Generation",
    page_icon="🦜",
)

st.markdown("# Code Generation Using Langchain, OpenAI, and Vertex AI 🦜🔗")
st.markdown("""
Explore diverse AI-powered code generation tools tailored for different usage scenarios.

## App 1: Code Generation with OpenAI

**Description**:

_Generate code snippets for single instructions using OpenAI's powerful language models.
Focus on concise code generation for specific tasks within token budget constraints._

**`Technologies:`**

OpenAI API for text-to-code generation

**`Pros:`**

- Efficient code generation for targeted tasks
- Lower token consumption
- Simpler model interactions

**`Cons:`**

- Limited context for multi-step code generation
- Less suitable for interactive coding conversations

**`Use Cases`**

- Generating functions or blocks of code based on clear prompts
- Translating natural language descriptions into code
- Autocompleting repetitive code patterns
            


## App 2: Chat Assistant for Coding with OpenAI Chat GPT 3.5 Turbo

**`Description:`**

_Engage in multi-turn conversations about coding using OpenAI's advanced chatbot model.
Get assistance with problem-solving, debugging, and code understanding through natural language interactions._

**`Technologies:`**
- Langchain for model integration
- OpenAI Chat GPT 3.5 Turbo for conversational AI

**`Pros:`**

- Supports rich, interactive coding discussions
- Can provide guidance and explanations
- Adapts to evolving conversation flow

**`Cons:`**

- Higher token consumption due to multi-turn nature
- Potential for conversational inconsistencies

**`Use Cases:`**

- Asking for help with coding challenges
- Brainstorming code ideas and approaches
- Understanding code snippets and concepts

            
## App 3: Chat Assistant for Coding with Vertex AI's Code Chat Model

**`Description:`**

_Experience a coding-focused chatbot powered by Vertex AI's Code Chat model.
Leverage its specialized capabilities for code generation, translation, and explanation._

**`Technologies:`**

- Langchain for model integration
- Vertex AI Code Chat model for code-centric conversational AI

**`Pros:`**

- Deeper understanding of code syntax and semantics
- Optimized for code-related tasks
- Potential for more precise and consistent code generation

**`Cons:`**

- Requires Vertex AI setup and integration
- Model availability and usage costs

**`Use Cases:`**

- Generating code from detailed descriptions or requirements
- Debugging code with interactive troubleshooting
- Transforming code between different programming languages
- Explaining code functionality and logic


""")


