import typer
from datetime import datetime, timedelta

from github_api import get_trending_repos

def get_date_string(days: int):
    # Calculate 'X' days ago
    target_date = datetime.now() - timedelta(days=days)
    # Format it like 2026-05-04
    return target_date.strftime("%Y-%m-%d")

app = typer.Typer()

@app.command("fetch")
def fetch(days: int = 7, lang: str = "python"):
    """Fetch trending repositories."""
    # This calls the get_date_string function to get the date string
    date_string = get_date_string(days)
    
    print(f"Checking GitHub for trending {lang} repositories since {date_string} days... 🔍")

    # Call the function and store the response
    data = get_trending_repos(date_string, lang)

    all_repos = data.get("items", [])

    top_repos = all_repos[:5]

    if top_repos:
        first_one = top_repos[0]
        print(f"Top repo name:{first_one['full_name']}")
        print(f"Stars:{first_one['stargazers_count']}")


    print(data)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print("No command provided, defaulting to fetch...")
        fetch()

if __name__ == "__main__":
    app()

