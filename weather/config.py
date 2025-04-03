import os

# Constants
try:
    QW_API_BASE = f"https://{os.environ['QWEATHER_HOST']}/v7/weather"
except:
    raise Exception("QWEATHER_HOST is not specified")

try:
    QW_API_KEY = os.environ["QWEATHER_API_KEY"]
except:
    raise Exception("API_KEY is not specified")

USER_AGENT = "mcp-qweather/1.0"