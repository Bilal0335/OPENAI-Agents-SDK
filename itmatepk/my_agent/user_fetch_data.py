
# ! user_fetch_data.py
from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_tools.user_data import fetch_user_data
import rich

user_data_agent = Agent(
    name="user_data_agent",
    instructions="You are a helpful agent that fetches user data.",
    model=GEMINI_MODEL,
    tools=[fetch_user_data]
)

# rich.print(user_data_agent.name)
# rich.print("__"*13)
# rich.print(user_data_agent.tools)
# rich.print("__"*13)
