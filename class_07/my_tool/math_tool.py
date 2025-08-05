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
