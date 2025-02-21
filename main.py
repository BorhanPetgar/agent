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
        
        action_match = None
        for line in result.split('\n'):
            action_match = action_re.match(line)
            if action_match:
                break
        
        if action_match:
            action, action_input = action_match.groups()
            if action not in known_actions:
                raise Exception(f'Unknown action: {action}: {action_input}')
            
            print(f'--- running {action} on {action_input}')
            try:
                observation = known_actions[action](action_input)
                print('Observation: ', observation)
                next_prompt = f'Observation: {observation}'
            except Exception as e:
                print(f'Action failed: {e}')
                next_prompt = f'Observation: Action failed: {e}'
                
        else:
            return result
                
        if "Answer:" in result:
            return result

                
                
print(query("What are the neighbors of Iran?"))
print(f'******** Question2 ********')
print(query("What is 5 to the power of 3?"))
