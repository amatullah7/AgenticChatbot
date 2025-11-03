from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode

def get_tools():
    # Initialize Tavily tool (limit to 2 results)
    tools = [TavilySearch(max_results=2)]
    return tools

def create_tool_node(tools):
    # Create a tool node for use in LangGraph
    return ToolNode(tools=tools)
