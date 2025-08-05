import asyncio
from agents import set_tracing_disabled,OpenAIChatCompletionsModel,AsyncOpenAI,RunConfig
from dotenv import load_dotenv
import rich
import os
load_dotenv()

set_tracing_disabled(disabled=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")


if not gemini_api_key:
    raise ValueError("gemini_api_key is not set")


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-2.0-flash"
)

config = RunConfig(
    model=model,
    model_provider=external_client
)