
# ! ctx_tool.py

from agents import function_tool,RunContextWrapper
from user_data_type.user_data import UserData


@function_tool
def get_course(ctx:RunContextWrapper[UserData]):
    """
    Course function.
    """
    return f"Your are enrolled in the course {ctx.context.course}."

@function_tool
def get_university(ctx:RunContextWrapper[UserData]):
    """
    University function.
    """
    return f"You are studying at {ctx.context.university}."


@function_tool
def get_age(ctx: RunContextWrapper[UserData]):
    """
    Age function.
    """
    print("<-- AGE FUNCTION CALLED -->")
    print("This is a function tool that returns the age of the user.")
    print(f"ctx --> {ctx.context.name} is {ctx.context.age} years old.")
    return f"Your age is {ctx.context.age} years old."



# ! pratice
@function_tool
def get_role(ctx:RunContextWrapper[UserData]):
    """
    Role function.
    """
    print("<-- ROLE FUNCTION CALLED -->")
    print("This is a function tool that returns the role of the user.")
    print(f"ctx --> {ctx.context.name} is a {ctx.context.role}.")
    return f"Your role is {ctx.context.role}."

@function_tool
def get_user_summary(ctx: RunContextWrapper[UserData]):
    """
    User summary tool.
    """
    return (
        f"Summary:\n"
        f"Name: {ctx.context.name}\n"
        f"Age: {ctx.context.age}\n"
        f"Role: {ctx.context.role}"
    )

# @function_tool
# def get_age(ctx:RunContextWrapper):
#     """
#     Age functio.
#     """
#     print("<-- AGE FUNCTION CALLED -->")
#     print("This is a function tool that returns the age of the user.")
#     print(f"ctx --> {ctx.context["user_name"]} is {ctx.context["user_age"]} years old.")
#     return f"Your age is 20 years old."
    