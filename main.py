import typer
from datetime import datetime, timedelta

def get_date_string(days: int):
    # Calculate 'X' days ago
    target_date = datetime.now() - timedelta(days=days)
    # Format it like 2026-05-04
    return target_date.strftime("%Y-%m-%d")

app = typer.Typer()

@app.command("fetch")
def fetch(days: int = 7):
    """Fetch trending repositories."""
    # This calls the get_date_string function to get the date string
    date_str = get_date_string(days)
    
    print(f"Checking GitHub for trending repositories since {date_str} days... 🔍")
    
@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print("No command provided, defaulting to fetch...")
        fetch()
if __name__ == "__main__":
    app()