import asyncio
from agents import Agent,Runner,set_tracing_disabled,OpenAIChatCompletionsModel,AsyncOpenAI,RunConfig
from dotenv import load_dotenv
import rich
import os
load_dotenv()

set_tracing_disabled(disabled=True)
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")


if not openrouter_api_key:
    raise ValueError("openrouter_api_key is not set")


external_client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1"
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="qwen/qwen3-coder:free"
)

simple_agent = Agent(
    name="simple_agent",
    instructions="You are helpfull assitant.",
    model=model
)

async def main():
    res = Runner.run_streamed(
        simple_agent,
        "hi"
    )
    async for event in res.stream_events():
        rich.print(event.type)
        
asyncio.run(main())