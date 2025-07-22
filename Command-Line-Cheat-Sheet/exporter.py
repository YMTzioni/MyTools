import json

# Function to export to HTML
def export_to_html(commands, filename='commands.html'):
    html = '<html><head><meta charset="utf-8"><title>Cheat Sheet</title></head><body>'
    html += '<h1>Linux Command Cheat Sheet</h1>'
    for cmd in commands:
        html += f"<div><b>Command:</b> {cmd['command']}<br>"
        html += f"<b>Description:</b> {cmd['description']}<br>"
        html += f"<b>Example:</b> {cmd['example']}<br><br></div>"
    html += '</body></html>'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

# Function to export to Markdown
def export_to_markdown(commands, filename='commands.md'):
    md = '# Linux Command Cheat Sheet\n\n'
    for cmd in commands:
        md += f"**Command:** {cmd['command']}\n"
        md += f"**Description:** {cmd['description']}\n"
        md += f"**Example:** {cmd['example']}\n\n"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(md) 