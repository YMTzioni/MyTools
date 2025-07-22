import json
import sys
import requests

COMMANDS_FILE = 'commands.json'


def load_commands():
    with open(COMMANDS_FILE, encoding='utf-8') as f:
        return json.load(f)

def fetch_cheatsh(command):
    url = f"https://cheat.sh/{command}?T"
    try:
        response = requests.get(url, timeout=5)
        if response.ok and "Unknown topic." not in response.text:
            return response.text
        else:
            return None
    except Exception:
        return None

def print_menu():
    print("Welcome to the Linux Command Cheat Sheet Generator!")
    print("Choose an option:")
    print("1. Search for a command")
    print("2. Show all commands")
    print("3. Export to HTML")
    print("4. Export to Markdown")
    print("5. Exit")

def search_command(commands):
    term = input("Enter a command name or keyword to search: ")
    # Try cheat.sh first
    cheatsh_result = fetch_cheatsh(term)
    if cheatsh_result:
        print(f"\nResult from cheat.sh for '{term}':\n")
        print(cheatsh_result)
    else:
        # Fallback to local database
        found = [cmd for cmd in commands if term in cmd['command'] or term in cmd['description']]
        if found:
            for cmd in found:
                print(f"\nCommand: {cmd['command']}\nDescription: {cmd['description']}\nExample: {cmd['example']}")
        else:
            print("No results found in cheat.sh or local database.")

def show_all(commands):
    for cmd in commands:
        print(f"\nCommand: {cmd['command']}\nDescription: {cmd['description']}\nExample: {cmd['example']}")

def main():
    commands = load_commands()
    while True:
        print_menu()
        choice = input("Enter a number: ")
        if choice == '1':
            search_command(commands)
        elif choice == '2':
            show_all(commands)
        elif choice == '3':
            from exporter import export_to_html
            export_to_html(commands)
            print("File commands.html saved!")
        elif choice == '4':
            from exporter import export_to_markdown
            export_to_markdown(commands)
            print("File commands.md saved!")
        elif choice == '5':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main() 