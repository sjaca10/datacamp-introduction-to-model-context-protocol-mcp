# Defining MCP Server Resources

## Exercise

You're expanding your MCP server for currency conversion to give it access to the list of currencies supported by the API you're using. The European Central Bank publishes a list of currency codes in a file called `currencies.txt` that is available in your server directory. This could be used by the client to ensure that the LLM is passing the correct argument values to the tool functions.

Your task is to define an MCP resource called `get_currencies()` that reads the contents of `currencies.txt`.

## Instructions

- Use the correct decorator and the `"file://currencies.txt"` URI to convert the `get_currencies()` function into a resource.
- Complete the `get_currencies()` function to open and read the contents of the `currencies.txt` file.
- Print the result of calling `get_currencies()` to verify the resource works correctly.
