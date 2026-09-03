# Building the Message and Calling the LLM

## Exercise

With your `get_context_from_mcp(user_query)` helper function created to return the resource text and prompt text, it's time to pass that information to the LLM!

The currency server, `get_context_from_mcp()`, `get_tools_from_mcp()`, `call_mcp_tool()`, and the Claude client are set up in the background. You need to complete the function that builds the prompt, calls the model, and handles either a direct message or a tool call. You've been provided with an ambiguous and an unambiguous user input to see if your MCP prompts made the difference!

## Instructions

- On **line 37**, build `full_prompt` by concatenating `prompt_text`, the string `"\n\nSupported currencies:\n"`, and `resource_text`.
- On **line 47**, send the `full_prompt` (as the user message content) and the `anthropic_tools` list to the model.
- On **lines 52-55**, if the response's `stop_reason` is `"end_turn"`, return `str(text)`.
- On **lines 58-60**, if the response's `stop_reason` is `"tool_use"`, pass the tool use block's `.name` and `.input` to `call_mcp_tool()`.
