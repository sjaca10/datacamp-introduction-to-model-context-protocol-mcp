# Add lookup_currencies(prefix): find rows where name or code contains prefix
@mcp.tool()
def lookup_currencies(prefix: str) -> str:
    """Find currencies whose code or name contains the given prefix."""
    try:
        # Use parameterized query and LIMIT 50
        cursor = conn.execute(
            "SELECT code, name FROM currencies WHERE name LIKE ? OR code LIKE ? LIMIT 50",
            (f"%{prefix}%", f"%{prefix}%")
        )
        rows = cursor.fetchall()
        return "\n".join(f"{row['code']} - {row['name']}" for row in rows)
    except sqlite3.Error as e:
        return f"Database error: {e}"

print(lookup_currencies("Euro"))
