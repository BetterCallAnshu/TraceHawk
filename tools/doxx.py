import os
import shutil

banner = """\033[91m
    ▓█████▄  ▒█████  ▒██   ██▒    ▄████▄   ██▀███  ▓█████ ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███
    ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░   ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
    ░██   █▌▒██░  ██▒░░  █   ░   ▒▓█    ▄ ▓██ ░▄█ ▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
    ░▓█▄   ▌▒██   ██░ ░ █ █ ▒    ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄
    ░▒████▓ ░ ████▓▒░▒██▒ ▒██▒   ▒ ▓███▀ ░░██▓ ▒██▒░▒████▒▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
     ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░   ░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
     ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░     ░  ▒     ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
     ░ ░  ░ ░ ░ ░ ▒   ░    ░     ░          ░░   ░    ░    ░   ▒    ░      ░ ░ ░ ▒    ░░   ░
       ░        ░ ░   ░    ░     ░ ░         ░        ░  ░     ░  ░            ░ ░     ░
     ░                           ░
\033[0m"""

def get_file_path(prompt):
    print(f"\n\033[35m{prompt}\033[0m")
    file_path = input("Drag and drop the file here and press Enter (or just press Enter to skip): ").strip().strip("'\"")

    if not file_path:
        return None  
    if os.path.exists(file_path):
        return file_path
    else:
        print("\033[31mInvalid file path. Please try again or press Enter to skip.\033[0m")
        return get_file_path(prompt)  
        
def save_data_to_txt(folder_path, data):
    file_path = os.path.join(folder_path, f"{os.path.basename(folder_path)}.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(banner)
        for key, value in data.items():
            if key not in ["Picture (File path)", "Document (File path)"]:
                file.write(f"{key}: {value}\n")

def copy_file(source_path, folder_path):
    try:
        source_path = source_path.strip("'\"")
        print(f"Attempting to copy from: {source_path}")

        if os.path.exists(source_path):
            file_name = os.path.basename(source_path)
            destination_path = os.path.join(folder_path, file_name)
            shutil.copy(source_path, destination_path)
            print(f"Copied {file_name} successfully!")
        else:
            print(f"Error: The file {source_path} does not exist.")
    except Exception as e:
        print(f"Failed to copy the file. Error: {e}")

def create_osint_profile():
    cwd = os.getcwd()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)

    folder_name = input("[+] Enter folder name for the profile: ").strip()
    folder_path = os.path.join(cwd, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    data = {}
    data["First Name"] = input("[+] First Name: ")
    data["Last Name"] = input("[+] Last Name: ")
    data["Nick name of person"] = input("[+] Nick name of person: ")
    data["Username/s"] = input("[+] Username/s: ")
    data["Age"] = input("[+] Age: ")
    data["DOB"] = input("[+] DOB: ")
    data["E-Mail"] = input("[+] E-Mail: ")
    data["Phone Number"] = input("[+] Phone Number: ")
    data["Social Media"] = input("[+] Social Media: ")
    data["IPv4"] = input("[+] IPv4: ")
    data["IPv6"] = input("[+] IPv6: ")
    data["Address"] = input("[+] Address (country/state/city): ")

    data["Picture (File path)"] = get_file_path("Drag and drop your Picture file into this terminal and press Enter:")
    data["Document (File path)"] = get_file_path("Drag and drop your Document file into this terminal and press Enter:")

    data["Links"] = input("[+] Links (Comma separated if more than one): ")
    data["NOTE"] = input("[+] ADD A NOTE (optional): ")

    save_data_to_txt(folder_path, data)

    if data["Picture (File path)"]:
        copy_file(data["Picture (File path)"], folder_path)
    if data["Document (File path)"]:
        copy_file(data["Document (File path)"], folder_path)

    print("\n[+] OSINT profile created successfully!")

if __name__ == "__main__":
    create_osint_profile()
