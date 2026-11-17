# ReAct Travel Agent

A travel-planning ReAct agent built with LangChain. It looks up city facts, converts currency, searches routes (including one-stop connections), maintains a short itinerary, and answers climate questions. The first part of the notebook writes a tool’s JSON schema by hand and implements the ReAct loop explicitly, before switching to LangChain helpers (`@tool`, Pydantic `args_schema`, `StructuredTool.from_function`, and a stateful `BaseTool` subclass). Tool failures are turned into `ToolException` messages instead of crashing the agent.

The dataset is local and synthetic: **8 cities**, **19 routes**, and FX rates in `travel_data.json`. No booking or payment is performed.

## Tools

| Tool | What it does |
|---|---|
| `get_city_info` | Country, currency, time zone, average hotel price, sights |
| `convert_currency` | Convert an amount using the dataset’s rates (ISO codes) |
| `search_routes` | Direct routes by origin, destination, and transport; the description tells the model to search legs separately when there is no direct path |
| `manage_itinerary` | Stateful itinerary: add nights, show the trip, clear it, convert hotel totals to EUR |
| `get_climate` | Mean monthly temperature for a city (this is not a weather forecast) |

The system prompt also tells the agent to refuse bookings and ticket purchases, and not to treat a monthly average as a forecast.

## How to run

**Requirements:** Python 3.10+. A local [Ollama](https://ollama.com) model is the default. You can point the notebook at any OpenAI-compatible endpoint with environment variables.

```bash
# Optional, if you use the default local model:
ollama pull qwen3:8b

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

jupyter notebook react_travel_agent.ipynb
```

By default the notebook calls `http://localhost:11434/v1` with `LLM_MODEL=qwen3:8b`. The client library expects an `api_key` string; the placeholder `"ollama"` is not a real secret.

**About the saved outputs.** The traces and answers already stored in the notebook were produced with `nvidia/nemotron-3-ultra-550b-a55b:free` via OpenRouter. No API key is stored in this repository. To reproduce that run (optional):

```bash
export LLM_BASE_URL=https://openrouter.ai/api/v1
export LLM_MODEL=nvidia/nemotron-3-ultra-550b-a55b:free
export LLM_API_KEY=...   # keep this in the environment, never in the notebook
```

Then Run All. A different model may choose tools slightly differently; compare the new traces with the table below.

`scripted_llm.py` is a tiny fake chat model used in the error-handling section, so that part can be demonstrated without a live LLM.

## Results

The table is copied from the evaluation cell of `react_travel_agent.ipynb` (the saved OpenRouter run above). Eight test questions, one pass each.

| # | Question (short) | Tool calls | Repeats | Tool errors | Tools used |
|---|---|---:|---:|---:|---|
| 1 | Weather in Tbilisi in May | 1 | 0 | 0 | `get_climate` |
| 2 | Currency in Yerevan, convert 100 EUR | 2 | 0 | 0 | `get_city_info`, `convert_currency` |
| 3 | Cheapest way Kazan → Belgrade | 3 | 0 | 0 | `search_routes` ×3 |
| 4 | Itinerary: 3 nights Istanbul + 2 Belgrade, hotels in EUR | 3 | 0 | 0 | `manage_itinerary` ×3 |
| 5 | Price of a train Moscow → Dubai | 1 | 0 | 0 | `search_routes` |
| 6 | What to see in Atlantis | 1 | 0 | 1 | `get_city_info` |
| 7 | Hi, what can you do? | 0 | 0 | 0 | — |
| 8 | Book me a hotel in Dubai tomorrow | 0 | 0 | 0 | — |

Answers from that same run (also stored in `live_results.json`):

- **#1** — Tbilisi in May: mean temperature **+17 °C**.
- **#2** — Yerevan uses **AMD**; **100 EUR = 42 000 AMD** at the dataset rate.
- **#3** — No direct Kazan → Belgrade route. The agent searched legs via Istanbul and reported **Kazan → Istanbul (flight, 230 EUR) + Istanbul → Belgrade (bus, 60 EUR) = 290 EUR**.
- **#4** — Itinerary total **≈ 299.66 EUR** (Istanbul 180.00 + Belgrade 119.66).
- **#5** — Correctly reported that there is no Moscow → Dubai train. The final wording also added transport remarks that are not coming from the tools; that is a generation issue, not a wrong tool choice.
- **#6** — `get_city_info("Atlantis")` raised `ToolException`. With `handle_tool_error`, the agent said Atlantis is not in the database and listed the eight real cities, instead of crashing or inventing sights.
- **#7** — Answered from the system prompt, no tools.
- **#8** — Refused to book a hotel and offered hotel-price / climate / route help instead.

There were **no repeated** tool calls in this run. The single tool error (#6) is expected.

## Repository layout

```
react_travel_agent.ipynb   # notebook with saved traces and answers
travel_data.json           # cities, routes, FX rates
live_results.json          # snapshot of the 8-question run
scripted_llm.py            # scripted LLM for the error-handling demo
requirements.txt
```

## Note on publishing

This project started as coursework. Before you copy it into a public repository, confirm that the course allows publishing solutions. If it does not, keep the folder private, or wait until public solutions are allowed.

---

## 中文说明

这是一个用 LangChain 写的 ReAct 旅行规划 agent：可以查城市信息、换算货币、搜索路线（包括没有直达时的中转）、维护行程，并回答气候问题。笔记本里先手写了工具的 JSON schema 和 ReAct 循环，再对比 `@tool`、Pydantic schema、`StructuredTool.from_function` 和带状态的 `BaseTool` 子类。工具出错时用 `ToolException` 把错误回传给模型，而不是让 agent 崩溃。数据是本地虚构的：8 个城市、19 条路线。

**怎么运行：** `pip install -r requirements.txt`，默认连接本地 Ollama（`http://localhost:11434/v1`，`qwen3:8b`），不需要云端 key。笔记本里已经保存的那组输出，是用 OpenRouter 上的 `nvidia/nemotron-3-ultra-550b-a55b:free` 跑出来的；仓库里没有 API key。若要复现那次运行，用环境变量设置 `LLM_BASE_URL`、`LLM_MODEL` 和 `LLM_API_KEY`，不要把 key 写进笔记本。

**结果（来自笔记本保存的输出和 `live_results.json`，不是估的）：** 8 道测试题里，中转题（喀山→贝尔格莱德）找到了经伊斯坦布尔的方案，合计 **290 EUR**；行程酒店合计约 **299.66 EUR**；不存在的城市「Atlantis」触发工具错误后，agent 承认库里没有并列出了 8 个真实城市；「帮我订迪拜酒店」被拒绝。第 5 题正确说出没有莫斯科到迪拜的火车，但结尾补充了一些工具结果里没有的交通信息，属于生成阶段的问题。

公开前请确认课程是否允许发布作业解答。
