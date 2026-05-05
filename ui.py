from rich.console import Console
from rich.table import Table, box
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
from rich.align import Align
from rich.style import Style
from datetime import datetime
import sys
import io

# Force UTF-8 for better icon support
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

console = Console(force_terminal=True)

# Define our color palette based on the images
AMBER = "#FFB000"
LIGHT_AMBER = "#FFCC00"
DARK_BG = "#121212"
GREY_TEXT = "#888888"

def sanitize_text(text):
    if not text:
        return "No description available"
    cleaned = " ".join(text.split())
    return cleaned[:150]

def print_header(lang: str, time: str):
    # Top Bar: Metadata
    top_bar = Table.grid(expand=True)
    top_bar.add_column(ratio=1)
    top_bar.add_column(ratio=1)
    top_bar.add_column(ratio=1)

    lang_text = Text.assemble(("LANGUAGE\n", f"bold {GREY_TEXT}"), (f"<> {lang.upper()}", f"bold {AMBER}"))
    time_text = Text.assemble(("TIMEFRAME\n", f"bold {GREY_TEXT}"), (f"🕒 {time.upper()}", f"bold {AMBER}"))
    status_text = Text.assemble(("SYSTEM STATUS\n", f"bold {GREY_TEXT}"), ("● SYNCED_OPTIMAL", "bold green"))
    
    top_bar.add_row(lang_text, time_text, status_text)

    console.print(top_bar)
    console.print("-" * console.width, style=f"{GREY_TEXT}")

    # Stylish Main Title
    title = Text("\nGITHUB_TRENDING_CLI", style=f"bold {LIGHT_AMBER}")
    title.stylize("bold white", 0, 6) # Style "GITHUB" differently for flair
    
    console.print(Align.left(title))
    console.print(Text("―" * 20 + "\n", style=AMBER))

def show_results(repos, limit: int = 10, translate: bool = False, 
                 lang_label: str = "All Languages", time_label: str = "Last 7 Days"):
    
    print_header(lang_label, time_label)

    if translate:
        console.print(f"[bold {AMBER}]Translating descriptions...[/bold {AMBER}]\n")
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

    # Section Label
    console.print(Panel(
        Text.assemble(
            (" 📂 REPOS_ENTRY_BUFFER", f"bold {AMBER}"),
            (f" " * (max(0, console.width - 60))),
            (f"LOAD_TIME: 142ms // ENTRIES: {len(repos)}", f"bold {GREY_TEXT}")
        ),
        box=box.SQUARE,
        border_style=GREY_TEXT,
        padding=(0, 1)
    ))

    # The Data Table
    table = Table(
        box=box.ROUNDED,
        header_style=f"bold {AMBER}",
        border_style=GREY_TEXT,
        expand=True,
        show_edge=True,
        show_lines=True,
        padding=(0, 2)
    )

    table.add_column("REPOSITORY_NAME", style=f"bold {LIGHT_AMBER}", ratio=5)
    table.add_column("STARS", justify="center", ratio=2)
    table.add_column("URL_ENDPOINT", style="bold blue", ratio=4)
    table.add_column("DESCRIPTION_LOG", style=f"italic {GREY_TEXT}", ratio=6)

    for rank, repo in enumerate(repos, start=1):
        full_name = repo['full_name']
        stars = repo['stargazers_count']
        
        # Rank integrated into name: 01. REPO_NAME
        repo_display = Text.assemble(
            (f"{rank:02d}. ", f"bold {AMBER}"),
            (f"📂 {full_name.upper()}", f"bold {LIGHT_AMBER}")
        )
        
        # Exact star count with yellow color
        star_display = Text.assemble(("⭐ ", "yellow"), (f"{stars:,}", "yellow"))

        table.add_row(
            repo_display,
            star_display,
            repo['html_url'].replace("https://", ""),
            sanitize_text(repo.get('description'))
        )

    console.print(table)
    console.print(f"\n[bold {GREY_TEXT}]END_OF_BUFFER // {datetime.now().strftime('%H:%M:%S')}[/bold {GREY_TEXT}]")