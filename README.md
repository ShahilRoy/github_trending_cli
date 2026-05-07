<div align="center">

  <img src="banner.png" alt="GitHub Trending CLI Banner" width="100%" />

  # 🚀 GitHub Trending Dashboard
  
  [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
  [![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
  [![GitHub stars](https://img.shields.io/github/stars/ShahilRoy/github_trending_cli?style=social)](https://github.com/ShahilRoy/github_trending_cli)

  **A professional, terminal-based dashboard to track GitHub trends in real-time.**
  *Sleek design, powerful filtering, and seamless exports.*

  [Features](#-key-features) • [Installation](#-installation) • [Authentication](#-authentication) • [Usage](#-usage-commands) • [License](#-license)

</div>

---

## ✨ Key Features

<div align="left">

- 📊 **Dynamic Trends**: Real-time access to popular GitHub projects.
- 🕒 **Temporal Filtering**: Browse trends by day, week, or specific years (e.g., 2024).
- 🌍 **Auto-Translation**: Instant translation of non-English descriptions.
- 📂 **Flexible Exports**: Save data as `CSV` or `JSON` directly to your Downloads.
- 🎨 **Premium UI**: High-contrast, dashboard-style terminal interface.
- ⚙️ **Smart Config**: Persistent settings for your preferred languages and tokens.

</div>

---

## 🛠️ Installation

Choose your operating system to see specific instructions:

<details>
<summary><b>🪟 Windows</b></summary>
<p>

1. **Download & Extract**: 
   Download the repository as a ZIP and extract it.
2. **Open Terminal**: 
   Open **PowerShell** or **Command Prompt**.
3. **Navigate**: 
   ```powershell
   cd path/to/extracted/folder
   ```
4. **Install**:
   ```powershell
   pip install .
   ```
</p>
</details>

<details>
<summary><b>🍎 macOS</b></summary>
<p>

1. **Download & Extract**: 
   Download the ZIP and extract it to your preferred location.
2. **Open Terminal**: 
   Press `Cmd + Space` and type **Terminal**.
3. **Navigate**: 
   ```bash
   cd ~/Downloads/github_trending_cli-main
   ```
4. **Install**:
   ```bash
   pip3 install .
   ```
   *(Note: You may need to use `python3 -m pip install .` if `pip3` is not in your path)*
</p>
</details>

<details>
<summary><b>🐧 Linux</b></summary>
<p>

1. **Clone/Download**: 
   ```bash
   git clone https://github.com/ShahilRoy/github_trending_cli.git
   cd github_trending_cli
   ```
2. **Dependencies**: 
   Ensure you have Python 3 and Pip installed:
   ```bash
   sudo apt update && sudo apt install python3-pip
   ```
3. **Install**:
   ```bash
   pip3 install .
   ```
</p>
</details>

---

## 🔐 Authentication

GitHub applies rate limits to unauthenticated requests. To ensure uninterrupted service, configure a Personal Access Token (PAT).

### 1. Generate Token
1. Go to [GitHub Settings](https://github.com/settings/tokens).
2. Select **Tokens (classic)** -> **Generate new token (classic)**.
3. Name it "CLI Trends" (no specific scopes needed for trend fetching).
4. **Copy the token** immediately.

### 2. Configure CLI
Run the following command in your terminal:
```bash
gh-t config --token YOUR_GITHUB_TOKEN
```

---

## ⌨️ Usage Commands

### 🔍 Fetching Trends
| Goal | Command |
| :--- | :--- |
| **Top 10 Trending** | `gh-t fetch` |
| **Custom Limit** | `gh-t fetch --limit 5` |
| **Filter by Language** | `gh-t fetch --lang python` |
| **Strict Language Check** | `gh-t fetch --lang rust --strict` |
| **Translate Descriptions** | `gh-t fetch --translate` |

### 📅 Time-Based Trends
| Goal | Command |
| :--- | :--- |
| **Specific Year** | `gh-t fetch --year 2023` |
| **Last N Days** | `gh-t fetch --days 30` |

### 💾 Data Export
| Goal | Command |
| :--- | :--- |
| **Export to CSV** | `gh-t fetch --export csv` |
| **Export to JSON** | `gh-t fetch --export json` |

### ⚙️ Persistent Configuration
| Goal | Command |
| :--- | :--- |
| **Set Default Language** | `gh-t config --lang javascript` |
| **View Current Config** | `gh-t config --show` |

---

## 📄 License
This project is free to use and modify, but it must **always remain free** for everyone. It is protected by the **GNU General Public License v3.0**.

---
*Created with ❤️ by Shahil Roy*
