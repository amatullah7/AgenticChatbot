import streamlit as st
import os
from src.langgraph.ui.uiconfigfile import Config

class LoadStremlitUI:
      def __init__(self):
            self.config=Config()
            self.user_controls={}

      def load_streamlit_ui(self):
            st.set_page_config(page_title="hello" + self.config.get_page_title(), layout="wide")
            st.header("hello" + self.config.get_page_title())

            with st.sidebar:
                  #Get options from config
                  llm_options = self.config.get_llm_options()
                  usecase_options = self.config.get_usecase_options()

                  #llm selection
                  self.user_controls["selected_llm"] = st.selectbox("select LLM", llm_options)
                  
                  if self.user_controls["selected_llm"] == "Groq":
                        #Model selection
                        model_options = self.config.get_groq_options()
                        self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                        self.user_controls["GROQ_API_KEY"]= st.session_state["GROQ_API_KEY"]=st.text_input("API_KEY", type="password")

                  #usecase selection
                  self.user_controls["selected_usecase"]=st.selectbox("Select usecase", usecase_options)

            return self.user_controls

