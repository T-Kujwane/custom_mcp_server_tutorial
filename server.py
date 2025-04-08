from fastmcp import FastMCP

mcp = FastMCP("Test_MCP")

@mcp.tool()
def add (a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def subtract (a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b


