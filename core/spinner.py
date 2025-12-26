import itertools, sys, time
from core.colors import C

def spinner(text="Loading", duration=2):
    spin = itertools.cycle(["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"])
    end = time.time() + duration
    while time.time() < end:
        sys.stdout.write(f"\r{C.CYAN}{next(spin)} {text}{C.RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    print()
