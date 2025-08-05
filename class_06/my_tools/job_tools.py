from agents import RunContextWrapper, function_tool
from user_data_type.job_data import Userdata

@function_tool
def get_skill(ctx: RunContextWrapper[Userdata]) -> str:
    """
    Returns a list of the user's skills from the context.

    Args:
        ctx (RunContextWrapper[Userdata]): The user context containing user information.

    Returns:
        str: A string listing the user's skills.
    """
    return f"You have skill in {ctx.context.skills}" if ctx.context.skills else "You have no skills listed."


@function_tool
def get_experience(ctx: RunContextWrapper[Userdata]) -> str:
    """
    Returns the number of years of experience the user has.

    Args:
        ctx (RunContextWrapper[Userdata]): The user context containing user information.

    Returns:
        str: A string stating the user's years of experience.
    """
    return f"You have {ctx.context.experience_years} years of experience."


@function_tool
def recommend_job(ctx: RunContextWrapper[Userdata]) -> str:
    """
    Recommends a job based on the user's role and skills.

    Args:
        ctx (RunContextWrapper[Userdata]): The user context containing user information.

    Returns:
        str: A recommended job based on user's skills and role.
    """
    role = ctx.context.role.lower()
    skills = ctx.context.skills.lower()

    if "python" in skills and role == "developer":
        return "Recommended Job: Backend Developer at TechCorp."
    elif "design" in skills:
        return "Recommended Job: UI/UX Designer at Creatix."
    else:
        return "Recommended Job: General Analyst at DataPro."
