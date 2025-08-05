from agents import Agent,Runner,function_tool
from main import config
import rich

@function_tool
def add(n1: int, n2: int) -> str:
    """
    Adds two integers and returns the result as a formatted string.

    Args:
        n1 (int): The first number.
        n2 (int): The second number.

    Returns:
        str: A string showing the sum.
    """
    print(">>>Plus Tools Fire!")
    return f"The answer is {n1 + n2}"


@function_tool
def sub(n1: int, n2: int) -> str:
    """
    Substract two integers and returns the result as a formatted string.

    Args:
        n1 (int): The first number.
        n2 (int): The second number.

    Returns:
        str: A string showing the substract.
    """
    print(">>>Substract Tools Fire!")
    return f"The answer is {n1 - n2}"


math_assistant = Agent(
    name="math_assistant",
    instructions="You are math assistant",
    tools=[add, sub]
)

simple_agent = Agent(
    name="Simple Assistant",
    instructions="You are helpfull assistant",
    tools=[math_assistant.as_tool(
        tool_name="math_assistant",
        tool_description=" This is a math_assistant tutor. "
    )]
)


res = Runner.run_sync(
    starting_agent=simple_agent,
    input="Please use the math_assistant to add 2 and 2.",
    run_config=config
)

rich.print(res.final_output)
# rich.print(simple_agent.tools)