

# ! main.py
from agents import Runner, set_tracing_disabled
from my_agent.ctx_agent import ctx_agents
import rich

from user_data_type.user_data import UserData

set_tracing_disabled(disabled=True)

user1 = UserData(
    name="Bilal",
    age=20,
    role="student",
    university="SMIU University",
    course="AI Engineering"
)


res = Runner.run_sync(
    starting_agent=ctx_agents,
    input="What is my name and univerity name? What is my age? What is my role? What is my course?",
    # context="bilal"
    # context=["Bilal","AKmal"]
    context=user1

)

rich.print(res.final_output)
