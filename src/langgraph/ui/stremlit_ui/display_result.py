import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase.lower().startswith("basic chatbot"):
            # ✅ Correct input format for LangGraph
            input_state = {"messages": [HumanMessage(content=user_message)]}

            with st.chat_message("user"):
                st.write(user_message)

            # ✅ Stream LangGraph responses safely
            for event in graph.stream(input_state):
                for value in event.values():
                    if "messages" in value:
                        messages = value["messages"]

                        # Handle both list or single message
                        if isinstance(messages, list):
                            last_msg = messages[-1]
                        else:
                            last_msg = messages

                        # Only show if it's an AIMessage
                        if isinstance(last_msg, AIMessage):
                            with st.chat_message("assistant"):
                                st.write(last_msg.content)

        elif usecase.lower().startswith("chatbot with web"):
            # ✅ Correct input format for LangGraph
            input_state = {"messages": [HumanMessage(content=user_message)]}

            with st.chat_message("user"):
                st.write(user_message)

            # ✅ Stream LangGraph responses safely
            for event in graph.stream(input_state):
                for value in event.values():
                    if "messages" in value:
                        messages = value["messages"]

                        # Handle both list or single message
                        if isinstance(messages, list):
                            last_msg = messages[-1]
                        else:
                            last_msg = messages

                        # Only show if it's an AIMessage
                        if isinstance(last_msg, AIMessage):
                            with st.chat_message("assistant"):
                                st.write(last_msg.content)
