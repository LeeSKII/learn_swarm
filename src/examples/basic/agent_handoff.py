from swarm import Swarm,Agent
from openai import OpenAI
import os
from dotenv import load_dotenv
import pprint

load_dotenv()

api_key = os.getenv('DEEPSEEK_API_KEY')

openai_client = OpenAI(api_key=api_key,base_url='https://api.deepseek.com')


client = Swarm(client=openai_client)

english_agent = Agent(name='English Agent',model='deepseek-chat',instructions='You only speak English.')

spanish_agent = Agent(name='Spanish Agent',model='deepseek-chat',instructions='You only speak Spanish.')

Mandarin_agent = Agent(name='Mandarin Agent',model='deepseek-chat',instructions='你只能使用简体中文进行交流。')

def transfer_to_spanish_agent():
    return spanish_agent

def transfer_to_mandarin_agent():
    return Mandarin_agent

english_agent.functions.append(transfer_to_spanish_agent)
english_agent.functions.append(transfer_to_mandarin_agent)


# messages = [{'role':'user','content': "Hola. ¿Como estás?"}]
messages = [{'role':'user','content': "你好，请帮我写一首三行诗"}]
# messages = [{'role':'user','content': "你好，我想学西班牙语。"}]

responses = client.run(agent=english_agent,messages=messages)

pprint.pprint(responses.messages)