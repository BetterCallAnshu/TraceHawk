from colorama import Fore, Style, init
init(autoreset=True)

def success(msg): 
    print(Fore.GREEN + "[✔] " + msg)

def error(msg): 
    print(Fore.RED + "[✘] " + msg)

def warning(msg): 
    print(Fore.YELLOW + "[!] " + msg)

def info(msg): 
    print(Fore.CYAN + "[i] " + msg)

def inp(msg): 
    return input(Fore.MAGENTA + "[?] " + msg + Style.RESET_ALL)
