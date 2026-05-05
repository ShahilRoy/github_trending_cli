import httpx
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

def get_trending_repos(date_string: str, lang: str = None):

    url = "https://api.github.com/search/repositories"
    headers = {}
    if TOKEN:
        headers["Authorization"] = f"token {TOKEN}"
    else:
        print("Warning: No GITHUB_TOKEN found. Rate limits will be strictly enforced.")
        pass

    # Use the flexible date_string directly in the query
    query = f"created:{date_string}"
    if lang:
        query += f" language:{lang}"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }

    try:
        # Added a 10-second timeout to prevent the app from hanging
        with httpx.Client(timeout=10.0) as client:
            response = client.get(url, headers=headers, params=params)
            
            if response.status_code == 401:
                print("Error: Invalid GitHub Token. Please check your .env file.")
                return {}
            elif response.status_code == 403:
                print("Error: Rate limit exceeded. Please wait a while before trying again or use a GitHub Token.")
                return {}

            response.raise_for_status()
            return response.json()
    
    except httpx.ConnectError:
        print("Error: Could not connect to GitHub. Please check your internet connection.")
    except httpx.TimeoutException:
        print("Error: Request timed out. Please try again later.")
    except httpx.HTTPStatusError as exc:
        print(f"HTTP Error occurred: {exc.response.status_code} - {exc.response.text}")
    except Exception as exc:
        print(f"An unexpected error occurred: {exc}") 


    return {} # Return an empty dictionary if the request fails