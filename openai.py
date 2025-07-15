#langchain_API_KEY="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"
#
#

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
 
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt= ChatPromptTemplate.from_messages(
    [   ("system", "You are a helpful assistant .please provide response tp user question"),
        ("user", "Question: {question}"),
    ]
)

st.title("LangChain OpenAI Chatbot")
input_text = st.text_input("Enter your question:")

llm= ChatOpenAI(
    model="turbo-3.5",
    temperature=0.7,
    max_tokens=1000,
    streaming=True,
    verbose=True
)
output_parser = StrOutputParser()

chain= prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))    