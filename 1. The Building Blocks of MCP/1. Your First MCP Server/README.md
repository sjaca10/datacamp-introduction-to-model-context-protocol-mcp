# Your First MCP Server

## Exercise

Time to get hands-on with your first MCP server! **We've provided all the code for you here**, which we'll teach in the next video, but take a look at the flow of the code:

1. An MCP server instance is defined with `FastMCP()`
2. A tool function (`convert_currency()`) is written to perform some action; in this case, retrieving currency information from the [Frankfurter API](https://frankfurter.dev/).
3. This function is converted into an MCP tool using the `@mcp.tool()` decorator.

## Instructions

- Take a look at the code provided to see how a function is converted into a tool for an MCP server.
- On line **43**, test the MCP tool with an amount and your choice of currencies to convert to and from.

Note: You'll need to use the official currency codes, like GBP for the British pound sterling.
