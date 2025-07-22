import platform
import psutil
import socket
import shutil
import time
from datetime import timedelta
try:
    from tabulate import tabulate
except ImportError:
    print("tabulate not found, please install with: pip install tabulate")
    exit(1)
import wmi
import requests

info = []

# CPU Info
try:
    cpu_name = platform.processor() or "Unknown"
    cpu_cores = psutil.cpu_count(logical=True)
    info.append(["CPU", cpu_name])
    info.append(["CPU Cores", cpu_cores])
except Exception as e:
    info.append(["CPU", f"Error: {e}"])
    info.append(["CPU Cores", f"Error: {e}"])

# RAM Info
try:
    total_ram = psutil.virtual_memory().total / (1024 ** 3)
    info.append(["Total RAM (GB)", f"{total_ram:.2f}"])
except Exception as e:
    info.append(["Total RAM (GB)", f"Error: {e}"])

# IP Address
try:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    info.append(["IP Address", ip_address])
except Exception as e:
    info.append(["IP Address", f"Error: {e}"])

# Public IP Address
try:
    public_ip = requests.get("https://api.ipify.org", timeout=5).text
    info.append(["Public IP Address", public_ip])
except Exception as e:
    info.append(["Public IP Address", f"Error: {e}"])

# OS Info
try:
    os_name = platform.system()
    os_version = platform.version()
    info.append(["Operating System", os_name])
    info.append(["OS Version", os_version])
except Exception as e:
    info.append(["Operating System", f"Error: {e}"])
    info.append(["OS Version", f"Error: {e}"])

# Disk Info
try:
    total, used, free = shutil.disk_usage("/")
    free_gb = free / (1024 ** 3)
    info.append(["Free Disk Space (GB)", f"{free_gb:.2f}"])
except Exception as e:
    info.append(["Free Disk Space (GB)", f"Error: {e}"])

# Uptime
try:
    boot_time = psutil.boot_time()
    uptime_sec = time.time() - boot_time
    uptime_str = str(timedelta(seconds=int(uptime_sec)))
    info.append(["System Uptime", uptime_str])
except Exception as e:
    info.append(["System Uptime", f"Error: {e}"])

# Machine Model (Windows WMI)
try:
    c = wmi.WMI()
    for sys in c.Win32_ComputerSystem():
        model = sys.Model
        manufacturer = sys.Manufacturer
        info.append(["Machine Model", f"{manufacturer} {model}"])
        break
except Exception as e:
    info.append(["Machine Model", f"Error: {e}"])

# Network Adapter Info (Windows WMI)
try:
    c = wmi.WMI()
    adapters = []
    for nic in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        adapters.append(f"{nic.Description} ({nic.MACAddress})")
    if adapters:
        info.append(["Network Adapters", ", ".join(adapters)])
    else:
        info.append(["Network Adapters", "None found"])
except Exception as e:
    info.append(["Network Adapters", f"Error: {e}"])

# CPU Temperature (Windows WMI, may not be available)
try:
    c = wmi.WMI(namespace="root\\wmi")
    temps = c.MSAcpi_ThermalZoneTemperature()
    if temps:
        # Convert from tenths of Kelvin to Celsius
        temp_c = (temps[0].CurrentTemperature / 10) - 273.15
        info.append(["CPU Temperature (C)", f"{temp_c:.1f}"])
    else:
        info.append(["CPU Temperature (C)", "Not available"])
except Exception as e:
    info.append(["CPU Temperature (C)", f"Error: {e}"])

# Organize info into sections
system_info = []
hardware_info = []
network_info = []

for prop, val in info:
    if prop in ["Operating System", "OS Version", "System Uptime", "Machine Model"]:
        system_info.append([prop, val])
    elif prop in ["CPU", "CPU Cores", "Total RAM (GB)", "Free Disk Space (GB)", "CPU Temperature (C)"]:
        hardware_info.append([prop, val])
    elif prop in ["IP Address", "Public IP Address", "Network Adapters"]:
        network_info.append([prop, val])

print()
print("==============================")
print("   System Information Report   ")
print("==============================")
print()

if system_info:
    print("[System]")
    print(tabulate(system_info, headers=["Property", "Value"], tablefmt="github"))
    print()
if hardware_info:
    print("[Hardware]")
    print(tabulate(hardware_info, headers=["Property", "Value"], tablefmt="github"))
    print()
if network_info:
    print("[Network]")
    print(tabulate(network_info, headers=["Property", "Value"], tablefmt="github"))
    print() 