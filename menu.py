import sys
import time
from colors import *
from modules import api_v1, api_v2

def main_menu():
    while True:
        print(f"\n{PURPLE}{BOLD}[1]{RESET} Find")
        print(f"{PURPLE}{BOLD}[2]{RESET} User Status")
        print(f"{RED}{BOLD}[0]{RESET} Exit")

        choice = input(f"{CYAN}MXA > {RESET}")

        if choice == "1":
            find_menu()
        elif choice == "2":
            user_status()
        elif choice == "0":
            print("Exiting...")
            sys.exit()
        else:
            print(f"{RED}Invalid option{RESET}")

def find_menu():
    confirm = input(f"{YELLOW}Do you want to continue? (y/n): {RESET}").lower()
    if confirm != "y":
        return

    username = input(f"{CYAN}Enter username: {RESET}")

    while True:
        print(f"\n{PURPLE}[1]{RESET} API v1 (slow)")
        print(f"{PURPLE}[2]{RESET} API v2 (fast)")
        print(f"{RED}[0]{RESET} Cancel")

        api = input(f"{CYAN}Select API > {RESET}")

        if api == "1":
            api_v1.run(username)
            loading()
            return
        elif api == "2":
            api_v2.run(username)
            loading()
            return
        elif api == "0":
            return
        else:
            print(f"{RED}Invalid selection{RESET}")

def user_status():
    while True:
        print(f"\n{PURPLE}[1]{RESET} Check")
        print(f"{RED}[0]{RESET} Back")

        c = input(f"{CYAN}Select > {RESET}")

        if c == "1":
            try:
                print(f"{GREEN}Checking status...{RESET}\n")
                while True:
                    import random
                    code = random.randint(0, 9999)
                    print(f"{CYAN}Status#{code:04d}{RESET}")
                    time.sleep(0.02)
            except KeyboardInterrupt:
                print(f"\n{YELLOW}Stopped.{RESET}")
                return
        elif c == "0":
            return

def loading():
    print(f"\n{YELLOW}Loading{RESET}", end="")
    for _ in range(6):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print(f"\n{GREEN}Returning to main menu...{RESET}\n")
