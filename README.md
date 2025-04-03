使用和风天气API的天气查询MCP服务器，支持查询实时天气

运行时需要声明环境变量
- `QWEATHER_HOST` 你的API端点
- `QWEATHER_API_KEY` 你的API_KEY（只做了API_KEY验证，不支持JWT）

建议使用[uv](https://docs.astral.sh/uv/)运行项目

```bash
uv sync
uv run main.py
```
