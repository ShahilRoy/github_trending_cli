import httpx
import os
from dotenv import load_dotenv
from .utils import load_config

load_dotenv()

def get_trending_repos(date_string: str, lang: str = None, strict: bool = False):
    # 1. Check Config/Env for Token
    config = load_config()
    TOKEN = config.get("token") or os.getenv("GITHUB_TOKEN")

    url = "https://api.github.com/search/repositories"
    headers = {}
    if TOKEN:
        headers["Authorization"] = f"token {TOKEN}"

    query = f"created:{date_string}"
    if lang:
        if strict:
            # Matches ONLY repos where this is the PRIMARY language
            query += f" language:{lang}"
        else:
            # Matches any repo where language is mentioned (inclusive)
            query = f"{lang} {query}"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }

    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(url, headers=headers, params=params)
            
            if response.status_code == 401:
                return {"error": "Invalid GitHub Token."}
            elif response.status_code == 403:
                return {"error": "Rate limit exceeded."}

            response.raise_for_status()
            return response.json()
    
    except Exception as exc:
        return {"error": str(exc)}

    return {}