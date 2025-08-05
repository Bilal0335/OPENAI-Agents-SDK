from agents import Agent,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled,RunConfig,Runner
from dotenv import load_dotenv
import os
import chainlit as cl
from typing import cast

load_dotenv()
set_tracing_disabled(disabled=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")


if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set")

@cl.on_chat_start
async def start():
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
    
    """Set up the chat session when a user connects."""
    
    cl.user_session.set("history",[])
    cl.user_session.set('config',config)
    
    
    agent:Agent = Agent(name="Assistant", 
          instructions="You are a helpful assistant", model=model)
    
    cl.user_session.set("agent",agent)
    
    await cl.Message(content="Welcome to the Panaversity AI Assistant! How can I help you today?").send()
    
    
@cl.on_message
async def main(message:cl.Message):
    """Process incoming messages and generate responses."""
    msg = cl.Message(content="thinking...")
    await msg.send()
    
    agent:Agent = cast(Agent,cl.user_session.get("agent"))
    config:RunConfig = cast(RunConfig,cl.user_session.get("config"))
    
     # Retrieve the chat history from the session.
    history = cl.user_session.get("history") or []
    
     # Append the user's message to the history.
    history.append(
        {
            "role":"user",
            "content":message.content
        }
    )
    
    try:
        # print("\n[CALLING_AGENT_WITH_CONTEXT]\n", history, "\n")
        print("\n[🧠 Chat History Context]")
        for h in history:
            print(f"{h['role'].capitalize()}: {h['content']}")
        print("\n[🚀 Calling Agent...]\n")
        
        result = Runner.run_sync(
            starting_agent=agent,
            input=history,
            run_config=config
        )
        
        response_content = result.final_output
         # Update the thinking message with the actual response
        msg.content = response_content
        await msg.update()
        
        # Update the session with the new history.
        cl.user_session.set("history",result.to_input_list())
        
         # Optional: Log the interaction
        print(f"\n👤 User: {message.content}")
        print(f"🤖 Assistant: {response_content}\n")
    
    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"❌ Error: {str(e)}")
        
