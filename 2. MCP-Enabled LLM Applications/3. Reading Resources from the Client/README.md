# Reading Resources from the Client

## Exercise

Let's now take the final step: adding functionality to the client so it can read the resource's data from your MCP server! This list of currencies and their symbols could be used as a checklist by an LLM to check that the user is requesting a currency supported by the `convert_currency()` tool, and also that the tool function's arguments are valid currency symbols.

The `currency_server.py` file has been spun up and is ready for you to use.

## Instructions

- Define an async function called `read_resource()` that takes a `resource_uri` parameter of type `str`
- Inside the function, use `session.read_resource()` with `await` to read the resource at the given URI, assigning the result to `resource_content`
- Loop through the contents of each resource and print its `.mimeType` and `.text` attributes
