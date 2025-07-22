import csv
import winreg

REG_PATHS = [
    (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
    (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
    (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
]

FIELDS = [
    "Name", "Version", "Publisher", "InstallDate", "UninstallString", "InstallLocation", "EstimatedSize", "Size (MB)",
    "DisplayIcon", "HelpLink", "URLInfoAbout", "Comments", "Contact", "Readme", "Language", "ModifyPath"
]

REG_FIELD_MAP = {
    "Name": "DisplayName",
    "Version": "DisplayVersion",
    "Publisher": "Publisher",
    "InstallDate": "InstallDate",
    "UninstallString": "UninstallString",
    "InstallLocation": "InstallLocation",
    "EstimatedSize": "EstimatedSize",
    "DisplayIcon": "DisplayIcon",
    "HelpLink": "HelpLink",
    "URLInfoAbout": "URLInfoAbout",
    "Comments": "Comments",
    "Contact": "Contact",
    "Readme": "Readme",
    "Language": "Language",
    "ModifyPath": "ModifyPath"
}

def get_installed_software():
    software_list = []
    for root, path in REG_PATHS:
        try:
            reg_key = winreg.OpenKey(root, path)
        except FileNotFoundError:
            continue
        for i in range(0, winreg.QueryInfoKey(reg_key)[0]):
            try:
                subkey_name = winreg.EnumKey(reg_key, i)
                subkey = winreg.OpenKey(reg_key, subkey_name)
                entry = {}
                for field, reg_field in REG_FIELD_MAP.items():
                    entry[field] = _get_reg_value(subkey, reg_field)
                # Calculate Size (MB) from EstimatedSize (KB)
                est_size = entry.get("EstimatedSize", "")
                if est_size.isdigit():
                    entry["Size (MB)"] = f"{round(int(est_size) / 1024, 2)}"
                else:
                    entry["Size (MB)"] = ""
                if entry["Name"]:
                    software_list.append(entry)
            except Exception:
                continue
    return software_list

def _get_reg_value(subkey, value):
    try:
        return str(winreg.QueryValueEx(subkey, value)[0])
    except Exception:
        return ""

def save_to_csv(software_list, filename="software_inventory.csv"):
    with open(filename, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for item in software_list:
            writer.writerow(item)

if __name__ == "__main__":
    print("Collecting installed software list...")
    software = get_installed_software()
    save_to_csv(software)
    print(f"Done. {len(software)} items saved to software_inventory.csv.") 