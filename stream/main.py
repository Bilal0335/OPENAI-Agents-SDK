import asyncio
import os,chainlit as cl
from openai import AsyncOpenAI
from agents import Agent,Runner,OpenAIChatCompletionsModel,RunConfig,set_tracing_disabled
from dotenv import load_dotenv
from openai.types.responses import ResponseTextDeltaEvent


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
set_tracing_disabled(disabled=True)

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-2.5-flash"
)

config = RunConfig(
    model=model,
    model_provider=external_client
)

# agent = Agent(
#         name="Joker",
#         instructions="You are a helpful assistant.",
#         model=model
#     )

# result = Runner.run_sync(agent, input="Please tell me 5 jokes.")

# rich.print(result.final_output)

async def main():
    agent = Agent(
        name="Joker",
        instructions="You are a helpful assistant.",
        model=model
    )

    result = Runner.run_streamed(agent, input="Please tell me 25 jokes.")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())