from agents import Agent,enable_verbose_stdout_logging
from my_config.gemini_config import GEMINI_MODEL
from my_tool.math_tool import add,sub,multiply
import rich
# enable_verbose_stdout_logging()
teach_agent_tool = Agent(
    name="teach_agent_tool",
    instructions="You're helpfull math tutor.",
    model=GEMINI_MODEL,
    tools=[add,sub,multiply]
)

# rich.print(teach_agent_tool.name)
# rich.print(teach_agent_tool.tools)

# agent_astool = Agent(
#     name="agent_astool",
#     instructions="You're helpfull assistant.",
#     model=GEMINI_MODEL,
#     tools=[gemini_agent.as_tool(
#         tool_name="math_teacher",
#         tool_description="this is a math teacher tool"
#     )]
# )


# rich.print(agent_astool.tools