from rich.console import Console
from rich.table import Table

console = Console()

def show_results(repos, limit: int = 5):
    # 1. Create the Table
    table = Table(title=f"🌟 Top {limit} Trending GitHub Repositories", show_lines=True)


    # 2. Define Columns(the headers)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Stars", style="magenta")
    table.add_column("Link", style="blue")
    table.add_column("About", style="green")
    

    # 3. Add the Data rows
    for repo in repos:
        table.add_row(
            repo["full_name"],
            str(repo["stargazers_count"]),
            repo["html_url"],
            repo["description"] or "No description available"
        )

    # 4. Print the table
    console.print(table)