import os
import vdf
POSSIBLE_STEAM_DIRECTORIES = [
    os.path.expanduser("~/.steam/steam"),
    os.path.expanduser("~/.local/share/Steam"),
    os.path.expanduser("~/.var/app/com.valvesoftware.Steam/data/Steam"),
    os.path.expanduser("/var/app/com.valvesoftware.Steam/data/Steam"),
]

def determine_steam_directory():
    for directory in POSSIBLE_STEAM_DIRECTORIES:
        if os.path.exists(directory):
            return directory
    return None


def parse_vdf(vdf_file_path):
    with open(vdf_file_path, mode='rb') as file:
        contents = file.read()
        print(vdf.binary_loads(contents))
        return(vdf.binary_loads(contents))

def determine_users(steam_directory):
    USER_DIR = os.path.expanduser(steam_directory + "/userdata")
    user_dirs = []

    if not os.path.exists(USER_DIR):
        print(f"The directory {USER_DIR} does not exist.")
        return user_dirs

    for entry in os.listdir(USER_DIR):
        entry_path = os.path.join(USER_DIR, entry)
        if os.path.isdir(entry_path):
            user_dirs.append(entry_path)

    return user_dirs
