# 🚀 GitHub Trending Dashboard

This tool lets you see what projects are popular on GitHub right now, directly from your computer terminal. It's designed to look great and be very easy to use.

---

## ✨ What can this tool do?

- 📊 **See Trends**: Shows a beautiful table of the top trending projects.
- 🕒 **Choose Time**: Look at trends from today, this week, or even a specific year like 2023.
- 🌍 **Translate**: If a project description is in a different language, it can translate it to English for you.
- 📂 **Save Results**: You can save the list to your **Downloads** folder as a file (JSON or CSV).
- 🎨 **Looks Cool**: It uses high-contrast colors and a professional "dashboard" style.

---

## 🛠️ How to Install (For Beginners)

If you are new to this, just follow these steps:

1. **Download the code**: 
   Click the green "Code" button at the top of this GitHub page and select "Download ZIP". Extract the folder once it's downloaded.
2. **Open your Terminal**:
   On Windows, search for "CMD" or "PowerShell". On Mac, search for "Terminal".
3. **Go to the folder**:
   Type `cd` followed by a space, then drag the folder into the terminal window and press Enter.
4. **Install the tool**:
   Type this and press Enter:
   ```bash
   pip install .
   ```

---

## 🔐 How to get your GitHub Token (Crucial)

GitHub limits how many times you can ask for data if you don't have a "Token". If you see a "Rate Limit" error, you need a token. Here is exactly how to get one:

1. Log in to your [GitHub account](https://github.com/).
2. Click your **Profile Picture** (top right) -> **Settings**.
3. Scroll all the way down on the left and click **Developer settings**.
4. Click **Personal access tokens** -> **Tokens (classic)**.
5. Click **Generate new token** -> **Generate new token (classic)**.
6. Give it a name (like "My CLI Tool").
7. **Important**: You don't need to check any boxes (permissions) for this tool to work! Just scroll to the bottom and click **Generate token**.
8. **Copy the token** (it looks like `ghp_...`). **Warning: You will only see it once!**

### How to use your token:
Type this in your terminal (replace `YOUR_TOKEN` with the code you just copied):
```bash
gh-t config --token YOUR_TOKEN
```

---

## ⌨️ How to use the Tool (Easy Commands)

Once installed, you can use these commands from anywhere:

### Basic Commands
| What you want to do | Type this command |
| :--- | :--- |
| **See Top 10 Trending Repos** | `gh-t fetch` |
| **See Top 5 instead of 10** | `gh-t fetch --limit 5` |
| **See only Python projects** | `gh-t fetch --lang python` |
| **Strictly only Python** (no mixed projects) | `gh-t fetch --lang python --strict` |

### Advanced Tricks
| What you want to do | Type this command |
| :--- | :--- |
| **See trends from 2023** | `gh-t fetch --year 2023` |
| **See trends from last 30 days** | `gh-t fetch --days 30` |
| **Translate results to English** | `gh-t fetch --translate` |
| **Save to Downloads folder (Excel/CSV)** | `gh-t fetch --export csv` |
| **Save to Downloads folder (JSON)** | `gh-t fetch --export json` |

### Configuration (Settings)
| What you want to do | Type this command |
| :--- | :--- |
| **Set a default language** (e.g. Java) | `gh-t config --lang java` |
| **Check your current settings** | `gh-t config --show` |

---

## 📄 License
This project is free to use and modify, but it must **always remain free** for everyone. It is protected by the **GNU General Public License v3.0**.

---
*Created with ❤️ by Shahil Roy*
