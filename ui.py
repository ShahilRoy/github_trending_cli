from rich.console import Console
from rich.table import Table
import sys
from deep_translator import GoogleTranslator

console = Console()

def sanitize_text(text):
    """Sanitize text to prevent UnicodeEncodeError on some Windows terminals."""
    if not text:
        return "No description available"
    try:
        # Encode and decode using the terminal's encoding to strip non-displayable characters
        return text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
    except:
        return "Description contains incompatible characters"

def show_results(repos, limit: int = 10, translate: bool = False):
    # 1. Create the Table
    title = f"Top {limit} Trending GitHub Repositories"
    if translate:
        title += " (Translated to English)"
    
    table = Table(title=title, show_lines=True)

    # 2. Define Columns (the headers)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Stars", style="magenta")
    table.add_column("Link", style="blue")
    table.add_column("About", style="green")

    # 3. Add the Data rows
    if translate:
        console.print("[yellow]Translating descriptions to English... (this may take a few seconds)[/yellow]")

    for repo in repos:
        description = repo["description"] or "No description available"
        
        # Translate if requested
        if translate and description and description != "No description available":
            try:
                # 'auto' detects the source language automatically
                description = GoogleTranslator(source='auto', target='en').translate(description)
            except Exception as e:
                # If translation fails, just keep the original (but sanitized)
                pass
        
        # Sanitize the final text to prevent terminal crashes
        description = sanitize_text(description)
        
        # Color code stars: make huge repos (10k+) stand out in yellow
        stars = repo["stargazers_count"]
        star_style = "yellow" if stars >= 10000 else "magenta"
        
        table.add_row(
            repo["full_name"],
            f"[{star_style}]{stars}[/{star_style}]",
            repo["html_url"],
            description
        )

    # 4. Print the table
    console.print(table)