from google.adk.agents.llm_agent import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
import asyncio
from google.adk.agents.llm_agent import Agent
from google.genai.types import UserContent, Part
from google.genai import types # For creating message Content/Parts
from dotenv import load_dotenv
import google.generativeai as genai
import os
from google.adk.tools import google_search


load_dotenv()

# Configura l'API key di Google AI
#api_key = os.getenv("GOOGLE_API_KEY")
#if not api_key:
#    raise ValueError("GOOGLE_API_KEY non trovata nel file .env")
#genai.configure(api_key=api_key)


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[google_search],
)

session_service = InMemorySessionService()


async def main():
    runner = Runner(agent=root_agent, app_name= 'ModeApp', session_service=session_service)

    session = await session_service.create_session(app_name=runner.app_name, 
                                                   user_id="mode")

    print("Chat iniziata. Scrivi 'bye', 'quit' o 'exit' per terminare.")
    while True:
        user_input = input("Tu: ")
        if user_input.lower() in ['bye', 'quit', 'exit']:
            print("Chat terminata.")
            break

        content = UserContent(parts=[Part(text=user_input)])
        print("Gemini: ", end="", flush=True)

       
        # L'esecuzione del runner è un generatore asincrono
        async for event in runner.run_async(
            user_id=session.user_id,
            session_id=session.id,
            new_message=content,
        ):
            for part in event.content.parts:
                print(part.text, end="", flush=True)
        print("\n") # Aggiunge una nuova riga dopo la risposta completa


if __name__ == '__main__':
    asyncio.run(main())