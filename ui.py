from rich.console import Console
from rich.table import Table, box
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from datetime import datetime
import io
import sys

# Force UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

console = Console(file=sys.stdout, force_terminal=True)

def sanitize_text(text):
    if not text:
        return "No description available"
    cleaned = " ".join(text.split())
    try:
        return cleaned.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
    except:
        return cleaned[:150]

def print_header(lang: str, time: str):
    # Stylized Large Header
    title = Text("GITHUB TRENDING", style="bold bright_white")
    subtitle = Text("Terminal Dashboard v2.0", style="dim cyan")
    
    # Metadata Info
    info = Text.assemble(
        ("\nLanguage: ", "bold cyan"), (f"{lang}", "white"),
        ("  |  Timeframe: ", "bold green"), (f"{time}", "white"),
        ("  |  Status: ", "bold yellow"), ("Synced", "white")
    )

    header_content = Align.center(Text.assemble(title, "\n", subtitle, "\n", info))
    
    console.print(Panel(
        header_content,
        box=box.ROUNDED,
        border_style="bright_blue",
        padding=(1, 2)
    ))

def show_results(repos, limit: int = 10, translate: bool = False, 
                 lang_label: str = "All Languages", time_label: str = "Last 7 Days"):
    
    print_header(lang_label, time_label)

    if translate:
        console.print("[bold yellow]Translating descriptions...[/bold yellow]\n")
        from deep_translator import GoogleTranslator
        translated_repos = []
        for repo in repos:
            desc = repo.get("description") or "No description available"
            if desc and desc != "No description available":
                try:
                    desc = GoogleTranslator(source='auto', target='en').translate(desc)
                except: pass
            translated_repos.append({**repo, "description": desc})
        repos = translated_repos

    # The Table
    table = Table(
        box=box.ROUNDED,
        header_style="bold bright_white on blue",
        padding=(1, 2), # Increased padding for vertical and horizontal space
        expand=True,    # Stretch to fill the terminal width
        show_lines=True # Draw lines between rows to un-squeeze data
    )

    table.add_column("RANK & REPOSITORY", style="bold bright_cyan", ratio=3)
    table.add_column("STARS", justify="center", no_wrap=True)
    table.add_column("GITHUB URL", style="bold sky_blue1", ratio=4)
    table.add_column("DESCRIPTION / INSIGHTS", ratio=5)

    for rank, repo in enumerate(repos, start=1):
        # Format: 01. repo/name with vibrant colors
        repo_display = f"[bold cyan]{rank:02d}.[/bold cyan] [bold green]{repo['full_name']}[/bold green]"

        stars = repo["stargazers_count"]
        if stars >= 10000:
            star_display = f"🌟 [bold yellow]{stars:,}[/bold yellow]"
        else:
            star_display = f"⭐ [yellow]{stars:,}[/yellow]"

        desc = sanitize_text(repo.get("description"))

        table.add_row(
            repo_display,
            star_display,
            repo["html_url"],
            desc
        )

    console.print(table)
    print() # Final spacing