import time
import random
from colors import *

def run(username):
    print(f"\n{GREEN}Running API v2{RESET}")
    print(f"{YELLOW}Press CTRL + C to interrupt{RESET}\n")

    try:
        while True:
            pwd = random.randint(100000, 999999)
            print(f"{CYAN}{username}:{pwd}{RESET}")
            time.sleep(0.03)
    except KeyboardInterrupt:
        stop = input(f"\n{RED}Do you want to stop? (yes/no): {RESET}").lower()
        if stop == "yes":
            return
