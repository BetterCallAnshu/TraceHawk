import socket
import threading
import subprocess
import platform
from queue import Queue
import ipaddress
import os
from itertools import zip_longest

TIMEOUT = 0.5
MAX_THREADS = 100

banner1 = """\033[091m
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
 ▄▄▄       ███▄    █   ▄████  ██▀███ ▓██   ██▓    ██▓ ██▓███       ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██ ▒ ██▒▒██  ██▒   ▓██▒▓██░  ██▒   ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██ ░▄█ ▒ ▒██ ██░   ▒██▒▓██░ ██▓▒   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██▀▀█▄   ░ ▐██▓░   ░██░▒██▄█▓▒ ▒     ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
 ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒░██▓ ▒██▒ ░ ██▒▓░   ░██░▒██▒ ░  ░   ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
 ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒▓ ░▒▓░  ██▒▒▒    ░▓  ▒▓▒░ ░  ░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░   ░▒ ░ ▒░▓██ ░▒░     ▒ ░░▒ ░        ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
  ░   ▒      ░   ░ ░ ░ ░   ░   ░░   ░ ▒ ▒ ░░      ▒ ░░░          ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
      ░  ░         ░       ░    ░     ░ ░         ░                    ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                                      ░ ░                                 ░                                                        
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
\033[0m
"""

banner = """\033[091m
      ⣀⣠⣤⣤⣤⣤⣀⡀
   ⣠⣤⢶⣻⣿⣻⣿⣿⣿⣿⣿⣿⣦⣤⣀
  ⣼⣺⢷⣻⣽⣾⣿⢿⣿⣷⣿⣿⢿⣿⣿⣿⣇
⠠⡍⢾⣺⢽⡳⣻⡺⣽⢝⢗⢯⣻⢽⣻⣿⣿⣿⣿⢿⡄
⡨⣖⢹⠜⢅⢫⢊⢎⠜⢌⠣⢑⠡⣹⡸⣜⣯⣿⢿⣻⣷
⢜⢔⡹⡭⣪⢼⠽⠷⠧⣳⢘⢔⡝⠾⠽⢿⣷⣿⣟⢷⣟
⢸⢘⢼⠿⠟⠁⠄⠄⡀⠄⠃⠑⡌⠄⠄⠈⠙⠿⣷⢽⣻
⢌⠂⠅⠄⠄⠄⠄⠄⠄⡀⣲⣢⢂⠄⠄⠄⠄⠄⠈⣯⠏
⠐⠨⡂⠄⠄⠄⠄⠄⡀⡔⠋⢻⣤⡀⠄⠄⢀⠄⢸⣯⠇
⠈⣕⠝⠒⠄⠄⠒⢉⠪⠄⠄⠄⢿⠜⠑⠢⠠⡒⡺⣿⠖
 ⠐⠅⠁⡀⠄⠐⢔⠁⠄⠄⠄⢀⢇⢌⠄⠄⠄⠸⠕
  ⠂⠄⠄⠨⣔⡝⠼⡄⠂⣦⡆⣿⣲⠐⠑⠁⠄⠃
      ⠃⢫⢛⣙⡊⣜⣏⡝⣝⠆
      ⠈⠈⠁⠁⠁⠈⠈⠊
\033[0m"""

COMMON_SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP",
    110: "POP3", 143: "IMAP", 443: "HTTPS", 3306: "MySQL", 3389: "RDP", 8080: "HTTP-Alt"
}

ip_queue = Queue()
lock = threading.Lock()

def parse_ip_range(start_ip, end_ip):
    start_int = int(ipaddress.IPv4Address(start_ip.strip()))
    end_int = int(ipaddress.IPv4Address(end_ip.strip()))
    return start_int, end_int

def is_alive(ip):
    try:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        return subprocess.call(['ping', param, '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
    except:
        return False

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
    return open_ports

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"

def scan_ip(ip, ports):
    if is_alive(ip):
        open_ports = scan_ports(ip, ports)
        if open_ports:
            hostname = get_hostname(ip)
            with lock:
                for port in open_ports:
                    service = COMMON_SERVICES.get(port, "Unknown")

                    print(f"\033[31m[+] {ip:<15} | {hostname:<30} | Port {port:<5} ({service}) OPEN\033[0m")

def worker(ports):
    while not ip_queue.empty():
        ip = ip_queue.get()
        scan_ip(ip, ports)
        ip_queue.task_done()

def run_scan():
    os.system('cls' if os.name == 'nt' else 'clear')

    [print(f"\033[91m{l1:<25}{l2}\033[0m") for l1, l2 in zip_longest(banner.splitlines(), banner1.splitlines(), fillvalue="")]
    print("🔍 Python Open Port Scanner")

    start_ip = input("\033[35mEnter starting IP: \033[0m").strip()
    end_ip = input("\033[35mEnter ending IP: \033[0m").strip()
    port_input = input("\033[35mEnter ports to scan (comma-separated): \033[0m").strip()

    try:
        ports = sorted(set(int(p.strip()) for p in port_input.split(',')))
    except ValueError:
        print("[!] Invalid port input.")
        return

    try:
        start, end = parse_ip_range(start_ip, end_ip)
        count = end - start + 1
    except Exception as e:
        print(f"[!] Error parsing IP range: {e}")
        return

    print(f"\n[i] Scanning {count} hosts for ports: {ports}\n")

    for ip_int in range(start, end + 1):
        ip_queue.put(str(ipaddress.IPv4Address(ip_int)))

    threads = []
    for _ in range(MAX_THREADS):
        t = threading.Thread(target=worker, args=(ports,))
        t.daemon = True
        t.start()
        threads.append(t)

    ip_queue.join()

    print("\n[✔] Scan complete!")

if __name__ == "__main__":
    run_scan()
