from agents import Agent,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled,RunConfig,Runner
from dotenv import load_dotenv
import os
import chainlit as cl
import asyncio

load_dotenv()
set_tracing_disabled(disabled=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")


if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set")


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

@cl.on_chat_start
async def chat_start():
    await cl.Message(content="👋 Welcome! Ask me anything about coding, math, or AI.").send()


@cl.on_message
async def main(message:cl.Message):
    msg = cl.Message(content="thinking...")
    await msg.send()
    
    agent = Agent(
        name="Assistant",
        instructions="you are helpfull assistant.",
        model=OpenAIChatCompletionsModel(
            model="gemini-2.5-flash",
            openai_client=external_client
        )
    )
    res = await Runner.run(
        starting_agent=agent,
        # input="tell me about recursion programming."
        input=message.content
    )
    
    print("[bold cyan]🤖 Assistant Response:[/bold cyan]")
    print(f"{res.final_output}")
    
    # await cl.Message(content=res.final_output).send()
    msg.content=f"{res.final_output}"
    await msg.update()
    
    
    
if __name__ == "__main__":
    asyncio.run(main())