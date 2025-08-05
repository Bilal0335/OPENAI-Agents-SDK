from agents import Agent,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled,RunConfig,Runner
from dotenv import load_dotenv
import os
import chainlit as cl
import asyncio
from typing import cast

load_dotenv()
set_tracing_disabled(disabled=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")


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
    model_provider=external_client,
    model=model,
    tracing_disabled=True
)

instructions = """
Aap aik intelligent assistant hain.

1. Agar user ka sawaal English mein ho, to jawab bhi sirf English mein dein.
2. Agar sawaal Roman Urdu ya Urdu mein ho, to jawab sirf Roman Urdu mein dein.
3. Har jawab simple, short aur aam zaban mein ho.
4. Kisi formatting, headings, ya bullet points ka istemal na karein.
"""

agent = Agent(
    name="Bilal",
    instructions=instructions,
    model=model
)

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(
        content="Welcome to the AI Assistant! How can I help you today?",
        author="AI Assistant"
    ).send()

# ! Example 03
@cl.on_message
async def handle_message(message):
    msg = cl.Message(content="Thinking...")
    await msg.send()

    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": message.content})

    res = await Runner.run(agent, message.content, run_config=config)

    history.append({"role": "assistant", "content": res.final_output})
    cl.user_session.set("history", history)

    # 🖥️ Terminal log
    print("\n========== Chat ==========")
    print(f"👤 User     : {message.content}")
    print(f"🤖 Assistant: {res.final_output}")
    print("==========================\n")

    # ⛳ Correct way to update the message
    msg.content = res.final_output
    await msg.update()
    
    
    
# ! Example 01 
# @cl.on_message
# async def handle_message(message):
#     history = cl.user_session.get("history", [])
#     history.append({"role": "user", "content": message.content})

#     print(f"\n👤 User: {message.content}")

#     res = await Runner.run(agent, message.content, run_config=config)

#     print(f"🤖 Assistant: {res.final_output}\n")

#     history.append({"role": "assistant", "content": res.final_output})
#     cl.user_session.set("history", history)

#     await cl.Message(content=res.final_output).send()

# ! Example 02
# @cl.on_message
# async def handle_message(message):

#     msg = cl.Message(content="Thinking...")
#     await msg.send()

#     history = cl.user_session.get("history", [])
#     history.append({"role": "user", "content": message.content})

#     res = await Runner.run(agent, message.content, run_config=config)

#     history.append({"role": "assistant", "content": res.final_output})
#     cl.user_session.set("history", history)

#     # 🖥️ Terminal mein chat-style display
#     print("\n========== Chat ==========")
#     print(f"👤 User     : {message.content}")
#     print(f"🤖 Assistant: {res.final_output}")
#     print("==========================\n")

#     await cl.Message(content=res.final_output).send()



