import hashlib
import zlib
import os

try:
    import whirlpool
except ImportError:
    whirlpool = None

banner = """\033[091m
           ___   __________    __  __           __             
    ____  /   | / ___/ ___/   / / / /___ ______/ /_  ___  _____
   / __ \/ /| | \__ \\__ \    / /_/ / __ `/ ___/ __ \/ _ \/ ___/
  / /_/ / ___ |___/ /__/ /  / __  / /_/ (__  ) / / /  __/ /    
 / .___/_/  |_/____/____/  /_/ /_/\__,_/____/_/ /_/\___/_/     
/_/                                                            
\033[0m"""

# Colors
PURPLE = "\033[35m"
RED = "\033[31m"
RESET = "\033[0m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def crc16(data: bytes):
    crc = 0xFFFF
    for b in data:
        crc ^= b << 8
        for _ in range(8):
            if (crc & 0x8000):
                crc = (crc << 1) ^ 0x1021
            else:
                crc <<= 1
            crc &= 0xFFFF
    return crc

def hash_password(password, algorithm):
    password_bytes = password.encode()

    if algorithm == "NTLM":
        return hashlib.new('md4', password_bytes.decode('utf-8').encode('utf-16le')).hexdigest()
    elif algorithm == "CRC16":
        return format(crc16(password_bytes), '04x')
    elif algorithm == "CRC32":
        return format(zlib.crc32(password_bytes) & 0xFFFFFFFF, '08x')
    elif algorithm == "Adler32":
        return format(zlib.adler32(password_bytes) & 0xFFFFFFFF, '08x')
    elif algorithm == "Whirlpool":
        if whirlpool:
            return whirlpool.new(password_bytes).hexdigest()
        else:
            return "Whirlpool module not installed (pip install whirlpool)"
    else:
        try:
            h = hashlib.new(algorithm.lower())
            h.update(password_bytes)
            return h.hexdigest()
        except ValueError:
            return f"{algorithm} not supported."

def passhasher():
    while True:
        clear()

        # Updated list — only working algorithms
        algorithms = [
            "NTLM", "MD4", "MD5",
            "SHA1", "SHA3-224", "SHA3-256", "SHA3-384", "SHA3-512",
            "SHA-224", "SHA-256", "SHA-384", "SHA-512",
            "CRC16", "CRC32", "Adler32", "Whirlpool"
        ]
        print(banner)
        print(PURPLE + "Supported Hash Algorithms:" + RESET)
        for i, algo in enumerate(algorithms, 1):
            print(f"{PURPLE}[{i}] {algo}{RESET}")

        choice = input(RED + "\nChoose hash algorithm number (or type 'exit' to quit): " + RESET).strip()

        if choice.lower() == "exit":
            print(RED + "Goodbye!" + RESET)
            break

        try:
            choice_num = int(choice)
            algo = algorithms[choice_num - 1]
        except (IndexError, ValueError):
            print(RED + "\nInvalid selection! Restarting..." + RESET)
            input(PURPLE + "\nPress Enter to continue..." + RESET)
            continue

        password = input(RED + "\nEnter the password to hash: " + RESET)

        hashed_password = hash_password(password, algo)

        print(PURPLE + f"\n[+] {algo} Hash:" + RESET)
        print(RED + hashed_password + RESET)

        input(PURPLE + "\nPress Enter to hash another password..." + RESET)

if __name__ == "__main__":
    passhasher()
