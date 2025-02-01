import whois
import socket
import dns.resolver

def domain_info(domain):
    try:
        w = whois.whois(domain)
        print(f"[+] Whois Information for {domain}:")
        print(w)
    except Exception as e:
        print(f"[-] Whois Lookup failed: {e}")

def dns_records(domain):
    try:
        resolver = dns.resolver.Resolver()
        a_records = resolver.resolve(domain, 'A')
        print(f"[+] DNS A Records for {domain}:")
        for record in a_records:
            print(record)
    except Exception as e:
        print(f"[-] DNS Lookup failed: {e}")

def run_info_gathering(domain):
    print("[*] Starting Information Gathering...")
    domain_info(domain)
    dns_records(domain)
