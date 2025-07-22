# Linux Command Cheat Sheet Generator

A tool for generating a Linux command cheat sheet with English explanations, including search, export to HTML/Markdown, and real-time online command lookup.

## How to Use?
1. Make sure you have Python installed.
2. Install the requests library:
   ```
   pip install requests
   ```
3. Open a terminal in the project directory.
4. Run:
   ```
   python cli.py
   ```
5. Choose an option from the menu (search, show all, export).

## Online Command Search
- When searching for a command, the tool first tries to fetch the latest explanation from cheat.sh.
- If there is no internet connection or the command is not found, the result will be shown from the local database (`commands.json`).

## How to Add a Command to the Local Database?
Open the `commands.json` file and add a new object in the following format:
```json
{
  "command": "command",
  "description": "Description in English",
  "example": "command example"
}
```

## Requirements
- Python 3.7+
- requests library

Good luck! 