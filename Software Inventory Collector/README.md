# Software Inventory Collector

This tool scans your Windows computer for installed software and saves the inventory to a CSV file.

## Features
- Lists all installed programs on the system
- Saves the results to `software_inventory.csv`
- Collects detailed information for each software (see below)
- Simple to use, no dependencies beyond Python standard library

## Usage
1. Run the script:
   ```
   python software_inventory_collector.py
   ```
2. The output file `software_inventory.csv` will be created in the same directory.

## Output Format
The CSV file contains the following columns (if available):
- Name
- Version
- Publisher
- InstallDate
- UninstallString
- InstallLocation
- EstimatedSize (in KB)
- Size (MB) *(calculated from EstimatedSize)*
- DisplayIcon
- HelpLink
- URLInfoAbout
- Comments
- Contact
- Readme
- Language
- ModifyPath

> **Note:** Not all fields are available for every program. 'Size (MB)' is calculated from 'EstimatedSize' (if present).

## Requirements
- Windows OS
- Python 3.x

## Notes
- The script uses Windows Registry to find installed software.
- Run the script with standard user privileges for a basic list, or as administrator for a more complete inventory. 