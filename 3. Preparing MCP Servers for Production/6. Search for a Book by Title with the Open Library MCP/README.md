# Search for a Book by Title with the Open Library MCP

## Exercise

The Open Library MCP exposes tools that query the Internet Archive's Open Library API. In this exercise you will connect to the server, initialize a session, and use the `get_book_by_title` tool to search for a book and print the result.

Because of the unique setup of DataCamp exercises, the `command` and `args` set in `StdioServerParameters()` differ from those shown in the video and what you would use locally, but the principle is the same: the server is being spun up from the installed source files.

## Instructions

- Call the `get_book_by_title` tool to search for book titles containing `"AI"` and assign the result to result.
- Assign the result text from `result.content[0].text` to `text` and print it.
