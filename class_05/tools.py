from agents import Agent,Runner,function_tool
from main import config
import rich

@function_tool
def usd_to_pkr():
    return 'Today USD to PKR is 280'

simple_agent = Agent(
    name="Simple Assistant",
    instructions="You are helpfull assistant",
    tools=[usd_to_pkr]
)

res = Runner.run_sync(
    starting_agent=simple_agent,
    input="what is USD to PKR today?",
    run_config=config
)

rich.print(res.final_output)