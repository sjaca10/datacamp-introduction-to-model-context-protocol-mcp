# 5. When APIs Require Authentication

## Exercise

When an external API requires an API key, the key should live in the server's environment and be attached only in the outbound request header. The client never sends or receives the key. In this exercise you will add optional API key support to the currency server's `convert_currency` tool.

The Frankfurter API does not require a key for basic use, but many APIs do. You will read an optional key from the environment (e.g., `CURRENCY_API_KEY`) and, if set, add it to the request as an `Authorization: Bearer` header.

An MCP server has already been instantiated and stored as the variable `mcp`. The `os` module has already been imported for you.

## Instructions

- Read the "`CURRENCY_API_KEY`" API key from the environment variables and add it to the `"Authorization"` header with a value `"Bearer "` plus the key to the request.
- Pass the headers in the API GET request.
