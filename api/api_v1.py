import random, time
from core.colors import C

def run(username):
    print(C.YELLOW + "[API v1] Running..." + C.RESET)
    for _ in range(5):
        pwd = ''.join(random.choices("abcdef0123456789", k=8))
        print(f"{username}:{pwd}")
        time.sleep(0.3)
