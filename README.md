# Cybersecurity Tools

This repository contains a collection of simple yet effective cybersecurity tools built with Python. These tools are designed for **information gathering** and **vulnerability scanning**, useful for penetration testers, security researchers, and anyone interested in learning about cybersecurity.

## Tools Overview

### 1. `info_gathering.py`
This script provides basic information about a target domain:
- **WHOIS Lookup**: Retrieves registration details about the domain.
- **DNS Records**: Fetches A records (IP addresses) for the domain.

### 2. `vuln_scanner.py`
This script scans a target for open ports:
- **Port Scanning**: It scans a set of common ports (FTP, SSH, HTTP, etc.) to check if they are open.

### 3. `main.py`
This is the main script that combines the functionalities of `info_gathering.py` and `vuln_scanner.py`. It allows the user to choose between performing information gathering, vulnerability scanning, or both.

Usage Instructions
--------------------

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pranav-ti/info_gathering_vuln_scanner.git
   cd info_gathering_vuln_scanner

2. **Install dependencies**:
   Before running the tools, install the required Python libraries by running:
   ```bash
   pip3 install -r requirements.txt

3. Run the tool: To start using the tool, run:
   ```bash
   python3 main.py

Follow the on-screen prompts to choose between information gathering, vulnerability scanning, or both.
