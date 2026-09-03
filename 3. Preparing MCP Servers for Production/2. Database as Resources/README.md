# Database as Resources

## Exercise

Now to take that database information and make it available as a resource in the MCP server. This can be used downstream to validate that the LLM is requesting supported currency codes, or even in the user interface to make the currency code a dropdown or autocomplete selection.

The database is still available as `currencies.db`, and the code to instantiate a server has been provided for you.

## Instructions

- Establish a connection to the database (`currencies.db`).
- Create a new MCP server resource for the database connection.
- Execute the database query so that the `get_currencies()` function returns the database's contents.
