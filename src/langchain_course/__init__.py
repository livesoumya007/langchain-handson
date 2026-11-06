from langchain_core.output_parsers import StrOutputParser
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama


from dotenv import load_dotenv

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))


info = "Artificial Intelligence is changing the way we build software, and with it, the way developers work. One of the most exciting new roles emerging from this shift is the Full-stack AI Engineer - someone who not only understands how to integrate AI systems, but also knows how to deliver complete, user-ready applications. This role builds directly on the foundation of the modern full-stack developer, extending it into the world of machine learning, large language models (LLMs), and AI-first products."

summary_template = """
Based on the text below, provide a summary of the key points in bullet form:

{info}

and also give 2 interesting facts about it. 
"""
#temprature=0 => model is more deterministic
llm = ChatOpenAI(temperature=0, model="gpt-5")
# llm = ChatOllama(temperature=0, model="gemma4:e2b")

#A prompt template consists of a string template. 
#It accepts a set of parameters from the user that can be used to generate a 
# prompt for a language model.
summary_prompt_tenplate = PromptTemplate(input_variables=["info"], template=summary_template)

"""
LCEL ->  LangChain Expression Language).
Think of | as Promise chaining or Unix pipe:
In A | B: Take the output of A and automatically feed it as the input into B.
"""

chain = summary_prompt_tenplate | llm | StrOutputParser()

"""
    the invoke() executes the entire LCEL chain. First it passes the
    input to the PromptTemplate, then it passes the output of the PromptTemplate
    to the LLM, then it passes the output of the LLM to the output parser, then it
    passes the output of the output parser to the final result. 
"""
response = chain.invoke(input={"info":info})

print("checking: ", response)
