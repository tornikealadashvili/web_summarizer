import requests                           
from bs4 import BeautifulSoup            

NOISE_TAGS = ["script", "style", "nav", "footer", "img", "input"]   # tags that waste tokens


def fetch_text(url: str, max_chars: int) -> str: #func that is reponsible for getting the text from the url and returning it as a string in response
    resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})  # download raw HTML
    resp.raise_for_status()                # throw on 404/500
    soup = BeautifulSoup(resp.text, "html.parser")   # parse into a tag tree
    for tag in soup(NOISE_TAGS):           
        tag.decompose()                    #noise tags are removed from the tree
    title = soup.title.string if soup.title else "No title"   # page title or fallback
    text = soup.get_text(separator="\n", strip=True)          # visible text only
    return f"{title}\n\n{text[:max_chars]}"                   # cap the length