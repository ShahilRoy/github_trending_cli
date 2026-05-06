import json
import os
import csv
from datetime import datetime

CONFIG_FILE = ".trending_config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

def save_config(config):
    current = load_config()
    current.update(config)
    with open(CONFIG_FILE, "w") as f:
        json.dump(current, f, indent=4)

def export_data(repos, format="json", filename=None):
    from pathlib import Path
    
    # Target the user's Downloads folder
    downloads_path = Path.home() / "Downloads"
    
    if not filename:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"github_trending_{timestamp}.{format}"
    
    # Combine with Downloads path
    full_path = downloads_path / filename
    
    if format == "json":
        with open(full_path, "w", encoding="utf-8") as f:
            json.dump(repos, f, indent=4, ensure_ascii=False)
    elif format == "csv":
        keys = ["rank", "name", "stars", "language", "url", "description"]
        with open(full_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for i, repo in enumerate(repos, 1):
                writer.writerow({
                    "rank": i,
                    "name": repo.get("full_name"),
                    "stars": repo.get("stargazers_count"),
                    "language": repo.get("language") or "N/A",
                    "url": repo.get("html_url"),
                    "description": repo.get("description")
                })
    return str(full_path)
