from langgraph.graph import StateGraph,START,END
from src.langgraphAgenticAI.state.state import State
from src.langgraphAgenticAI.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphAgenticAI.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import ToolNode,tools_condition
from src.langgraphAgenticAI.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraphAgenticAI.nodes.ai_news_node import AINewsNode

class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot using Langgraph.
        This method initialises a chatbot node using the 'BasicChatbotNode' class
        and integrates it into the graph.The chatbot node is set as both the entryand exit point of the graph.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node and a tool node.
        It defines tools, initializes the chatbot with tool capabilities,
        and sets up conditional and direct edges between nodes.
        The chatbot node is set as the entry point.  
        """
        # define the tool and the tool node
        tools = get_tools()
        tool_node = create_tool_node(tools) 
    
        #define the llm
        llm = self.llm

        #Defne the chatbot node
        obj_chatbot_with_node = ChatbotWithToolNode(llm)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)

        #Adding the nodes
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        #Define the direct and conditional edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        # self.graph_builder.add_edge("chatbot",END)

    def ai_news_builder_graph(self):

        ai_news_node=AINewsNode(self.llm)
        #Creating and adding nodes for AI news use case
        self.graph_builder.add_node("fetch_news",ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",ai_news_node.summarize_news)
        self.graph_builder.add_node("save_results",ai_news_node.save_results)
        
        #Adding the edges for AI News usecase
        #Trying a different method to traverse graph from Start node to fetch news node using 'set_entry_point' function
        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_results")
        self.graph_builder.add_edge("save_results",END)


    def setup_graph(self,usecase:str):
        """
        Sets up the graph for the selected usecase.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        if usecase == "Chatbot with Web tool":
            self.chatbot_with_tools_build_graph()

        if usecase == "AI News":
            self.ai_news_builder_graph()

        return self.graph_builder.compile()