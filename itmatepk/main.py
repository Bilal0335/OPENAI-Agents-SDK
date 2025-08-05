# from agents import Runner, set_tracing_disabled,RunConfig,set_default_openai_api,set_default_openai_client

# from my_agent.teacher_agent import math_agent_gemini, nextjs_agent_groq

# from my_config.gemini_config import GEMINI_MODEL,gemini_client

# import rich

# set_default_openai_client(gemini_client)
# set_default_openai_api("chat_completions")

# set_tracing_disabled(disabled=True)

# # Math agent test
# result = Runner.run_sync(starting_agent=nextjs_agent_groq, input="What is the power of 2?",run_config=RunConfig(model=GEMINI_MODEL,model_provider=gemini_client))
# rich.print("📘 [bold green]Math Agent Response:[/bold green]")
# rich.print(result.final_output)

# print("---" * 13)

# # Next.js agent test
# # result = Runner.run_sync(starting_agent=nextjs_agent_groq, input="How do I fetch data using getServerSideProps in Next.js?")
# # rich.print("🧠 [bold blue]Next.js Agent Response:[/bold blue]")
# # rich.print(result.final_output)
# # print("---" * 13)


# !-------------------------------------

from agents import Runner, set_tracing_disabled
from my_agent.teacher_agent import math_agent_gemini, nextjs_agent_groq
from my_config.gemini_config import GEMINI_MODEL, gemini_client
from my_config.groq_config import GROQ_MODEL, groq_client
import rich

# Disable tracing logs
set_tracing_disabled(disabled=True)

# ✅ Math agent test
print("---" * 13)
math_result = Runner.run_sync(starting_agent=math_agent_gemini, input="What is the derivative of x^2?")
rich.print("🧮 [bold green]Math Agent Output:[/bold green]")
rich.print(math_result.final_output)

print("---" * 13)

# ✅ Next.js agent test
nextjs_result = Runner.run_sync(starting_agent=nextjs_agent_groq, input="What is Next.js?")
rich.print("🌐 [bold blue]Next.js Agent Output:[/bold blue]")
rich.print(nextjs_result.final_output)

print("---" * 13)

# !-------------------------------------

# You are a skilled Next.js developer. Return the topic, explanation, and a code sample.