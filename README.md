# Web Summarizer

A single-call LLM app: page text → prompt → model → summary -  that downloads a web page and returns a short markdown summary.
It runs fully locally with **Ollama (Gemma 3)**. To use OpenAI or another OpenAI-compatible API instead, you only edit `.env`.


## What it's for
- Getting the gist of a long page in seconds
- Quick research on a company or product before a call
- A clean example of the core LLM pipeline: **fetch → clean → prompt → model**

## Requirements
- [uv](https://docs.astral.sh/uv/) (installs Python and dependencies for you)
- [Ollama](https://ollama.com) with the model pulled: `ollama pull gemma3:4b`
  *or* an API key for OpenAI or another OpenAI-compatible provider

## Quick start
```bash
git clone https://github.com/<your-username>/web-summarizer.git
cd web-summarizer
cp .env.example .env          # Windows: copy .env.example .env
uv sync
uv run web-summarizer {website link}
```

## Configuration (`.env`)
| Variable | Default | Meaning |
|---|---|---|
| `LLM_BASE_URL` | `http://localhost:11434/v1` | API endpoint (Ollama or e.g. `https://api.openai.com/v1`) |
| `LLM_API_KEY` | `ollama` | API key (ignored by Ollama) |
| `LLM_MODEL` | `gemma3:4b` | Model name |
| `MAX_CHARS` | `6000` | Max page characters sent to the model |

## Limitations
- Sites that render content with JavaScript (single-page apps) return little or no text, because the page is downloaded, not opened in a browser.
- Long pages are cut off at `MAX_CHARS`. you can also modify it on your own in config.py file 

## License
MIT