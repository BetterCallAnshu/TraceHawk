import subprocess
import os

banner = """\033[94m
 ______
 \      \   _____  _____  ______
 /   |   \ /     \ \__  \ \____ \ 
/    |    \  Y Y  \/ __  \|  |_> >
\____|__  /__|_|  (____  /   ___/
        \/      \/     \/|__|    
\033[0m"""

banner1 = """
\033[92m
1. Fast scan (top 100 ports)
2. Full port scan (0-65535)
3. Manual port input (e.g., 22,80,443)
4. OS Detection
5. Service Detection
6. Vulnerability Scan
7. Aggressive Scan (-A)
8. Custom Nmap Command
\033[0m
"""

def nmapscan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[96m=== Advanced Nmap Scanner ===\033[0m")
    print(banner)
    print("\033[94mChoose scan type: \033[0m")
    print(banner1)

    choice = input("Your choice (1-8): ").strip()

    target = input("Enter target domain or IP (no http/https): ").strip()

    if choice == "1":
        cmd = f"nmap -T4 --top-ports 100 {target}"
    elif choice == "2":
        cmd = f"nmap -p- {target}"
    elif choice == "3":
        ports = input("Enter ports (e.g., 21,22,80,443): ").strip()
        cmd = f"nmap -p {ports} {target}"
    elif choice == "4":
        cmd = f"nmap -O {target}"
    elif choice == "5":
        cmd = f"nmap -sV {target}"
    elif choice == "6":
        cmd = f"nmap --script vuln {target}"
    elif choice == "7":
        cmd = f"nmap -A {target}"
    elif choice == "8":
        custom = input("Enter full Nmap command (use {target} for the target): ").strip()
        cmd = custom.replace("{target}", target)
    else:
        print("\033[91m[!] Invalid choice.\033[0m")
        return

    print(f"\n\033[93m[+] Running:\033[0m {cmd}\n" + "-"*60)
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    nmapscan()
