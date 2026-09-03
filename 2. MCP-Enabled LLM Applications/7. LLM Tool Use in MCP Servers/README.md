# LLM Tool Use in MCP Servers

## Exercise

You've built an MCP server containing a tool for converting currencies using up-to-date exchange rates. Integrating it with an LLM will give it the ability to accurately answer questions about currencies and exchange rates—something it can't do by default.

The bulk of the code is provided for you here, as the main focus should be on understanding the workflow rather than syntax.

## Instructions

- Send the user query (`user_query`) and formatted list of tools (`anthropic_tools`) to Claude.
- Call the MCP tool chosen by the LLM, using the name and arguments extracted from the tool use block.
- Send the result (`result`) back to Claude for the final response.
