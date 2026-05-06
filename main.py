import click
from datetime import datetime, timedelta
import json
import os

from src.api import get_trending_repos
from src.ui import show_results
from src.utils import save_config, load_config, export_data

@click.group()
def cli():
    """GitHub Trending Dashboard CLI"""
    pass

@cli.command()
@click.option("--token", default="", help="GitHub Token")
@click.option("--lang", default="", help="Default Language")
@click.option("--show", is_flag=True, help="Show config")
def config(token, lang, show):
    """Configuration settings."""
    if show:
        conf = load_config()
        if not conf:
            click.echo("No configuration found.")
            return
        for k, v in conf.items():
            click.echo(f"{k}: {v}")
        return
    
    updates = {}
    if token: updates["token"] = token
    if lang: updates["default_lang"] = lang
    
    if updates:
        save_config(updates)
        click.echo("Config updated.")
    else:
        click.echo("No updates provided. Use --token or --lang.")

@cli.command()
@click.option("--days", default=7, help="Days to look back")
@click.option("--year", default=0, help="Specific year")
@click.option("--month", default=0, help="Specific month")
@click.option("--day", default=0, help="Specific day")
@click.option("--lang", default="", help="Language filter")
@click.option("--limit", default=10, help="Result limit")
@click.option("--translate", is_flag=True, help="Translate descriptions")
@click.option("--export", default="", help="Export format (csv/json)")
@click.option("--strict", is_flag=True, help="Strict language filtering (primary only)")
def fetch(days, year, month, day, lang, limit, translate, export, strict):
    """Fetch trending repos."""
    if not lang:
        lang = load_config().get("default_lang", "")

    date_query = ""
    display_label = ""

    if year > 0:
        date_query = f"{year}"
        display_label = f"year {year}"
        if month > 0:
            date_query += f"-{month:02d}"
            if day > 0:
                date_query += f"-{day:02d}"
    else:
        target_date = datetime.now() - timedelta(days=days)
        date_query = f">{target_date.strftime('%Y-%m-%d')}"
        display_label = f"the last {days} days"

    data = get_trending_repos(date_query, lang, strict=strict)

    if "error" in data:
        click.echo(f"Error: {data['error']}")
        return

    top_repos = data.get("items", [])[:limit]

    if top_repos:
        show_results(top_repos, limit, translate, lang_label=lang or "All", time_label=display_label)
        if export:
            path = export_data(top_repos, format=export.lower())
            click.echo(f"Exported to {path}")
    else:
        click.echo("No results found.")

if __name__ == "__main__":
    cli()

