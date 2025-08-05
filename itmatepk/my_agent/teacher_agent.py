from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_config.groq_config import GROQ_MODEL
from my_data_type.my_data_type_schema import MathAnswer
from my_data_type.my_data_type_schema import NextJSHelp
    
math_agent_gemini = Agent(
    name="math_agent_gemini",
    instructions="You are a brilliant math tutor. Help users solve mathematical problems step by step with clear explanations.",
    model=GEMINI_MODEL,
    output_type=MathAnswer
)

nextjs_agent_groq = Agent(
    name="nextjs_agent_groq",
    instructions="You are a skilled web developer specializing in Next.js. Assist users with React, routing, APIs, and deployment.",
    model=GROQ_MODEL,
    # output_type=NextJSHelp
    # model="gemini-2.5-flash"
)
