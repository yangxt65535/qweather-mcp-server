
from mcp.server.fastmcp import FastMCP

from weather.config import *
from weather.utils import lookup_city_code, make_qweather_request, create_weather_string_now

# Initialize FastMCP server
mcp = FastMCP("qweather")

@mcp.tool()
async def get_weather_now(location: str):
    """Get the weather of a place for the moment

    Args:
        location: the name of province, city or district
    """
    try:
        location_code = lookup_city_code(location)
    except ValueError as e:
        return(str(e))
 
    url = f"{QW_API_BASE}/now?location={location_code}"
    data = await make_qweather_request(url)

    return create_weather_string_now(location, data)

@mcp.tool()
async def get_weather_day(location: str, day: int):
    """Get the weather of a place for the following consecutive days.

    Args:
        location: the name of province, city or district
        day: number of days, supported: 3/7/10/15/30 days
    """
    try:
        location_code = lookup_city_code(location)
    except ValueError as e:
        return(str(e))
 
    url = f"{QW_API_BASE}/{day}d?location={location_code}"
    data = await make_qweather_request(url)

    if not data or "daily" not in data or not data["daily"]:
        return "Unable to fetch weather"
    
    return str(data["daily"])