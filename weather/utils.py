import httpx
import pandas as pd
from typing import Any

from weather.config import *

# Read city list csv
city_list_file = "assets\China-City-List-latest.csv"
df = pd.read_csv(city_list_file, skiprows=1)
df = df[["Location_Name_ZH", "Location_ID"]]

# Make requests
async def make_qweather_request(url: str) -> dict[str, Any] | None:
    """向 QWEATHER API 发送请求"""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json",
        "X-QW-Api-Key": QW_API_KEY,
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
        
def lookup_city_code(name: str) -> str:
    """根据城市中文名，查询代号"""
    result = df[df["Location_Name_ZH"] == name]
    if not result.empty:
        return result["Location_ID"].iloc[0]
    else:
        raise ValueError(f"Location not found: {name}")
    
def create_weather_string_now(location, data):
    if not data or "now" not in data or not data["now"]:
        return "Unable to fetch weather"
    
    now = data["now"]
    return f"{location}{now['text']}，温度{now['temp']}体感{now['feelsLike']}摄氏度，{now['windDir']}{now['windScale']}级，湿度{now['humidity']}%，气压{now['pressure']}hPa"