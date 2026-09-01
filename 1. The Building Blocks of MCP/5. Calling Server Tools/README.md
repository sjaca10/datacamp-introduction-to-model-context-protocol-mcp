# Calling Server Tools

## Exercise

Now to trigger tool calls in the server from your client! Again, you'll be using asynchronous operations to ensure that nothing breaks or freezes while waiting for other operations to complete.

## Instructions

- Call the tool with the `tool_name` and `arguments` parameters specified by the user; ensure that the call pauses to wait for the server to respond using the appropriate Python keyword.
- Extract and print the text content of the server response.
- Run the `"convert_currency"` tool with a set of valid parameters (use whatever values and currencies you wish here).
