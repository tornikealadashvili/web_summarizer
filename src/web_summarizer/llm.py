from openai import OpenAI                                  # client which will be used
from web_summarizer import config                          # configs from config.py
from web_summarizer.prompts import SYSTEM_PROMPT, build_user_prompt   # prompts from prompts.py

_client = OpenAI(                         
    base_url=config.BASE_URL,
    api_key=config.API_KEY,
    timeout=300,                           
    max_retries=0,                         
)


def summarize_text(page_text: str) -> str:   # clean text in -> summary out
    response = _client.chat.completions.create(
        model=config.MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(page_text)},
        ],
    )
    return response.choices[0].message.content   # the summary text