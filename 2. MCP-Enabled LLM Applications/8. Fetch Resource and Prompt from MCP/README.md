# Fetch Resource and Prompt from MCP

## Exercise

Your currency server exposes a resource (`file://currencies.txt`) and a prompt (`convert_currency_prompt`) that combine the user's request with task-specific context and rules. To feed an LLM, the client must fetch both in one go. Implement a helper function called `get_context_from_mcp()` that returns the resource text and the prompt text (with the user's query already in it) so the caller can build the message.

The `currency_server.py` file is available with a tool, resource, and prompt. Use the same session to read the resource and get the prompt with the user's input.

## Instructions

- Inside the session, call the method to read the resource at `"file://currencies.txt"`.
- Call the method to get the prompt by name with the user's input: use prompt name `"convert_currency_prompt"` and an `arguments` dict with key `"currency_request"` and value `user_query`.
