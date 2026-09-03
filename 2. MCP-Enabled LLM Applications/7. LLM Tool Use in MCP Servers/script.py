from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def call_anthropic_llm(user_query: str):
    """Call Claude with MCP tools."""
    
    print(f"\nUser: {user_query}\n")

    mcp_tools = await get_tools_from_mcp()
    
    anthropic_tools = []
    for tool in mcp_tools:
        anthropic_tool = {
            "name": tool.name,
            "description": tool.description or "",
            "input_schema": tool.inputSchema,
        }
        anthropic_tools.append(anthropic_tool)
    
    # Send the user query and formatted tools to the LLM
    client = AsyncAnthropic(api_key="<ANTHROPIC_API_TOKEN>")

    response = await client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": user_query}
        ],
        tools=anthropic_tools,
    )

    if response.stop_reason == "tool_use":
        tool_use = next(block for block in response.content if block.type == "tool_use")
        name = tool_use.name
        args = tool_use.input

        print(f"Model decided to call: {name}")
        print(f"Arguments: {args}\n")

        # Call the MCP tool
        result = await call_mcp_tool(name, args)

        # Send the result back to Claude for the final response
        followup = await client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": user_query},
                {"role": "assistant", "content": response.content},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": result,
                        }
                    ],
                },
            ],
            tools=anthropic_tools,
        )

        final_text = next((block.text for block in followup.content if block.type == "text"), None)
        if final_text:
            print(f"\nAssistant: {final_text}")
            return str(final_text)
        else:
            print("No follow-up message from model.")

    else:
        text = next((block.text for block in response.content if block.type == "text"), "")
        print(f"\nAssistant: {text}")
        return str(text)


if __name__ == "__main__":
    asyncio.run(call_anthropic_llm("How much is 250 US dollars in euros?"))
