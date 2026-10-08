import time
from itertools import zip_longest
import os

banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠿⢿⡀⠀⠀⠀⠀⣠⣶⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣴⣿⡋⠀⠀⠈⢳⡄⠀⢠⣾⣿⠁⠈⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠿⠛⠉⠉⠁⠀⠀⠀⠹⡄⣿⣿⣿⠀⠀⢹⡇⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⢻⣿⣿⡆⠀⠸⣿⠀⠀⠀
⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣆⠹⣿⣷⠀⢘⣿⠀⠀⠀
⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠋⠉⠛⠂⠹⠿⣲⣿⣿⣧⠀⠀
⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣷⣾⣿⡇⢀⠀⣼⣿⣿⣿⣧⠀
⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⢿⣿⣿⣿⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡈⠿⢿⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⢙⠛⣿⣿⣿⣿⡟⠀⡿⠀⠀⢀⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣶⣤⣉⣛⠻⠇⢠⣿⣾⣿⡄⢻⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣆⠁
"""

banner1 = """



▄▄▄█████▓ ▒█████   ██▀███      ██▓     ██▓ ███▄    █  ██ ▄█▀  ██████ 
▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒   ▓██▒    ▓██▒ ██ ▀█   █  ██▄█▒ ▒██    ▒ 
▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒   ▒██░    ▒██▒▓██  ▀█ ██▒▓███▄░ ░ ▓██▄   
░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄     ▒██░    ░██░▓██▒  ▐▌██▒▓██ █▄   ▒   ██▒
  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒   ░██████▒░██░▒██░   ▓██░▒██▒ █▄▒██████▒▒
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░   ░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░
    ░      ░ ▒ ▒░   ░▒ ░ ▒░   ░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░░ ░▒ ▒░░ ░▒  ░ ░
  ░      ░ ░ ░ ▒    ░░   ░      ░ ░    ▒ ░   ░   ░ ░ ░ ░░ ░ ░  ░  ░  
             ░ ░     ░            ░  ░ ░           ░ ░  ░         ░
"""


def delayed_print(text, delay=0.1):
    print(text)
    time.sleep(delay)

def darkweb():
    os.system('cls' if os.name == 'nt' else 'clear')
    [print(f"\033[91m{l1:<40}{l2}\033[0m") for l1, l2 in zip_longest(banner.splitlines(), banner1.splitlines(), fillvalue="")]
    delayed_print("                                                   ")
    delayed_print("                                                   ")
    delayed_print("\033[33m[!] BEFORE OPENING THIS, MAKE SURE YOU ALREADY HAVE TOR BORWSER INSTALLED.\033[0m")
    delayed_print("")
    delayed_print("🔍TOR SEARCH ENGINES")
    delayed_print("[+] Torch -> http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion")
    delayed_print("[+] Tor66 -> http://tor66sewebgixwhcqfnp5inzp5x5uohhdy3kvtnyfxc2e5mxiuh34iid.onion")
    delayed_print("[+] EXCAVATOR -> http://2fd6cemt4gmccflhm6imvdfvli3nf7zn6rfrwpsy7uhxrgbypvwf5fad.onion")
    delayed_print("[+] ")
    delayed_print("📑DATA BREACHES")
    delayed_print("[+] Hell of hackers -> http://hellhoh5035sylxrpfu45p5r74n2lzvirnvszmziuvn7bcejlynaqxyd.onion")
    delayed_print("[+] PastBin (also on surfaceweb) -> https://pastebin.com")
    delayed_print("[+] ")

if __name__ == "__main__":
    darkweb()

