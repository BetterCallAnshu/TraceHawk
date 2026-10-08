import subprocess
import os
import sys

banner = """\033[92m
________  .__  __ __________                __                
\______ \ |__|/  |\______   \__ __  _______/  |_  ___________
 |    |  \|  \   __\    |  _/  |  \/  ___/\   __\/ __ \_  __ \ 
 |    `   \  ||  | |    |   \  |  /\___ \  |  | \  ___/|  | \/
/_______  /__||__| |______  /____//____  > |__|  \___  >__|
        \/                \/           \/            \/        \033[0m"""

def get_website():
    website = input("\033[94mEnter the website URL (e.g., https://example.com): \033[0m").strip()
    if not website.startswith("http"):
        print("\033[91mError: Please include 'http://' or 'https://' in the URL.\033[0m")
        sys.exit(1)
    return website

def get_wordlist():
    print("\033[94mPlease drag and drop your wordlist (.txt) file into the terminal.\033[0m")
    wordlist = input("Wordlist path: ").strip()

    wordlist = wordlist.strip().strip('"').strip("'")
    wordlist = os.path.abspath(wordlist)

    if not os.path.isfile(wordlist):
        print(f"\033[91mError: File not found -> {wordlist} \033[0m")
        sys.exit(1)
    return wordlist

def get_threads():
    while True:
        try:
            threads = int(input("\033[94mEnter number of threads (e.g., 50): \033[0m").strip())
            if threads < 1:
                print("\033[91mThread count must be positive. \033[0m")
                continue
            return threads
        except ValueError:
            print("\033[91mPlease enter a valid number.\033[0m")

def run_gobuster(website, wordlist, threads):
    cmd = [
        "gobuster", "dir",
        "-u", website,
        "-w", wordlist,
        "-t", str(threads),
        "-s", "200,204,301,307,403",
        "--status-codes-blacklist", ""
    ]
    print("\nRunning Gobuster with the following command:")
    print(" ".join(cmd))
    print("-" * 60)
    subprocess.run(cmd)

def dirbuster():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    print("\033[92m=== Gobuster DirBuster Launcher ===\033[0m")
    website = get_website()
    wordlist = get_wordlist()
    threads = get_threads()
    run_gobuster(website, wordlist, threads)

if __name__ == "__main__":
    dirbuster()
