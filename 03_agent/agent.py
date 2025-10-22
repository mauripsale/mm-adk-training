from google.adk.agents.llm_agent import Agent

def get_weather(city: str):
    """
    Retrieves the weather for a city

    Args:
        city (str): The city name.
    """
    return {"status": "success", "report": f"Il meteo a {city} è Reggiano."}


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge, when the question is about the weather use the tool',
    tools=[get_weather]
)

