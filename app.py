#Q&A Chatbot

from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st

##Function to load OpenAI model and get Response

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),model_name='text-davinci-003',temperature=0.5)
    response=llm(question)
    return response

#Initialising streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input = st.text_input("Input: ",key="input")
response = get_openai_response(input)


submit = st.button("Ask your Question")

#If ask button is clicked

if submit:
    st.subheader("The response is: ")
    st.write(response)
    