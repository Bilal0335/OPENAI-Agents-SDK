
# ! ctx_agents.py
from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_tools.ctx_tool import get_age,get_role,get_user_summary,get_course,get_university
from instruction.dynamic_instr import dynamic_instruction
from user_data_type.user_data import UserData
import rich


ctx_agents = Agent[UserData](
    name="ctx_agents",
    instructions=dynamic_instruction,
    model=GEMINI_MODEL,
    tools=[get_age,get_role,get_user_summary,get_course,get_university]
)

# rich.print(gemini_agent.name)
# rich.print(gemini_agent.tools)