from agents import Runner,set_tracing_disabled
from my_agent.teacher_agent_tool import teach_agent_tool
from my_config.gemini_config import GEMINI_MODEL
import rich
from my_tool.math_tool import add, sub, multiply

set_tracing_disabled(disabled=True)

teach_agent_tool = Runner.run_sync(
    starting_agent=teach_agent_tool,
    input=" 2 + 2? and is ma multiply kro 100",
)

# 📤 Print the final result from the agent
rich.print("\n🤖 CALLING AGENT\n")
rich.print(teach_agent_tool.final_output)
