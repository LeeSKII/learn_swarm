import os
from dotenv import load_dotenv
from openai import OpenAI, api_key
from swarm import Swarm,Agent
import pprint

load_dotenv()

def get_weather(location:str)->str:
    return "{'temp':67, 'unit':'F'}"

api_key = os.getenv('DEEPSEEK_API_KEY')
gpt_api_key = os.getenv('GPT_API_KEY')

deepseek_url = 'https://api.deepseek.com'
gpt_url = 'https://api.gptapi.us/v1'

openai_client = OpenAI(api_key=gpt_api_key,base_url=gpt_url)

deepseek_model_name = 'deepseek-chat'
gpt_model_name = 'gpt-4o'
anthropic_model_name= 'claude-3-5-sonnet-20241022'

agent = Agent(name='agent',instructions='You are a helpful agent.',functions=[get_weather],model=gpt_model_name)

client = Swarm(client=openai_client)

messages = [{'role':'user','content':"What's the weather in NYC?"}]

response = client.run(agent=agent,messages=messages,max_turns=10,debug=True)

pprint.pprint(response.messages[-1]['content'])

