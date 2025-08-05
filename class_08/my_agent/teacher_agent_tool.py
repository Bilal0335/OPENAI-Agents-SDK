from agents import Agent,ModelSettings
from my_config.gemini_config import GEMINI_MODEL
from agents.agent import StopAtTools
from my_tool.math_tool import add, generate_poem, sub, multiply, divide, explain_math_term

# ! ✅ Method 1: run_llm_again (default)
# teach_agent_tool = Agent(
#     name="teach_agent_tool",
#     instructions="You're a helpful math tutor.",
#     model=GEMINI_MODEL,
#     tools=[add, sub, multiply, divide, explain_math_term],
#     tool_use_behavior="run_llm_again"  
#     # LLM ko dobara chalana after tool
#     # LLM (AI brain) tool ka result dobara process karta hai aur explain karta hai.
# )

# ! ✅ Method 2: stop_on_first_tool
# teach_agent_tool_stop = Agent(
#     name="teach_agent_tool_stop",
#     instructions="You're a helpful math tutor.",
#     model=GEMINI_MODEL,
#     tools=[add, sub, multiply, divide, explain_math_term],
#     tool_use_behavior=StopAtTools(stop_at_tool_names=["multiply","add"])
#     #StopAtTools(...) =list y ander Or ki tarah kam krda hy
#     # StopAtTools(...) = direct tool result, no explanation
#     # tool_use_behavior="run_llm_again"
# )


# !!modelsetting

# 🔵 Less creative Agent (low temperature)
agent_low_temp = Agent(
    name="LowTempMathPoemAgent",
    instructions="You're a helpful math poet agent. Solve math or write poems using tools only.",
    model=GEMINI_MODEL,
    tools=[add, multiply, generate_poem],
    tool_use_behavior="run_llm_again",
    model_settings=ModelSettings(
        tool_choice="required",
        temperature=0.2  # Less creative
    )
)

# 🔴 More creative Agent (high temperature)
agent_high_temp = Agent(
    name="HighTempMathPoemAgent",
    instructions="You're a helpful math poet agent. Solve math or write poems using tools only.",
    model=GEMINI_MODEL,
    tools=[add, multiply, generate_poem],
    tool_use_behavior="run_llm_again",
    model_settings=ModelSettings(
        tool_choice="required",
        temperature=2.0  # Very creative!
    )
)

# ! ✅ Method 2: stop_on_first_tool mand modelSetting
# teach_agent_tool_stop = Agent(
#     name="teach_agent_tool_stop",
#     instructions="You're a helpful math tutor.",
#     model=GEMINI_MODEL,
#     tools=[add, sub, multiply, divide, explain_math_term],
#     tool_use_behavior=StopAtTools(stop_at_tool_names=["multiply","add"]),
#     model_settings=ModelSettings(tool_choice="sub")  #llm  tool call krta hy
    # model_settings=ModelSettings(tool_choice="required")  #llm  tool call krta hy
    # model_settings=ModelSettings(tool_choice="auto")  #llm  tool call krta hy
    # model_settings=ModelSettings(tool_choice="none")  #llm ny tool call nhi krta hy
    #StopAtTools(...) =list y ander Or ki tarah kam krda hy
    # StopAtTools(...) = direct tool result, no explanation
    # tool_use_behavior="run_llm_again"
# )


# ! method 2 Stop on first tool
# teach_agent_tool_stop = Agent(
#     name="teach_agent_tool_stop",
#     instructions="You're a helpful math tutor.",
#     model=GEMINI_MODEL,
#     tools=[add, sub, multiply, divide, explain_math_term],
#     tool_use_behavior="stop_on_first_tool"  
#     # Pehle tool result ko hi final maan lo
#     # Sirf tool ka result user ko return hota hai — AI kuch explain nahi karta.
# )

# ! ✅ Method 3: List of specific tools
# teach_agent_tool_list = Agent(
#     name="teach_agent_tool_list",
#     instructions="You're a helpful math tutor.",
#     model=GEMINI_MODEL,
#     tools=[add, sub, multiply, divide, explain_math_term],
#     tool_use_behavior=["add", "multiply"]  # sirf in tools par ruk jao
# )


"""

🔍 Detailed Explanation in Roman Urdu + English
🔧 tool_use_behavior = "run_llm_again"
Roman Urdu:
Is ka matlab hai ke jab AI koi tool use karega (jaise add(5, 3)), to tool ka result LLM ko dobara diya jayega — taki wo result ko explain kare, ya context add kare.

English:
After the tool is used, the LLM runs again to interpret or explain the result. Great when you want the LLM to say things like "The answer is 8."

⛔ tool_use_behavior = "stop_on_first_tool"
Roman Urdu:
Yeh keh raha hai: agar koi tool call ho gaya, to usi ka result final hai. LLM ko dobara mat chalao. Sirf tool ka output hi user ko dikhao.

English:
As soon as a tool is called, that result is returned directly. The LLM does not get a chance to add explanation. Good for fast or simple responses.

🧠 tool_use_behavior = ["add", "multiply"]
Roman Urdu:
Agar yeh specific tools (add, multiply) use ho gaye, to un par LLM ko dobara mat chalao. Lekin agar koi aur tool (jaise explain_math_term) use hua, to us par LLM chalay.

English:
If one of the listed tools is used, then stop there and return the result. For other tools not in the list, allow LLM to continue processing.




"""