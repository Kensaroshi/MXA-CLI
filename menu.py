from core.colors import C
from core.effects import clear, typewriter
from core.spinner import spinner
from api import api_v1, api_v2

def main_menu():
    while True:
        print(C.CYAN + "\n[1] Find User")
        print("[2] User Status")
        print("[Q] Quit" + C.RESET)

        choice = input("> ").lower()

        if choice == "1":
            confirm = input("Proceed? (y/n): ").lower()
            if confirm != "y":
                continue

            username = input("Enter Username: ")

            print("[1] API v1")
            print("[2] API v2")
            api = input("> ")

            spinner("Initializing")
            if api == "1":
                api_v1.run(username)
            elif api == "2":
                api_v2.run(username)

        elif choice == "2":
            spinner("Checking status")
            for i in range(20):
                print(f"Status#{str(i).zfill(4)}")

        elif choice == "q":
            print("Exit.")
            break
