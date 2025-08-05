
# ! dynamic_instr.py
from agents import RunContextWrapper, Agent

from user_data_type.user_data import UserData


# def dynamic_instruction(ctx:RunContextWrapper[UserData],agent:Agent[UserData]):
#     return f"""
#     user_name is {ctx.context.name},
#     your are helpful assistant
#     """
    
    
# ! pratice

# ! dynamic_instr.py
from agents import RunContextWrapper, Agent
from user_data_type.user_data import UserData

def dynamic_instruction(ctx: RunContextWrapper[UserData], agent: Agent[UserData]):
    if ctx.context.role == "student":
        role_msg = "You are a student who is learning new things."
    else:
        role_msg = "You are a professional focused on productivity."

    return f"""
    The user's name is {ctx.context.name}.
    The user's age is {ctx.context.age}.
    The user's role is {ctx.context.role}.

    {role_msg}
    
    You are a helpful assistant. Use this information when answering questions.
    """





# def dynamic_instruction(ctx:RunContextWrapper,agent):
#     return f"""
#     user_name is {ctx.context["user_name"]},
#     your are helpful assistant
#     """
    