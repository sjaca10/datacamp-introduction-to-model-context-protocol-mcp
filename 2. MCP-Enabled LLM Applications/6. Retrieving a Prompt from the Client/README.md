# Retrieving a Prompt from the Client

## Exercise

Now retrieve a specific prompt from the currency server with user input so the template and the user's request are combined. This is what you would pass to an LLM before it decides whether to call the conversion tool.

## Instructions

- After initializing the session, call the method to get a prompt by name, passing the prompt name and an `arguments` dict with the user's input.
- Extract and print the text content of the first message in the prompt result.
