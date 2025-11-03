# src/langgraph/ui/load_ui.py

import streamlit as st
import os
from src.langgraph.ui.uiconfigfile import Config

class LoadStremlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="hello" + self.config.get_page_title(), layout="wide")
        st.header("hello" + self.config.get_page_title())

        # ✅ Initialize session_state keys to prevent reset on rerun
        for key in ["GROQ_API_KEY", "TAVILY_API_KEY", "selected_llm", "selected_usecase"]:
            if key not in st.session_state:
                st.session_state[key] = ""

        with st.sidebar:
            # Get options from config
            llm_options = [opt.strip() for opt in self.config.get_llm_options()]
            usecase_options = [opt.strip() for opt in self.config.get_usecase_options()]

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox(
                "Select LLM", llm_options, key="selected_llm"
            )

            if self.user_controls["selected_llm"] == "Groq":
                model_options = [opt.strip() for opt in self.config.get_groq_options()]
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.text_input("API_KEY", type="password", key="GROQ_API_KEY")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your GROQ_API_KEY key to proceed. Don't have? refer: https://controls.groq.com/")

            # Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Usecases", usecase_options, key="selected_usecase"
            )

            if self.user_controls["selected_usecase"] == "Chatbot With Web":
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"] = st.text_input("TAVILY API KEY", type="password", key="TAVILY_API_KEY")

                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your TAVILY_API_KEY key to proceed. Don't have? refer: https://app.tavily.com/home/")

        return self.user_controls
