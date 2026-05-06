# 🚀 GitHub Trending Dashboard CLI

A professional, high-contrast terminal dashboard for tracking trending GitHub repositories. Built with Python and Rich, this CLI provides a premium interface for developers to discover what's hot in the ecosystem.

![CLI Preview](https://raw.githubusercontent.com/ShahilRoy/github_trending_cli/main/preview.png) *(Placeholder: You can add a real screenshot here later)*

## ✨ Features

- 📊 **Dynamic Dashboard**: Beautifully formatted tables with rank, stars, language, and repository info.
- 🕒 **Flexible Timeframes**: Fetch trending repos from the last X days or specific years/months.
- 🌍 **Translation**: Auto-translate repository descriptions to English using Google Translate.
- 📂 **Data Export**: Save results directly to `JSON` or `CSV` for further analysis.
- ⚙️ **Configurable**: Set default languages and GitHub tokens for higher rate limits.
- 🎨 **Premium UI**: Amber-themed dashboard with ASCII art and system status indicators.

## 🛠️ Installation

### Using Pip (Recommended)
```bash
pip install .
```

### From Source
1. Clone the repository:
   ```bash
   git clone https://github.com/ShahilRoy/github_trending_cli.git
   cd github_trending_cli
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ⌨️ Command Reference

### 🛠️ Configuration Variations
| Goal | Command |
| :--- | :--- |
| **Set GitHub Token** | `python main.py config --token ghp_your_token` |
| **Set Default Language** | `python main.py config --lang python` |
| **Set Both Token & Language** | `python main.py config --token ghp_xyz --lang rust` |
| **View Current Config** | `python main.py config --show` |

### 📊 Fetching Variations
| Goal | Command |
| :--- | :--- |
| **Quick Start** (Default 7 days) | `python main.py fetch` |
| **Limit Results** (e.g., top 5) | `python main.py fetch --limit 5` |
| **Filter by Language** (Inclusive) | `python main.py fetch --lang python` |
| **Strict Language Filter** (Primary only) | `python main.py fetch --lang python --strict` |
| **Change Timeframe** (e.g., last 30 days) | `python main.py fetch --days 30` |
| **Fetch Specific Year** | `python main.py fetch --year 2023` |
| **Fetch Specific Month** | `python main.py fetch --year 2024 --month 5` |
| **Fetch Specific Day** | `python main.py fetch --year 2024 --month 5 --day 20` |
| **Translate to English** | `python main.py fetch --translate` |
| **Export to JSON** | `python main.py fetch --export json` |
| **Export to CSV** | `python main.py fetch --export csv` |
| **Ultimate Combo** (Top 3, Rust, Translate, Export) | `python main.py fetch --limit 3 --lang rust --translate --export json` |

## 🔐 Authentication
To avoid GitHub API rate limiting, it is recommended to use a GitHub Token:
1. Generate a token at [GitHub Settings](https://github.com/settings/tokens).
2. Configure it:
   ```bash
   python main.py config --token ghp_your_token_here
   ```
   Or add it to a `.env` file: `GITHUB_TOKEN=ghp_...`

## 📄 License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

---
*Created with ❤️ by Shahil Roy*
