import os
import socket
import platform
import requests

banner = """\033[91m\
    ________     __    ____  ____  __ ____  ______
   /  _/ __ \   / /   / __ \/ __ \/ //_/ / / / __ \ 
   / // /_/ /  / /   / / / / / / / ,< / / / / /_/ /
 _/ // ____/  / /___/ /_/ / /_/ / /| / /_/ / ____/
/___/_/      /_____/\____/\____/_/ |_\____/_/

\033[0m"""

def geolocate(ip):
    """Get geolocation info for an IP address."""
    print("\033[95m\n[+] Geolocating IP...\033[0m")
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        for key, value in data.items():
            print(f"\033[95m{key.capitalize():<15}: {value}\033[0m")
    except Exception as e:
        print(f"\033[91m[-] Error: {e}\033[0m")

def trace_dns(ip):
    """Perform reverse DNS lookup."""
    print("\033[95m\n[+] Performing DNS Trace...\033[0m")
    try:
        host = socket.gethostbyaddr(ip)
        print(f"\033[95mDomain Name       : {host[0]}\033[0m")
    except Exception as e:
        print(f"\033[91m[-] Error: {e}\033[0m")

def trace_mac(ip):
    """Try to fetch MAC address via ARP (local network)."""
    print("\033[95m\n[+] Tracing MAC Address...\033[0m")
    if platform.system() == "Windows":
        os.system(f"ping -n 1 {ip} >nul")
        os.system(f"arp -a {ip}")
    else:
        os.system(f"ping -c 1 {ip} > /dev/null")
        os.system(f"arp {ip}")

def run_menu():
    """Run CLI menu for IP tools."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        print("\033[95m1) Geolocate\033[0m")
        print("\033[95m2) Trace DNS\033[0m")
        print("\033[95m3) Trace MAC Address\033[0m")
        print("\033[95m0) Exit\033[0m")

        choice = input("\033[91mSelect an option: \033[0m")

        if choice == '1':
            ip = input("\033[91mEnter IP Address: \033[0m")
            geolocate(ip)
        elif choice == '2':
            ip = input("\033[91mEnter IP Address: \033[0m")
            trace_dns(ip)
        elif choice == '3':
            ip = input("\033[91mEnter IP Address: \033[0m")
            trace_mac(ip)
        elif choice == '0':
            break
        else:
            print("\033[91m[-] Invalid choice.\033[0m")

        input("\033[91mPress Enter to continue...\033[0m")

if __name__ == '__main__':
    run_menu()
