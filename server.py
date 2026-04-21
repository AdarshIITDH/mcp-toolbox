from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AdderServer")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

def main():
    # Default direct execution works well for a stdio-based MCP server,
    # which is exactly what mcpo expects to wrap.
    mcp.run()

if __name__ == "__main__":
    main()
