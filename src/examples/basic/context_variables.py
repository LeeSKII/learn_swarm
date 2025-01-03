from swarm import Swarm,Agent
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv('DEEPSEEK_API_KEY')

openai_client = OpenAI(api_key=api_key,base_url='https://api.deepseek.com')

client = Swarm(client=openai_client)

def instructions(context_variables:dict):
    name = context_variables.get('name')
    return f'You are a helpful bot. Greet the user by name ({name}).'

# Tool function
def print_account_details(context_variables:dict):
    user_id = context_variables.get('user_id')
    name = context_variables.get('name')
    print(f'Account details:{name},{user_id}')
    return 'Success getting account details,stopping.'

# Define agent
agent = Agent(name='agent',instructions=instructions,model='deepseek-chat',functions=[print_account_details])

context_variables = {'name':'John','user_id':12345}

# 如果不加max_turns，这个案例在一定概率下有可能会无限循环，LLM似乎并未识别到已完成了打印用户信息的任务
responses = client.run(agent=agent,messages=[{'role':'user','content':'print my account details'}],context_variables=context_variables,max_turns=20)

print(responses.messages[-1]['content'])