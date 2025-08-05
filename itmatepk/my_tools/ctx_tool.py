from agents import function_tool,RunContextWrapper
from user_data_type.user_data import UserData

@function_tool
def get_age(ctx: RunContextWrapper[UserData]):
    """
    Age function.
    """
    print("<-- AGE FUNCTION CALLED -->")
    print("This is a function tool that returns the age of the user.")
    print(f"ctx --> {ctx.context.name} is {ctx.context.age} years old.")
    return f"Your age is {ctx.context.age} years old."

# @function_tool
# def get_age(ctx:RunContextWrapper):
#     """
#     Age functio.
#     """
#     print("<-- AGE FUNCTION CALLED -->")
#     print("This is a function tool that returns the age of the user.")
#     print(f"ctx --> {ctx.context["user_name"]} is {ctx.context["user_age"]} years old.")
#     return f"Your age is 20 years old."
    