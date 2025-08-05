from agents import Runner, set_tracing_disabled
from my_tools.agent_tool_control import tool_beh_agent
import rich

set_tracing_disabled(disabled=True)

res = Runner.run_sync(
    starting_agent=tool_beh_agent,
    # input = "2 aur 5 ka sum karo, phir jo bhi answer aaye usko 5 se minus karo aur us k multiply kro 10 ko"
    input=" 12 + 5 = ?",
    max_turns=4


)

rich.print(res.final_output)
