import argparse                            
import sys                                
import requests                            

from web_summarizer import config
from web_summarizer.scraper import fetch_text
from web_summarizer.llm import summarize_text


def main() -> None:                    
    parser = argparse.ArgumentParser(description="Summarize any website with a local or cloud LLM.")
    parser.add_argument("url", help="Website URL to summarize")   
    args = parser.parse_args()            # read what the user typed

    try:                                   # Java: try
        page = fetch_text(args.url, config.MAX_CHARS)
    except requests.RequestException as e: 
        print(f"Could not fetch {args.url}: {e}", file=sys.stderr)  
        sys.exit(1)                        

    print(summarize_text(page))            # summarize and print


if __name__ == "__main__":                 # allows running this file directly too
    main()