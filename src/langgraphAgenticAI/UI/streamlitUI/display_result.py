import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json

class DisplayResultSTreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase == "Basic Chatbot":
            for event in graph.stream({'messages': [HumanMessage(content=user_message)]}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message('user'):
                        st.write(user_message)
                    with st.chat_message('assistant'):
                        st.write(value['messages'][-1].content)
        elif usecase == "Chatbot with Web tool":
            with st.chat_message('user'):
                st.write(user_message)
            for event in graph.stream({'messages': [HumanMessage(content=user_message)]}):
                for value in event.values():
                    for message in value['messages']:
                        if isinstance(message, AIMessage):
                            if message.tool_calls:
                                with st.chat_message('assistant'):
                                    st.write("Assistant is calling tools...")
                            else:
                                with st.chat_message('assistant'):
                                    st.write(message.content)
                        elif isinstance(message, ToolMessage):
                            with st.chat_message('assistant'):
                                st.write(f"Tool Result: {message.content}")

        elif usecase =="AI News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing the news.."):
                result = graph.invoke({"messages": [HumanMessage(content=frequency)], "news_data": [], "summary": ""})
                try:
                    #Read the markdown file
                    AI_NEWS_PATH = f"./AINews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH,'r') as file:
                        markdown_content = file.read()

                    #Display the markdown content in streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News not generated or file not found : {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error has occured: {str(e)}")