#!/usr/bin/env python3
from banner import show_banner
from menu import main_menu

def clear():
    print("\033c", end="")

clear()
show_banner()
main_menu()
