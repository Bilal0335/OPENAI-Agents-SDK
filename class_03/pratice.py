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
        model="gemini-2.0-flash",
        openai_client=external_client
    )
    
    config = RunConfig(
        model=model,
        model_provider=external_client
    )
    
    cl.user_session.set("histor",[])
    cl.user_session.set("config",config)
    
    frontend_agent = Agent(
        name="FrontendDev",
        instructions="You are a frontend expert. Help only with HTML, CSS, JS, React, etc.",
        model=model
    )

    backend_agent = Agent(
        name="BackendDev",
        instructions="You are a backend expert. Answer only FastAPI, Django, DBs, Auth, etc.",
        model=model
    )

    career_agent = Agent(
        name="CareerCoach",
        instructions="You are a career coach. Guide on resumes, interviews, and learning paths.",
        model=model
    )
    
    cl.user_session.set("frontend_agent",frontend_agent)
    cl.user_session.set("backend_agent",backend_agent)
    cl.user_session.set("career_agent",career_agent)
    
    cl.Message(content="Welcome! Ask anything about frontend, backend, or career.").send()
    
    
@cl.on_message
async def main(message:cl.Message):
    msg = cl.Message(content="Thinking...")
    await msg.send()
    
    config:RunConfig = cast(RunConfig,cl.user_session.get("config"))
    history = cl.user_session.get("history") or []
    
    user_input = message.content.lower()
    if "html" in user_input or "css" in user_input or "react" in user_input:
        agent = cast(Agent, cl.user_session.get("frontend_agent"))
    elif "api" in user_input or "database" in user_input or "auth" in user_input:
        agent = cast(Agent, cl.user_session.get("backend_agent"))
    elif "resume" in user_input or "career" in user_input or "job" in user_input:
        agent = cast(Agent, cl.user_session.get("career_agent"))
    else:
        # Default fallback agent (frontend for now)
        agent = cast(Agent, cl.user_session.get("frontend_agent"))

    history.append(
        {
            "role":"user",
            "content":user_input,
        }
    )
    
    try:
        result = Runner.run_sync(
            starting_agent=agent,
            input=history,
            run_config=config
        )
        
        response_content = result.final_output
        msg.content = response_content
        await msg.update()
        
        cl.user_session.set("history",result.to_input_list())
        
        print("\n========== Chat ==========")
        print(f"👤 User: {message.content}\n")
        print(f"🤖 Assistant ({agent.name}): {response_content}")
        print("==========================\n")
        
    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"❌ Error: {str(e)}")
        
        