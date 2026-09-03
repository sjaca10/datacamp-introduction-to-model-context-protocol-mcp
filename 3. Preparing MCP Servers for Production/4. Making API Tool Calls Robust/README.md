# Making API Tool Calls Robust

## Exercise

In production, the currency server's `convert_currency()` tool should not hang if the exchange-rate API is slow or unreachable. To mitigate this, you'll implement a **timeout** to the request and ensure any failure returns a short, clear error message to the user instead of a raw exception.

An MCP server has already been instantiated and stored as the variable `mcp`.

## Instructions

- Implement try-except logic that will attempt the API request, and gracefully fail if an error is returned by capturing the exception.
- Add a timeout of 10 seconds to the `requests.get()` call so the request does not hang indefinitely.
