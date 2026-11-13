import streamlit as st
from langchain_ollama import ChatOllama

st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

llm = ChatOllama(
    model="llama3.2"
)

if st.button("Submit"):
    result = llm.invoke(user_input)
    st.write(result.content)