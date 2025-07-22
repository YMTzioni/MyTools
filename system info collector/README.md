# System Info Collector

A simple Python script to collect and display key system information for Windows machines. Useful for technicians, diagnostics, and quick system overviews.

## Features
- Displays CPU info (name, cores)
- Shows total RAM
- Reports local and public IP addresses
- Shows OS and version
- Displays free disk space
- Shows system uptime
- Displays machine model
- Lists network adapters
- Shows CPU temperature (if available)
- Robust error handling
- Output is organized by sections for readability

## Requirements
- Python 3.7+
- See `requirements.txt` for required packages

## Installation
1. Clone or download this repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the script in your terminal:
```
python system_info_collector.py
```

## Example Output
```
==============================
   System Information Report   
==============================

[System]
| Property         | Value                |
|------------------|----------------------|
| Operating System | Windows              |
| OS Version       | 10.0.19045           |
| System Uptime    | 2:15:34              |
| Machine Model    | Dell Inc. XPS 13     |

[Hardware]
| Property            | Value      |
|---------------------|-----------|
| CPU                 | Intel ... |
| CPU Cores           | 8         |
| Total RAM (GB)      | 16.00     |
| Free Disk Space (GB)| 120.50    |
| CPU Temperature (C) | 45.0      |

[Network]
| Property           | Value                        |
|--------------------|-----------------------------|
| IP Address         | 192.168.1.10                |
| Public IP Address  | 8.8.8.8                     |
| Network Adapters   | Intel(R) Ethernet ... (xx)  |
``` 