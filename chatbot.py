import os
import openai
import httpx


class ChatBot:
    def __init__(self, system=''):
        self.system = system
        self.message = []
        if self.system:
            self.messages.append({'role': 'system', 'content': system})

    def __call__(self, message):
        self.messages.append({'role': 'user', 'content': message})
        result = self.exectute()
        self.messages.append({'role': 'assistant', 'content': result})
        return result
    
    def execute(self):
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages)
        return completion.choices[0].message.content
    
