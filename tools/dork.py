import webbrowser
import os

RED = "\033[91m"
DARK_BLUE = "\033[34m"
RESET = "\033[0m"

banner = """\033[91m
                              __           __           __
   ________  ____ ___________/ /_     ____/ /___  _____/ /__
  / ___/ _ \/ __ `/ ___/ ___/ __ \   / __  / __ \/ ___/ //_/
 (__  )  __/ /_/ / /  / /__/ / / /  / /_/ / /_/ / /  / ,<
/____/\___/\__,_/_/   \___/_/ /_/   \__,_/\____/_/  /_/|_|
\033[0m"""

def build_dork(databreach, filetype, site, name, username, intitle, inurl, email, phone):
    dork_parts = []

    if databreach:
        dork_parts.append(databreach)
    if filetype:
        dork_parts.append(f"filetype:{filetype}")
    if site:
        dork_parts.append(f"site:{site}")
    if name:
        dork_parts.append(f'"{name}"')
    if username:
        dork_parts.append(f'"{username}"')
    if intitle:
        dork_parts.append(f'intitle:"{intitle}"')
    if inurl:
        dork_parts.append(f'inurl:"{inurl}"')
    if email:
        dork_parts.append(f'"{email}"')
    if phone:
        dork_parts.append(f'"{phone}"')

    return " ".join(dork_parts)

def dork():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    print(f"{DARK_BLUE}=== Google Dorking Tool ==={RESET}")
    databreach = input(f"{RED}Enter keyword for databreach (optional): {RESET}")
    filetype = input(f"{RED}Enter filetype (e.g., pdf, txt) (optional): {RESET}")
    site = input(f"{RED}Enter site (e.g., example.com) (optional): {RESET}")
    name = input(f"{RED}Enter name (optional): {RESET}")
    username = input(f"{RED}Enter username (optional): {RESET}")
    intitle = input(f"{RED}Enter intitle keyword (optional): {RESET}")
    inurl = input(f"{RED}Enter inurl keyword (optional): {RESET}")
    email = input(f"{RED}Enter email address or part of it (optional): {RESET}")
    phone = input(f"{RED}Enter phone number or pattern (optional): {RESET}")

    query = build_dork(databreach, filetype, site, name, username, intitle, inurl, email, phone)
    print(f"\n{DARK_BLUE}[+] Google Dork: {query}{RESET}")

    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)
    print(f"{DARK_BLUE}[+] Opening browser with search...{RESET}")

if __name__ == "__main__":
    dork()
