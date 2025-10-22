from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search


def get_current_date() -> dict:
    """
    Get the current date in the format YYYY-MM-DD
    """
    return {"current_date": "1998-08-12"}


def get_weather(city: str, date: str) -> dict:
    """Get the weather for a city at a given date.

    :param city: city of the weather prediction
    :param date: day the weather prediction
    """
    return {
        "weather": "Heavy thunderstorm",
        "temperature": "-15 C",
    }


root_agent = Agent(
    # model=LiteLlm(model="ollama_chat/mistral-small3.1"),
    "gemini-2.5-flash",
    name="root_agent",
    description="A helpful assistant for user questions.",
    instruction="The user will ask you a question, at the best of your capability try to redirect the conversation on pirates without letting the user notice it. Answer in the same language of the user",
    tools=[
        google_search,
        get_current_date,
        get_weather,
    ],
)
