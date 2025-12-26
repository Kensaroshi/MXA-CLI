import sys, time

def clear():
    print("\033c", end="")

def typewriter(text, delay=0.02):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()
