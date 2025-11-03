from langgraph.graph import StateGraph, START, END
from src.langgraph.State.state import State
from src.langgraph.Nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph.Nodes.chatbot_with_tools_node import ChatbotWithToolNode
from src.langgraph.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition


class GraphBuilder:
    def __init__(self, model):
        self.llm = model

    def basic_chatbot_build_graph(self):
        graph = StateGraph(State)

        chatbot_node = BasicChatbotNode(self.llm)
        graph.add_node("chatbot", chatbot_node.process)

        graph.add_edge(START, "chatbot")
        graph.add_edge("chatbot", END)

        return graph.compile()

    def chatbot_with_tools_build_graph(self):
        tools = get_tools()
        tool_node = create_tool_node(tools)

        llm = self.llm
        chatbot_with_node = ChatbotWithToolNode(llm)
        chatbot_node = chatbot_with_node.create_chatbot(tools)

        graph = StateGraph(State)
        graph.add_node("chatbot", chatbot_node)
        graph.add_node("tools", tool_node)

        graph.add_edge(START, "chatbot")
        graph.add_conditional_edges("chatbot", tools_condition)
        graph.add_edge("tools", "chatbot")
        graph.add_edge("chatbot", END)

        return graph.compile()

    def setup_graph(self, usecase: str):
        usecase = usecase.strip().lower()

        if "basic chatbot" in usecase:
            return self.basic_chatbot_build_graph()
        elif "chatbot with web" in usecase:
            return self.chatbot_with_tools_build_graph()
        else:
            raise ValueError(f"Unknown usecase: {usecase}")
