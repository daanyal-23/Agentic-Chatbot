from src.langgraphAgenticAI.state.state import State


class BasicChatbotNode:
    """
    Basic Chatbot logic implementation
    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State) -> dict:
        """
        Process the input state and generate a chatbot response
        """
        if not self.llm:
            raise ValueError("LLM model not initialized")
        return {"messages": [self.llm.invoke(state['messages'])]}
    