import typer
from datetime import datetime, timedelta

from github_api import get_trending_repos
from ui import show_results

app = typer.Typer()

@app.command("fetch")
def fetch(
    days: int = typer.Option(None, help="Number of days to look back from today."),
    year: int = typer.Option(None, help="Fetch repos from a specific year (e.g., 2022)."),
    month: int = typer.Option(None, min=1, max=12, help="Fetch repos from a specific month (1-12). Requires --year."),
    day: int = typer.Option(None, min=1, max=31, help="Fetch repos from a specific day (1-31). Requires --year and --month."),
    lang: str = typer.Option(None, help="Filter by language (e.g. python, javascript)."),
    limit: int = typer.Option(10, help="Number of repositories to display. Default is 10."),
    translate: bool = typer.Option(False, "--translate", "-t", help="Translate descriptions to English.")
):
    """Fetch trending repositories from custom dates or time ranges."""
    
    # Validation: month/day require a year
    if (month or day) and not year:
        print("Error: You must provide a --year to filter by month or day.")
        raise typer.Exit()
    if day and not month:
        print("Error: You must provide a --month to filter by day.")
        raise typer.Exit()

    date_query = ""
    display_label = ""

    # If year is provided, we build a specific date string (YYYY or YYYY-MM or YYYY-MM-DD)
    if year:
        date_query = f"{year}"
        display_label = f"year {year}"
        
        if month:
            date_query += f"-{month:02d}"
            # Get month name for better display
            month_name = datetime(year, month, 1).strftime("%B")
            display_label = f"{month_name} {year}"
            
            if day:
                date_query += f"-{day:02d}"
                display_label = f"{month_name} {day}, {year}"
    
    # If no year, but days is provided (or default to 7)
    else:
        lookback = days if days is not None else 7
        target_date = datetime.now() - timedelta(days=lookback)
        date_query = f">{target_date.strftime('%Y-%m-%d')}"
        display_label = f"the last {lookback} days"

    lang_label = lang.capitalize() if lang else "All Languages"

    # Call the API with our constructed date query
    data = get_trending_repos(date_query, lang)

    all_repos = data.get("items", [])
    top_repos = all_repos[:limit]

    if top_repos:
        show_results(top_repos, limit, translate, lang_label=lang_label, time_label=display_label)
    else:
        print(f"No trending repositories found for {display_label}.")

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        fetch()

if __name__ == "__main__":
    app()
