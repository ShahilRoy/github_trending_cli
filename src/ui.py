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

    # Stylish Main Title (Compact ASCII Art)
    ascii_art = r"""
  ____ _ _   _           _     _____              _ _             
 / ___(_) |_| |__  _   _| |__ |_   _| __ ___ _ __   __| (_)_ __   __ _ 
| |  _| | __| '_ \| | | | '_ \  | || '__/ _ \ '_ \ / _` | | '_ \ / _` |
| |_| | | |_| | | | |_| | |_) | | || | |  __/ | | | (_| | | | | | (_| |
 \____|_|\__|_| |_|\__,_|_.__/  |_||_|  \___|_| |_|\__,_|_|_| |_|\__, |
                                                                 |___/ 
    """
    title = Text(ascii_art, style=f"bold {AMBER}")
    
    console.print(Panel(
        Align.center(title),
        box=box.DOUBLE,
        border_style=AMBER,
        padding=(0, 1),
        width=console.width
    ))

def show_results(repos, limit: int = 10, translate: bool = False, 
                 lang_label: str = "All Languages", time_label: str = "Last 7 Days"):
    
    print_header(lang_label, time_label)

    if translate:
        from deep_translator import GoogleTranslator
        translated_repos = []
        with console.status(f"[bold {AMBER}]Translating descriptions...[/bold {AMBER}]", spinner="dots"):
            for repo in repos:
                desc = repo.get("description") or "No description available"
                if desc and desc != "No description available":
                    try:
                        desc = GoogleTranslator(source='auto', target='en').translate(desc)
                    except Exception:
                        pass # Ignore translation errors
                translated_repos.append({**repo, "description": desc})
        repos = translated_repos

    if not repos:
        console.print(Panel(
            Text("No trending repositories found for the selected language and timeframe.", style=f"bold {GREY_TEXT}"),
            box=box.SQUARE,
            border_style=AMBER,
            padding=(1, 2),
            title=f"[bold {AMBER}]INFO[/bold {AMBER}]",
            title_align="left"
        ))
        console.print(f"\n[bold {GREY_TEXT}]END_OF_BUFFER // {datetime.now().strftime('%H:%M:%S')}[/bold {GREY_TEXT}]")
        return

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

    table.add_column("REPOSITORY", style=f"bold {LIGHT_AMBER}", ratio=6)
    table.add_column("STARS", justify="center", ratio=2)
    table.add_column("LANGUAGE", justify="center", style=f"bold {GREY_TEXT}", ratio=2)
    table.add_column("URL", style="bold bright_blue", ratio=8) # Brighter blue, allows wrapping
    table.add_column("ABOUT", style=f"italic {GREY_TEXT}", ratio=5)

    for rank, repo in enumerate(repos, start=1):
        # Only repo name, no owner, no icon
        repo_name = repo['full_name'].split('/')[-1].upper()
        stars = repo['stargazers_count']
        language = repo['language'] if repo['language'] else "N/A"
        
        # Shorten URL for display space
        short_url = repo['html_url'].replace("https://", "")
        
        # Rank integrated into repo name
        repo_display = Text.assemble(
            (f"{rank:02d}. ", f"bold {AMBER}"),
            (repo_name, f"bold {LIGHT_AMBER}")
        )
        
        # Exact star count with yellow color
        star_display = Text.assemble(("⭐ ", "yellow"), (f"{stars:,}", "yellow"))

        # Clickable URL (if terminal supports it)
        url_display = Text(short_url, style=f"bold bright_blue link {repo['html_url']}")

        table.add_row(
            repo_display,
            star_display,
            language,
            url_display,
            sanitize_text(repo.get('description'))
        )

    console.print(table)
    console.print(f"\n[bold {GREY_TEXT}]END_OF_BUFFER // {datetime.now().strftime('%H:%M:%S')}[/bold {GREY_TEXT}]")