
# ! main.py
from agents import Runner,set_tracing_disabled
from my_agent.teacher_agent_tool import teach_agent_tool,teach_agent_as_tool
from my_config.gemini_config import GEMINI_MODEL
import rich


set_tracing_disabled(disabled=True)

# teach_agent_tool = Runner.run_sync(
#     starting_agent=teach_agent_tool,
#     input="2+2=?"
# )

# rich.print("Teaching Agent>>\n",teach_agent_tool.final_output)


teach_agent_as_tool = Runner.run_sync(
    starting_agent=teach_agent_as_tool,
    input="2+2=?"
)

rich.print("Teaching Agent as Tool>>\n",teach_agent_as_tool.final_output)

