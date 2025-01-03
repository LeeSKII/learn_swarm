import os
from dotenv import load_dotenv
from openai import OpenAI
from swarm import Swarm,Agent
import pprint

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

openai_client = OpenAI(api_key=api_key,base_url="https://api.deepseek.com")

client = Swarm(client=openai_client)

agent = Agent(name="Agent",instructions='You are a helpful bot.',model='deepseek-chat')

messages = [{'role':'user','content':'why water is important?'}]

responses = client.run(agent=agent,messages=messages)

pprint.pprint(responses.messages[-1]['content'])