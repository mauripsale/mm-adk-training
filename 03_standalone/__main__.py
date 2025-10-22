import asyncio
import uuid
from google.genai import types

from google.adk.agents.llm_agent import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner


APP_NAME = "weather-tutorial-app"


async def main():
    USER_ID = uuid.uuid4().hex
    SESSION_ID = uuid.uuid4().hex

    session_service = InMemorySessionService()

    _ = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    root_agent = Agent(
        model="gemini-2.5-flash",
        name="root_agent",
        description="A helpful assistant for user questions.",
        instruction="Answer user questions to the best of your knowledge",
    )

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    while True:
        query = input(">>> ")
        await call_agent_async(query, runner, USER_ID, SESSION_ID)


async def call_agent_async(query: str, runner, user_id, session_id):
    """Sends a query to the agent and prints the final response."""

    content = types.Content(role="user", parts=[types.Part(text=query)])

    final_response_text = "Agent did not produce a final response."  # Default

    async for event in runner.run_async(
        user_id=user_id, session_id=session_id, new_message=content
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_response_text = (
                    f"Agent escalated: {event.error_message or 'No specific message.'}"
                )
            break

    print(f"<<< Agent Response: {final_response_text}")


if __name__ == "__main__":
    import dotenv

    dotenv.load_dotenv()
    asyncio.run(main())
