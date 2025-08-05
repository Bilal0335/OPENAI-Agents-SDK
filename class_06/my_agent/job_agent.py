from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from user_data_type.job_data import Userdata
from my_tools.job_tools import get_experience,get_skill,recommend_job
from instruction.dynamic_job import dynamic_data


# job_agent = Agent[Userdata](
#     name="job_agent",
#     description="An agent that helps users find job recommendations based on their skills and experience.",
#     tools=[
#         get_experience,
#         get_skill,
#         recommend_job
#     ],
#     dynamic_instruction=dynamic_data,
#     dynamic_context=RunContextWrapper[Userdata],
#     user_data_type=Userdata
# )

job_recommender_agent = Agent[Userdata](
    name="job_recommender_agent",
    instructions=dynamic_data,
    model=GEMINI_MODEL,
    tools=[get_skill, get_experience, recommend_job]
)