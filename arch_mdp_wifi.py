#!/usr/bin/env python3
import os
import sys
import logging
import configparser
import argparse
from dataclasses import dataclass
from typing import List, Optional, Generator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("WiFiInspector")

@dataclass
class WiFiProfile:
    """Dataclass representing a structured Wi-Fi network profile."""
    filename: str
    filepath: str
    ssid: str
    password: Optional[str] = None
    is_secure: bool = False

class PrivilegeError(Exception):
    """Raised when the script is not executed with root privileges."""
    pass

class ProfileNotFoundError(Exception):
    """Raised when the NetworkManager configuration directory is missing."""
    pass

class NetworkManagerInspector:
    """Handles discovery, parsing, and extraction of NetworkManager profiles."""
    
    DEFAULT_CONNECTION_DIR = "/etc/NetworkManager/system-connections/"

    def __init__(self, connection_dir: str = DEFAULT_CONNECTION_DIR) -> None:
        self.connection_dir = connection_dir
        self._validate_environment()

    def _validate_environment(self) -> None:
        """Validates execution privileges and directory existence."""
        if os.geteuid() != 0:
            raise PrivilegeError("This script must be executed with root privileges (sudo).")
        
        if not os.path.isdir(self.connection_dir):
            raise ProfileNotFoundError(f"Directory {self.connection_dir} not found. Verify NetworkManager installation.")

    def fetch_profile_filenames(self) -> List[str]:
        """Retrieves a list of valid profile files from the system directory."""
        try:
            return [
                f for f in os.listdir(self.connection_dir)
                if os.path.isfile(os.path.join(self.connection_dir, f))
            ]
        except OSError as e:
            logger.error(f"Failed to read connection directory: {e}")
            return []

    def parse_profile(self, filename: str) -> WiFiProfile:
        """Parses an individual profile configuration file."""
        filepath = os.path.join(self.connection_dir, filename)
        config = configparser.ConfigParser()
        
        try:
            config.read(filepath)
            ssid = config.get("connection", "id", fallback=filename)
            password = config.get("wifi-security", "psk", fallback=None)
            is_secure = config.has_section("wifi-security")

            return WiFiProfile(
                filename=filename,
                filepath=filepath,
                ssid=ssid,
                password=password,
                is_secure=is_secure
            )
        except Exception as e:
            logger.warning(f"Failed to parse profile {filename}: {e}")
            return WiFiProfile(filename=filename, filepath=filepath, ssid=filename, password=None, is_secure=False)

    def get_all_profiles(self) -> Generator[WiFiProfile, None, None]:
        """Generator yielding parsed Wi-Fi profiles."""
        for filename in self.fetch_profile_filenames():
            yield self.parse_profile(filename)


class CLIController:
    """Manages command-line presentation and user interaction workflow."""

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="Advanced NetworkManager Profile Credential Inspector")
        self.parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose debug logging")
        self.args = self.parser.parse_args()

    def run(self) -> None:
        """Executes the main application lifecycle."""
        if self.args.verbose:
            logger.setLevel(logging.DEBUG)

        try:
            inspector = NetworkManagerInspector()
            profiles = list(inspector.get_all_profiles())

            if not profiles:
                logger.info("No saved Wi-Fi profiles were discovered.")
                sys.exit(0)

            print("\n" + "="*40)
            print(" DISCOVERED WI-FI PROFILES ")
            print("="*40)
            
            for index, profile in enumerate(profiles, start=1):
                print(f"[{index}] {profile.filename} (SSID: {profile.ssid})")
            
            print("-" * 40)
            selection = input("\nSelect profile number to inspect: ").strip()
            
            try:
                choice_idx = int(selection) - 1
                if choice_idx < 0 or choice_idx >= len(profiles):
                    raise IndexError()
                selected = profiles[choice_idx]
            except (ValueError, IndexError):
                logger.error("Invalid selection index provided.")
                sys.exit(1)

            print("\n" + "="*40)
            print(f" PROFILE DETAILS: {selected.filename}")
            print("="*40)
            print(f"Target SSID : {selected.ssid}")
            
            if selected.password:
                print(f"PSK Password: {selected.password}")
            else:
                print("PSK Password: [Open Network or No Password Stored]")
            print("="*40 + "\n")

        except (PrivilegeError, ProfileNotFoundError) as err:
            logger.error(str(err))
            sys.exit(1)
        except KeyboardInterrupt:
            print("\n[!] Operation cancelled by user.")
            sys.exit(0)

if __name__ == "__main__":
    controller = CLIController()
    controller.run()

# Made by M0ht3p on VSCodium for the NSI repo
