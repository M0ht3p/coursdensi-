import os
import configparser
CONNECTION_DIR = "/etc/NetworkManager/system-connections/"
if os.geteuid() != 0:
    print("[-] Error: This script must be run with root privileges (sudo).")
    exit(1)
try:
    profiles = [f for f in os.listdir(CONNECTION_DIR) if os.path.isfile(os.path.join(CONNECTION_DIR, f))]
except FileNotFoundError:
    print(f"[-] Error: Directory {CONNECTION_DIR} not found. Is NetworkManager installed?")
    exit(1)
if not profiles:
    print("[-] No saved Wi-Fi profiles found.")
    exit(1)
print("\nSaved Wi-Fi Profiles:")
for i, profile in enumerate(profiles, 1):
    print(f"[{i}] {profile}")
try:
    ch = int(input("\nChoose WiFi number: "))
    selected_profile = profiles[ch - 1]
except (ValueError, IndexError):
    print("[-] Invalid selection.")
    exit(1)
config = configparser.ConfigParser()
config.read(os.path.join(CONNECTION_DIR, selected_profile))
try:
    ssid = config.get("connection", "id", fallback=selected_profile)
    password = config.get("wifi-security", "psk", fallback=None)

    print(f"\nSSID: {ssid}")
    if password:
        print(f"Password: {password}")
    else:
        print("Password: No password found or profile is open.")
except Exception as e:
    print(f"[-] Error parsing profile: {e}")
