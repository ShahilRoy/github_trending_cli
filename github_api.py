import httpx
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv("GITHUB_TOKEN")

def get_trending_repos(date_string: str, lang: str):
    url = "https://api.github.com/search/repositories"
    headers = {"Authorization": f"token{TOKEN}"}
    params = {
        "q": f"created:>{date_string} language:{lang}",
        "sort": "stars",
        "order": "desc"
    }

    with httpx.Client() as client:
        response = client.get(url,params=params, headers=headers)
        return response.json()