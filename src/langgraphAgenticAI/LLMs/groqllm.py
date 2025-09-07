import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        if not self.user_controls_input:
            raise ValueError("User controls input is None")
        try:
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY", "")
            selected_groq_model = self.user_controls_input.get("selected_groq_model", "")
            api_key = groq_api_key or os.environ.get("GROQ_API_KEY", "")
            if not api_key:
                st.error("Please Enter the Groq API Key")
                return None

            llm = ChatGroq(api_key=api_key, model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error Occured With the Following Exception : {e}")
        return llm
