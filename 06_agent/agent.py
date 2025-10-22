import os
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

google_maps_api_key = "AIzaSyCo1XTVmGKZv7yXEBZ_ZVttop6Z5s5kq4I"


root_agent = Agent(
    model='gemini-2.0-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Help the user with mapping, directions, and finding places using Google Maps tools.. Rispondi in modo aulico ed elegante. rimani però fedele alla strada, tu sei nato povero ma ora sei borghese, non dimenticarlo mai.',
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params = StdioServerParameters(
                    command='npx',
                    args=[
                        "-y",
                        "@modelcontextprotocol/server-google-maps",
                    ],
                    # Pass the API key as an environment variable to the npx process
                    # This is how the MCP server for Google Maps expects the key.
                    env={
                        "GOOGLE_MAPS_API_KEY": google_maps_api_key
                    }
                ),
            ),
            # You can filter for specific Maps tools if needed:
            # tool_filter=['get_directions', 'find_place_by_id']
        )
    ],  
)



