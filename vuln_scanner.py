import socket

# Mapping of common ports to services
PORT_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    443: "HTTPS",
}

def scan_ports(target, ports):
    print(f"[*] Scanning {target} on ports {ports}")
    try:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)  # Timeout for slow responses
            result = s.connect_ex((target, port))  # Connect to the target port
            if result == 0:
                # Get service name from the dictionary
                service = PORT_SERVICES.get(port, "Unknown Service")
                print(f"[+] Port {port} ({service}) is open")
            s.close()
    except Exception as e:
        print(f"[-] Error during scanning: {e}")

def run_vuln_scanner(target):
    # Define ports to scan (you can expand this list)
    ports_to_scan = list(PORT_SERVICES.keys())
    print("[*] Starting Vulnerability Scanning...")
    scan_ports(target, ports_to_scan)
