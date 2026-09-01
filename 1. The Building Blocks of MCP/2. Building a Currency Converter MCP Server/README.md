# Building a Currency Converter MCP Server

## Exercise

Time to begin building your first MCP server! Here, you'll define an MCP server called `'Currency Converter'` that consists of a single tool called `convert_currency()` to convert monetary values between different currencies.

This tool should take `amount`, `from_currency`, and `to_currency` parameters, and return a string containing the amount converted into the desired currency, along with the exchange rate used.

For example, `100 EUR = 88.04 GBP (Rate: 0.8804)`.

## Instructions

- Instantiate an MCP server called `"Currency Converter"`.
- Create an MCP tool called `convert_currency()` that takes `amount`, `from_currency`, and `to_currency` arguments.
- Complete the API endpoint URL by setting the `base` and `symbols` query parameters to `from_currency` and `to_currency`, respectively.
- Send a GET request to the `url`, extract the JSON from the response object, and calculate `converted_amount` by multiplying `amount` by `rate`.
