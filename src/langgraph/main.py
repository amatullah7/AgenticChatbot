import streamlit as st
from src.langgraph.ui.stremlit_ui.load_ui import LoadStremlitUI
from src.langgraph.LLM.groqllm import GroqLLM
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.ui.stremlit_ui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():
      """
      LOADS UI
      
      """

      ##load ui
      ui=LoadStremlitUI()
      user_input=ui.load_streamlit_ui()

      if not user_input:
            st.error("Error: Failed to load user input from the UI . ")
            return
      
      user_message = st.chat_input("Enter your message")

      if user_message:
            try:
                  #config LLM
                  obj_llm_config = GroqLLM(user_controls_input=user_input)
                  model = obj_llm_config.get_llm_model()

                  if not model:
                        st.error("Error: LLM model could not be initialized")
                        return

                  #Initialize and set up the graph based on use case
                  usecase = user_input.get('selected_usecase')
                  if not usecase:
                        st.error("Error: No use case selected")
                        return 
                  
                  ##Graph Builder
                  graph_builder=GraphBuilder(model)
                  try:
                        graph=graph_builder.setup_graph(usecase)
                        DisplayResultStreamlit(usecase, graph,user_message).display_result_on_ui()
                  except Exception as e:
                        st.error(f"Error: Graph set up failed {e}")


            except Exception as e:
                  st.error(f"Error: Graph set up failed- {e}")
                  return