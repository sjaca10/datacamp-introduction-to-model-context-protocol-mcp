# Listing Prompts from the Client

## Exercise

Your currency server has been written to `currency_server.py` with a tool, a resource, and a prompt. Create a client that lists the prompts available on this server so you can discover what prompt templates the LLM can use.

## Instructions

- Connect to the MCP server, initialize the session, and call the method that lists available prompts, assigning the result to a variable.
- Print each prompt's name (the function name from the server, not the title).
