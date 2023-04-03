import openai
import re
import httpx
import os
from dotenv import load_dotenv
import sys
from io import StringIO
import json 

from prompts import top_level, purpose_thought, thought_act, act_observe
from tools import wikipedia, python_repl, terminal
from utils import log_thought, log_action, log_observation, log_answer, log_purpose

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class LLM:
    def __init__(self, system=""):
        self.system = system
        self.messages = []
        if self.system:
            self.messages.append({"role": "system", "content": system})
    
    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result
    
    def execute(self):
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages)
        # print(completion.usage)
        return completion.choices[0].message.content


action_re = re.compile(r"Action:\s+```(.*?)```", re.DOTALL)
def thought_act_observe(purpose, max_iters=10):
    '''
    Given a purpose, this executes the Thought, Act, Observe loop.
    '''
    driver = LLM(system=top_level)
    log_purpose(purpose)
    pt = purpose_thought.format(purpose=purpose)
    thought = driver(pt)
    log_thought(thought)
    step = 0
    while step < max_iters:
        step += 1
        ta = thought_act.format(thought=thought)
        action = driver(ta)
        action = action_re.search(action)
        if not action:
            print(f'No action found in response: {action}')
            observation = "No action found. Did you mean to return an answer?"
        else:
            action = action.group(1)
            action = json.loads(action)
            action, action_input = action["action"], action["action_input"]
            log_action(action, action_input)
            if action not in known_actions:
                return f"Error: Unknown action {action}"
            observation = known_actions[action](action_input)
        log_observation(observation)
        ao = act_observe.format(observation=observation)
        thought = driver(ao)
        if "answer:" in thought.lower():
            log_answer(thought)
            return thought
        
        log_thought(thought)

known_actions = {
    "wikipedia": wikipedia,
    "python": python_repl,
    "terminal": terminal,
}

if __name__ == "__main__":
    thought_act_observe("What is my internet speed?")