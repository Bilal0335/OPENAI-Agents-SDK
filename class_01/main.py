from agents import Agent,Runner,AsyncOpenAI,RunConfig,OpenAIChatCompletionsModel,set_tracing_disabled
from dotenv import load_dotenv
import os 
import chainlit as cl
import asyncio
from rich import print

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
set_tracing_disabled(disabled=True)

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set")


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


@cl.on_message
async def main(message:cl.Message):
    msg = cl.Message(content="Thinking...")
    await msg.send()
    
    agent = Agent(
        name="agent",
        instructions="You are exper math_professor.",
        model=OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=external_client
        )
    )
    res = await Runner.run(
        starting_agent=agent,
        input=message.content,
    )
    print("[bold cyan]🤖 Assistant Response:[/bold cyan]")
    print(f"{res.final_output}")
    
    # await cl.Message(content=res.final_output).send()
    msg.content=f"{res.final_output}"
    await msg.update()
    
    

# async def main():
#     math_professor = Agent(
#         name="math_professor",
#         instructions="You are exper math_professor.",
#         model=OpenAIChatCompletionsModel(
#             model="gemini-2.0-flash",
#             openai_client=external_client
#         )
#     )
    
#     res = await Runner.run(
#         starting_agent=math_professor,
#         input="what is parabola?",
#     )
#     print("[bold cyan]🤖 Assistant Response:[/bold cyan]")
#     print(f"{res.final_output}")
    
    
    
if __name__ == "__main__":
    asyncio.run(main())
    