from agents import Agent,ModelSettings
from agents.agent import StopAtTools
from my_config.gemini_config import GEMINI_MODEL
from my_tools.math_tool import add,sub,multiply
import rich

tool_beh_agent = Agent(
    name="tool_beh_agent",
    instructions="You're helpfull math tutor.",
    model=GEMINI_MODEL,
    tools=[add,sub,multiply],
    # tool_use_behavior="run_llm_again" # refine llm
    # tool_use_behavior="stop_on_first_tool" 
    # tool_use_behavior=StopAtTools(stop_at_tool_names=["add","multiply","sub"]),
    tool_use_behavior=StopAtTools(stop_at_tool_names=["add","multiply"]),
    # model_settings=ModelSettings(tool_choice="auto")
    # model_settings=ModelSettings(tool_choice="none")
    # model_settings=ModelSettings(tool_choice="required"),
    model_settings=ModelSettings(tool_choice="sub",parallel_tool_calls=False),
    reset_tool_choice=True
)

# rich.print(gemini_agent.name)
# rich.print(gemini_agent.tools)