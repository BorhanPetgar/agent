from chatbot import ChatBot
from prompt import prompt
from tools import known_actions, calculate, wikipedia
import re


action_re = re.compile('^Action: (\w+): (.*)')

def query(question, max_turns=5):
    i = 0
    bot = ChatBot(prompt)
    next_prompt = question
    
    while i < max_turns:
        i += 1
        result = bot(next_prompt)
        print(result)
        actions = [action_re.match(a) for a in result.split('\n') if action_re.match(a)]
        if actions:
            action, action_input = actions[0].groups()
            if action not in known_actions:
                raise Exception(f'Unknown action: {action}: {action_input}')
            print(f'--- running {action} on {action_input}')
            observation = known_actions[action](action_input)
            print('Observation: ', observation)
            next_prompt = f'Observation: {observation}'
        else:
            return result
                
                
                
print(query("what is a cat?"))
