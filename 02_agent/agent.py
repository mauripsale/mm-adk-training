from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user lsquestions to the best of your knowledge. Search on Google if you are not sure about the answer.',
    tools=[google_search],
)
