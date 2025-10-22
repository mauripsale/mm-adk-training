from agent import root_agent
from google.adk.runners import InMemoryRunner
from google.genai.types import UserContent, Part
from dotenv import load_dotenv
import asyncio

load_dotenv()

runner = InMemoryRunner(agent=root_agent)
async def main():
    session = await runner.session_service.create_session(
        app_name=runner.app_name,
        user_id="test_user",
    )
    print("Chat iniziata. Scrivi 'bye', 'quit' o 'exit' per terminare.")

async def runner_main():
    # La creazione della sessione è asincrona e va fatta qui
    session = await runner.session_service.create_session(
        app_name=runner.app_name,
        user_id="test_user"
    )
    print("Chat iniziata. Scrivi 'bye', 'quit' o 'exit' per terminare.")

    while True:
        user_input = input("Prompt: ")
        if user_input.lower() in ["bye", "quit", "exit"]:
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
            if event.is_final_response():
                print(f"IsFinal {event.is_final_response()}")
                for part in event.content.parts:
                    print(part.text, end="", flush=True)
        print("\n") # Aggiunge una nuova riga dopo la risposta completa