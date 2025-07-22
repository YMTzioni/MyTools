import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def get_user_input():
    print("--- Port Scanner ---")
    target = input("Enter IP address or hostname (default: localhost): ") or "localhost"
    port_range = input("Enter port range (e.g. 20-1024, 'all' for 1-65535, default: 1-1024): ") or "1-1024"
    timeout_str = input("Enter socket timeout in seconds (default: 0.2): ") or "0.2"
    if port_range.strip().lower() == 'all':
        start_port, end_port = 1, 65535
    else:
        try:
            start_port, end_port = map(int, port_range.split('-'))
            if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port <= end_port):
                raise ValueError
        except Exception:
            print("Invalid port range. Using default: 1-1024")
            start_port, end_port = 1, 1024
    try:
        timeout = float(timeout_str)
        if timeout <= 0:
            raise ValueError
    except Exception:
        print("Invalid timeout. Using default: 0.2")
        timeout = 0.2
    return target, range(start_port, end_port+1), timeout

def check_port(target, port, timeout):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        result = s.connect_ex((target, port))
        try:
            service = socket.getservbyport(port)
        except Exception:
            service = 'Unknown'
        status = "OPEN" if result == 0 else "closed"
        return port, status, service

def scan_ports(target, ports, timeout):
    print(f"\nScanning ports on {target} with 200 threads...\n")
    results = []
    with ThreadPoolExecutor(max_workers=200) as executor:
        future_to_port = {executor.submit(check_port, target, port, timeout): port for port in ports}
        for future in as_completed(future_to_port):
            port, status, service = future.result()
            print(f"Port {port:5d}: {status:6s} | Service: {service}")
            results.append((port, status, service))
    return results

def check_vulnerabilities(target):
    # Placeholder: Perform simple vulnerability checks (headers, outdated servers, etc.)
    pass

def main():
    target, ports, timeout = get_user_input()
    start_time = time.time()
    results = scan_ports(target, ports, timeout)
    check_vulnerabilities(target)
    open_ports = [(port, service) for port, status, service in results if status == "OPEN"]
    print(f"\nScan completed. Elapsed time: {time.time() - start_time:.2f} seconds.")
    if open_ports:
        print("\nOpen ports:")
        for port, service in sorted(open_ports):
            print(f"  Port {port:5d} | Service: {service}")
    else:
        print("\nNo open ports found.")

if __name__ == "__main__":
    main() 