
# ! main.py
from agents import Runner,set_tracing_disabled
# from my_agent.teacher_agent_tool import teach_agent_tool,teach_agent_tool_stop
from my_agent.teacher_agent_tool import teach_agent_tool_stop
from my_config.gemini_config import GEMINI_MODEL
import rich
from my_tool.math_tool import add, sub, multiply, divide, explain_math_term

set_tracing_disabled(disabled=True)

# teach_agent_tool = Runner.run_sync(
#     starting_agent=teach_agent_tool,
#     input="2+2=? explain the answer step by step."
# )

# rich.print("Teaching Agent>>\n",teach_agent_tool.final_output)

# teach_agent_tool_stop = Runner.run_sync(
#     starting_agent=teach_agent_tool_stop,
#     input="what is 10 + 5? explain the answer step by step."
# )

teach_agent_tool_stop = Runner.run_sync(
    starting_agent=teach_agent_tool_stop,
    input="2+5=?"
    # input="2+5=? jo be answer ay us ko multiplay krdou 100. jo bi answer ay us ko sub krdou 50 se."
)

rich.print("Teaching Agent Tool Stop>>\n",teach_agent_tool_stop.final_output)

# teach_agent_tool_list = Runner.run_sync(
#     starting_agent=teach_agent_tool_list,
#     input="2+2=?"
# )

# rich.print("Teaching Agent Tool Lilst>>\n",teach_agent_tool_list.final_output)


# from config import config
# from agents import Agent,Runner,enable_verbose_stdout_logging,function_tool, ModelSettings

# # enable_verbose_stdout_logging()

# @function_tool
# def get_weather(city: str) ->str:
#     """Get the current weather for a given city."""
#     print(f"Fetching weather for {city}")
#     return f"The weather in {city} is sunny."

# @function_tool
# def get_time(city: str) -> str:
#     """Get the current time for a given city."""
#     print(f"Fetching time for {city}")
#     return f"The current time in {city} is 3:00 PM."

# @function_tool
# def get_news(topic: str) -> str:
#     """Get the latest news for a given topic."""
#     print(f"Fetching news for {topic}")
#     return f"The latest news on {topic} is that everything is going great!"

# @function_tool
# def get_joke() -> str:
#     """Get a random joke."""
#     print("Fetching a joke")
#     return "Why did the scarecrow win an award? Because he was outstanding in his field!"

# @function_tool
# def get_quote() -> str:
#     """Get a random quote."""
#     print("Fetching a quote")
#     return "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt"

# @function_tool
# def get_advice() -> str:
#     """Get a random piece of advice."""
#     print("Fetching advice")
#     return "Don't watch the clock; do what it does. Keep going. - Sam Levenson"


# @function_tool
# def summarize_text(text: str) -> str:
#     """Summarize the given text."""
#     print(f"Summarizing text: {text}")
#     return f"Summary: {text[:50]}..."

# @function_tool
# def translate_text(text: str, target_language: str) -> str:
#     """Translate the given text to the target language."""
#     print(f"Translating text: {text} to {target_language}")
#     return f"Translated text: {text} in {target_language}"

# @function_tool
# def generate_poem(topic: str) -> str:
#     """Generate a poem about the given topic."""
#     print(f"Generating poem about: {topic}")
#     return f"Roses are red, violets are blue, here's a poem about {topic} just for you!"

# @function_tool
# def create_story(character: str, setting: str) -> str:
#     """Create a story with the given character and setting."""
#     print(f"Creating story with character: {character} in setting: {setting}")
#     return f"Once upon a time in {setting}, {character} embarked on an adventure."

# agent = Agent(
#     name="Multi-Function Agent",
#     instructions="You can perform various tasks like fetching weather, time, news, jokes, quotes, advice, summarizing text, translating text, generating poems, and creating stories.Always respond with the result of the task by using tool.",
#     tools=[
#         get_weather,
#         get_time,
#         get_news,
#         get_joke,
#         get_quote,
#         get_advice,
#         summarize_text,
#         translate_text,
#         generate_poem,
#         create_story
#     ],
#     model_settings=ModelSettings(
#         tool_choice = "required",
#         temperature=2.0,

#     ),
#     # tool_use_behavior="stop_on_first_tool"
# )


# result = Runner.run_sync(
#     agent,
#     "What is the weather in New York? What time is it in New York? Can you also tell me a joke and latest news of lagend league and plz generate a poem about friendship?",
#     run_config=config,
#     max_turns=1)

# print(result.final_output)