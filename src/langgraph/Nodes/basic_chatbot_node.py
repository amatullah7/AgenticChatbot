from src.langgraph.State.state import State


class BasicChatbotNode:
      """
      basic chatbot logic implementation
      """

      def __init__(self, model):
            self.llm=model
      
      def process(self, state:State)->dict:
            """processes the input state and generates a chatbot response"""
            return {"messages":self.llm.invoke(state['messages'])}

      