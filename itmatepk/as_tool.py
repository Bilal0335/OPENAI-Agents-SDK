from agents import Runner, set_tracing_disabled
from my_agent.teacher_agent_tool import agent_astool
import rich

set_tracing_disabled(disabled=True)

res = Runner.run_sync(
    starting_agent=agent_astool,
    input="Adding 10, 20 and subtract 40"

)

rich.print(res.final_output)
