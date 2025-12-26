import random
from core.colors import C

def run(username):
    print(C.GREEN + "[API v2] Ultra Fast Mode" + C.RESET)
    for _ in range(30):
        pwd = ''.join(random.choices("abcdef0123456789", k=10))
        print(f"{username}:{pwd}")
