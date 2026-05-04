import typer
from datetime import datetime, timedelta

from github_api import get_trending_repos

from ui import show_results

def get_date_string(days: int):
    # Calculate 'X' days ago
    target_date = datetime.now() - timedelta(days=days)
    # Format it like 2026-05-04
    return target_date.strftime("%Y-%m-%d")

app = typer.Typer()

@app.command("fetch")
def fetch(
    days: int = typer.Option(7, help="Number of days to look back."),
    lang: str = typer.Option(None, help="Filter by language (e.g. python, javascript). Leave empty for all languages."),
    limit: int = typer.Option(5, help="Number of repositories to display. Default is 5.")
):
    """Fetch trending repositories."""
    # This calls the get_date_string function to get the date string
    date_string = get_date_string(days)

    lang_label = lang if lang else "all languages"
    print(f"Checking GitHub for trending [{lang_label}] repositories since {date_string}... 🔍")

    # Call the function and store the response
    data = get_trending_repos(date_string, lang)

    all_repos = data.get("items", [])

    top_repos = all_repos[:limit]

    if top_repos:
        show_results(top_repos, limit)
    else:
        print("No trending repositories found.")
        

    # print(data)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print("No command provided, defaulting to fetch...")
        fetch()

if __name__ == "__main__":
    app()

