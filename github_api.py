import httpx
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv("GITHUB_TOKEN")

def get_trending_repos(date_string: str, lang: str = None):
    url = "https://api.github.com/search/repositories"
    headers = {"Authorization": f"token {TOKEN}"}

    # Only filter by language if one is specified
    query = f"created:>{date_string}"
    if lang:
        query += f" language:{lang}"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }

    with httpx.Client() as client:
        response = client.get(url,params=params, headers=headers)
        return response.json()