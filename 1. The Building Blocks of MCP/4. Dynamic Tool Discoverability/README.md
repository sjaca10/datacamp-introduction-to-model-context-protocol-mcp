# Dynamic Tool Discoverability

## Exercise

MCP servers can house lots of functionality as separate tools, so a common first step is to list out all of the tools available to understand what they are and how they can be used.

`asyncio` has already been imported for you.

## Instructions

- Define a function called `get_tools_from_mcp()`, and start by defining the stdio server parameters so that the `"currency_server.py"` file is executed.
- Connect to the MCP server and open a session; allow *concurrent* operations and automatic session closing.
- Initialize the session.
- Return the tools available in the server.
- Return each tool's name and description (in that order) from response.
