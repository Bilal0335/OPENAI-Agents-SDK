from agents import OpenAIChatCompletionsModel,AsyncOpenAI
from decouple import config

key = config("GEMINI_API_KEY")
base_url = config("BASE_URL_GEMINI")

gemini_client = AsyncOpenAI(
    api_key=key,
    base_url=base_url
)

GEMINI_MODEL = OpenAIChatCompletionsModel(
    openai_client=gemini_client,
    model="gemini-2.5-flash"
)

