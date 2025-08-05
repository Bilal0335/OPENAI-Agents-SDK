from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_agent.teacher_agent_tool import gemini_agent
import rich

# gemini_agent = Agent(
#     name="gemini_agent",
#     instructions="You're helpfull math tutor.",
#     model=GEMINI_MODEL,
#     tools=[add,sub]
# )

# rich.print(gemini_agent.name)
# rich.print(gemini_agent.tools)

agent_astool = Agent(
    name="agent_astool",
    instructions="You're helpfull assistant.",
    model=GEMINI_MODEL,
    tools=[gemini_agent.as_tool(
        tool_name="math_teacher",
        tool_description="this is a math teacher tool"
    )]
)


# rich.print(agent_astool.tools)