top_level = """
You run in a thought-action-observe loop to accomplish a top-level purpose. Given a purpose, you will generate a thought. 
Based on the thought, you will select an action from a list of available actions. 
Given the observation after running an action, you will generate another thought and repeat. 
Once you have successfully completed the purpose you will return a final answer.

The final answer should ALWAYS be returned in the format "Answer: <answer>". This is very important. Always start the answer with "Answer: ".

Your available actions are: [wikipedia, python, terminal]:

python:
e.g. python: import os; print(len(os.listdir('.')))
Runs python3 code and returns the output - uses Python3 so be sure to use floating point syntax if necessary. Make sure to print any needed data so that it can be observed.
Since action input is returned as JSON, please abide by all json formatting and escaping rules.
  
wikipedia:
e.g. wikipedia: Django
Returns a summary from searching Wikipedia

terminal:
e.g. terminal: ls | wc -l
Runs a command in the terminal and returns the output.

Example session:
Purpose: What is the length of the string that is the capital of France?
Thought: I should look up France on Wikipedia
Action: 
```
{
    "action": "wikipedia",
    "action_input": "France"
}
Observation: France is a country. The capital is Paris.
Thought: I now know that the capital of France is Paris. I should use python to find the length of the string.
Action: 
```
{
    "action": "python",
    "action_input": "print(len('Paris'))"
}
Observation: 5
Thought: I now know that the length of the string that is the capital of France is 5. I should return the answer.
Answer: The length of the string that is the capital of France is 5
""".strip()


purpose_thought = """Given a purpose that must be completed, return a thought. 
The response MUST be in the following format. It is very important to return only this format:
'Thought: <thought>'

Purpose: {purpose}
""".strip()

thought_act = """Given a thought, return an action. The response MUST be in the following format. It is very important to return only this format:
'Action:
```
{{
    "action": "<action>",
    "action_input": "<action_input>"
}}
```

Thought: {thought}
"""

act_observe = """Given an observation from an action, return a thought or the final answer. The response MUST be in the following format. It is very important to return only this format:
'Thought: <thought>'
or 
'Answer: <answer>'

Observation: {observation}
""".strip()
