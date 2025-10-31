from langgraph.graph import StateGraph, START, END
from src.langgraph.State.state import State
from src.langgraph.Nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model

    def basic_chatbot_build_graph(self):
        # ✅ Create the graph builder
        graph = StateGraph(State)

        # ✅ Create and register the node
        chatbot_node = BasicChatbotNode(self.llm)
        graph.add_node("chatbot", chatbot_node.process)

        # ✅ Define entry and exit edges
        graph.add_edge(START, "chatbot")
        graph.add_edge("chatbot", END)

        # ✅ Return the compiled graph
        return graph.compile()

    def setup_graph(self, usecase: str):
        usecase = usecase.strip().lower()

        if "basic chatbot" in usecase:
            return self.basic_chatbot_build_graph()
        else:
            raise ValueError(f"Unknown usecase: {usecase}")
