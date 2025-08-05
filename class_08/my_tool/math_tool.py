
# ! my_tool/math_tool.py 
from agents import function_tool

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
    print(">>> Add Tool Fired!")
    return f"Your answer is {n1 + n2}"

@function_tool
def sub(n1: int, n2: int) -> str:
    """
    Subtracts two integers and returns the result as a formatted string.

    Args:
        n1 (int): The first number.
        n2 (int): The second number.

    Returns:
        str: A string showing the difference.
    """
    print(">>> Subtract Tool Fired!")
    return f"Your answer is {n1 - n2}"

@function_tool
def multiply(n1: int, n2: int) -> str:
    """
    Multiplies two integers and returns the result as a formatted string.

    Args:
        n1 (int): The first number.
        n2 (int): The second number.

    Returns:
        str: A string showing the product.
    """
    print(">>> Multiply Tool Fired!")
    return f"Your answer is {n1 * n2}"

@function_tool
def divide(n1:int,n2:int) -> str:
    """
    Divides two integers and returns the result as a formatted string.
    
    """
    print(">>> Divide Tool Fired!")
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return f"Your answer is {n1 / n2}"


@function_tool
def explain_math_term(term:str)->str:
    """
    Explains basic math terms.
    """
    print(">>> Explain Math Term Tool Fired!")
    explains = {
        "prime": "A prime number is only divisible by 1 and itself.",
        "lcm": "LCM stands for Least Common Multiple.",
        "gcd": "GCD stands for Greatest Common Divisor."
    }
    return explains.get(term.lower(), "Explanation not found for this term.")


@function_tool
def generate_poem(topic: str) -> str:
    """Generate a poem about the given topic."""
    return f"Here’s a basic poem about {topic}.\nRoses are red, violets are blue,\nThis is a poem for you."