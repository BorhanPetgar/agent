from langchain_community.llms import Ollama
from langchain.schema import HumanMessage, SystemMessage


class ChatBot:
    def __init__(self, system=''):
        self.system = system
        self.messages = []
        if self.system:
            self.messages.append(SystemMessage(self.system))
        
        # Initialize Ollama with the desired model (e.g., "llama2")
        # self.llm = Ollama(model="deepseek-r1:1.5b")
        self.llm = Ollama(model="llama2")

    def __call__(self, message):
        self.messages.append(HumanMessage(message))
        
        result = self.execute_react()
        
        self.messages.append(result)
        return result

    def execute_react(self):
        response = self.llm.invoke(self.messages)
        return response

# Example usage
if __name__ == "__main__":
    bot = ChatBot(system="You are a helpful assistant that uses the ReAct framework.")
    response = bot("What is the capital of France?")
    print(response)