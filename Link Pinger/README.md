# Link Pinger

A tool for checking links from a text file — determines which links are alive, dead, redirecting, or slow.

## Usage
1. Create a file named `links.txt` in the project directory, with one URL per line. You can enter links with or without the protocol (e.g., `youtube.com` or `https://youtube.com`). The tool will automatically try to complete the protocol if it is missing.
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the tool:
```
python link_pinger.py
```
4. The results will be printed to the console and saved to `link_report.csv`.

## Parameters
- A link is considered slow if it takes more than 2 seconds to respond.
- Dead link: Not accessible or returns an error code.
- Redirect: Returns a redirect response.
- If a link does not start with `http://` or `https://`, the tool will first try `https://` and then `http://` if needed.

Good luck! 