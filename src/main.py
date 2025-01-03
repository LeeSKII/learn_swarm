from swarm import Swarm, Agent
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")
print(api_key)

open_client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
)

client = Swarm(client=open_client)

def transfer_to_agent_b():
    return agent_b
  
def transfer_to_agent_c():
    return agent_c


agent_a = Agent(
    name="主理人",
    model="deepseek-chat",
    instructions="你是一位乐于助人的机器人。",
    functions=[transfer_to_agent_b,transfer_to_agent_c],
)

agent_b = Agent(
    name="英语专家",
    model="deepseek-chat",
    instructions="请只使用英语进行回复.",
)
agent_c = Agent(
    name="数学专家",
    model="deepseek-chat",
    instructions="精通数学运算，回复使用法语.",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "我想要求解数学问题，请帮我找一位精通数学的专家，解决3+4+5=?"}],
)

print(response.messages[-1]["content"])