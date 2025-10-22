from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search


def get_weather(city: str, unit: str):
    """
    Retrieves the weather for a city in the specified unit.

    Args:
        city (str): The city name.
        unit (str): The temperature unit, either 'Celsius' or 'Fahrenheit'.
    """
    # ... function logic ...
    return {"status": "success", "report": f"Weather for {city} is sunny."}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Get the temperature unit from Google and return the weather for the requested city.',
    tools=[get_weather, google_search],
)
