from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Currency Converter")

# Connect to the database on startup
conn = sqlite3.connect("currencies.db")
conn.row_factory = sqlite3.Row

# Create an MCP resource
@mcp.resource("db://currencies")
def get_currencies() -> str:
    """
    Get the list of currency names published by the European Central Bank for currency conversion.

    Returns:
        One line per currency (code - name), from the database.
    """
    try:
        # Query the database
        cursor = conn.execute("SELECT code, name FROM currencies")
        rows = cursor.fetchall()
        return "\n".join(f"{row['code']} - {row['name']}" for row in rows)
    except sqlite3.Error as e: return f"Error: {e}"

result = get_currencies()
print(result[:200] + "..." if len(result) > 200 else result)
