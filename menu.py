import time
import random

def main_menu():
    while True:
        print("""
[1] Demo Scan
[2] Dice Game
[3] About
[0] Exit
""")
        choice = input("MXA > ")

        if choice == "1":
            demo_scan()
        elif choice == "2":
            dice_game()
        elif choice == "3":
            about()
        elif choice == "0":
            print("Exit...")
            time.sleep(1)
            break
        else:
            print("Unknown command\n")

def demo_scan():
    print("\nStarting demo scan...\n")
    for i in range(1, 6):
        print(f"[+] Scanning module {i}/5")
        time.sleep(0.6)
    print("\n[✓] Done (demo only)\n")

def dice_game():
    print("\nRolling dice...")
    time.sleep(1)
    print("Result:", random.randint(1, 6), "\n")

def about():
    print("""
MXA-CLI
MaxAvas Command Line Interface
Terminal-style demo project for Kali Linux
No hacking. Just for fun.
""")
