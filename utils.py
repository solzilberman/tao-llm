import textwrap

class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    ORANGE = '\033[33m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    LIGHTGREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log_thought(thought):
    thought = thought.replace('Thought: ', '')
    thought = textwrap.fill(thought)
    print(f'{colors.CYAN}Thought: {colors.ENDC}{thought}')

def log_action(action, action_input):
    print(f'{colors.GREEN}Action: {colors.ENDC}{action}\n{colors.LIGHTGREEN}Action Input: {colors.ENDC}{action_input}')

def log_observation(observation):
    observation = textwrap.fill(observation)
    print(f'{colors.YELLOW}Observation: {colors.ENDC}{observation}')

def log_answer(answer):
    answer = textwrap.fill(answer)
    print(f'{colors.RED}Answer: {colors.ENDC}{answer}')

def log_purpose(purpose):
    print(f'{colors.ORANGE}Purpose: {colors.ENDC}{purpose}')