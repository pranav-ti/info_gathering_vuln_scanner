from info_gathering import run_info_gathering
from vuln_scanner import run_vuln_scanner

def main():
    print("Cybersecurity Tool: Information Gathering and Vulnerability Scanner")
    target = input("Enter the target domain/IP: ")
    choice = input("Choose action: [1] Information Gathering [2] Vulnerability Scanner [3] Both: ")

    if choice == "1":
        run_info_gathering(target)
    elif choice == "2":
        run_vuln_scanner(target)
    elif choice == "3":
        run_info_gathering(target)
        run_vuln_scanner(target)
    else:
        print("[-] Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
