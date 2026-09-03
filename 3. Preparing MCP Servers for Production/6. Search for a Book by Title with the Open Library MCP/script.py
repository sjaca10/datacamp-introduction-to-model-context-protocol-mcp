from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(command=OPEN_LIBRARY_SERVER_CMD, args=OPEN_LIBRARY_SERVER_ARGS)
    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call get_book_by_title for "AI" and assign the result
            result = await session.call_tool("get_book_by_title", {"title": "AI"})
            # Assign the result text and print it
            text = result.content[0].text
            print(text)

asyncio.run(main())
