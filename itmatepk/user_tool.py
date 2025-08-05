from agents import Runner, set_tracing_disabled
from my_agent.user_fetch_data import user_data_agent
import rich

set_tracing_disabled(disabled=True)

res = Runner.run_sync(
    starting_agent=user_data_agent,
    input="Please return a list of all users' names and their usernames."

)

rich.print(res.final_output)
