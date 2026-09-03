# Defining and MCP Server Prompt

## Exercise

You're adding a reusable prompt to your currency converter MCP server so that an LLM knows how to handle conversion requests and when to ask for clarification (e.g., missing amount or currency codes). This reduces prompt-load on users and makes the assistant more reliable.

An MCP server instance is already created. Add a prompt using the `@mcp.prompt()` decorator and a function that returns the prompt template with the user's request appended.

## Instructions

- Decorate a function with `@mcp.prompt()` and set the title to `"Currency Conversion"`.
- Define a function that takes `currency_request: str` and returns a string containing the prompt template and the user's request.
- Call the prompt function with a sample request and print the result to verify it works.
