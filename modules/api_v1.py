import time
import random
from colors import *

def run(username):
    confirm = input(f"{YELLOW}Are you sure you want to use API v1? (y/n): {RESET}").lower()
    if confirm != "y":
        return

    print(f"\n{GREEN}Running API v1...{RESET}\n")
    for _ in range(5):
        pwd = random.randint(100000, 999999)
        print(f"{CYAN}{username}:{pwd}{RESET}")
        time.sleep(0.5)
