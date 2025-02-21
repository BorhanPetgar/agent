import os
import httpx
from langchain_community.llms import Ollama

"""
from langchain_community.llms import Ollama

llm = Ollama(model="llama2")

llm.invoke("tell me about partial functions in python")
"""
class ChatBot:
    def __init__(self, system=''):
        self.system = system
        self.messages = []
        self.llm = Ollama(model="llama2")

        if self.system:
            self.messages.append({'role': 'system', 'content': system})

    def __call__(self, message):
        self.messages.append({'role': 'user', 'content': message})
        result = self.execute()
        self.messages.append({'role': 'assistant', 'content': result})
        return result
    
    def execute(self):
        result = self.llm.invoke(self.messages)
        # completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages)
        return result
    
