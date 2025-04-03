from weather.server import mcp
        
if __name__ == "__main__":
    # Initialize and run the server
    print("Starting MCP server")
    mcp.run(transport="stdio")
