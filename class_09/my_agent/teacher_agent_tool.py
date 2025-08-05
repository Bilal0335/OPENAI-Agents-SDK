
# ! teaching_agent_tool.py
from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_tool.math_tool import add ,sub,multiply,divide
import rich

teach_agent_tool = Agent(
    name="teach_agent_tool",
    model=GEMINI_MODEL,
    tools=[add, sub, multiply, divide]
)

teach_agent_as_tool = Agent(
    name="teach_agent_as_tool",
    model=GEMINI_MODEL,
    tools=[teach_agent_tool.as_tool(
        tool_name="math_tool",
        tool_description="A tool to teach the agent how to perform basic math operations like addition, subtraction, multiplication, and division."
    )]
)

# rich.print("Teaching Agent as Tool>>\n", teach_agent_as_tool.tools)