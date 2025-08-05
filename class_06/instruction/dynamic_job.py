from user_data_type.job_data import Userdata
from agents import RunContextWrapper,Agent

def dynamic_data(
    ctx:RunContextWrapper[Userdata],
    agent:Agent[Userdata]
):
    return f"""
    The user's name is {ctx.context.name}.
    Age: {ctx.context.age}
    Role: {ctx.context.role}
    Skills: {ctx.context.skills}
    Experience: {ctx.context.experience_years} years

    Recommend jobs or insights based on their background. Be helpful.
    """