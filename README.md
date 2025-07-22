# 🧪 Port Scanner & Simple Vulnerability Check

A simple Python tool to scan open ports on a target machine and perform basic vulnerability checks.

## Features
- **Dynamic input:** Choose target (IP/hostname), port range (e.g. 20-1024 or 'all'), and socket timeout.
- **Multi-threaded scan:** Fast scanning using 200 threads.
- **Service detection:** Shows the common service name for each port (if known).
- **Summary:** At the end, lists all open ports found.


## Usage
1. Run `port_scanner.py` with Python 3.
2. Enter the target address, port range (e.g. `80-1000` or `all`), and timeout when prompted.
3. The script will scan the selected ports and print results as it goes.
4. At the end, you'll see a summary of all open ports.

## Example
```
--- Port Scanner ---
Enter IP address or hostname (default: localhost): localhost
Enter port range (e.g. 20-1024, 'all' for 1-65535, default: 1-1024): 20-100
Enter socket timeout in seconds (default: 0.2): 0.2

Scanning ports on localhost with 200 threads...
Port    21: closed | Service: ftp
Port    22: OPEN   | Service: ssh
...

Scan completed. Elapsed time: 1.23 seconds.

Open ports:
  Port    22 | Service: ssh
```


## Requirements
- Python 3.x
- No external dependencies required for basic scan

