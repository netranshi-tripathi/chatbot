# chatbot/ollama.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
 

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt= ChatPromptTemplate.from_messages(
    [   ("system", "You are a helpful assistant .please provide response tp user question"),
        ("user", "Question: {question}"),
    ]
)

st.title("LangChain demo with gemma Chatbot")
input_text = st.text_input("Enter your question:")

llm= Ollama(
    model="gemma:2b",
)
output_parser = StrOutputParser()

chain= prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))    