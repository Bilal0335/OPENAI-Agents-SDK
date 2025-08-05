from agents import RunContextWrapper, Agent

from user_data_type.user_data import UserData


def dynamic_instruction(ctx:RunContextWrapper[UserData],agent:Agent[UserData]):
    return f"""
    user_name is {ctx.context.name},
    your are helpful assistant
    """
    
# def dynamic_instruction(ctx:RunContextWrapper,agent):
#     return f"""
#     user_name is {ctx.context["user_name"]},
#     your are helpful assistant
#     """
    