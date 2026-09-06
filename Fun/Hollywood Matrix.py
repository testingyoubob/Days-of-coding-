from helper import *
target = "ACCESS GRANTED: SYSTEM ONLINE"
chars = string.ascii_letters + string.digits + "!@#$%^&*()"
revealed = [" "] * len(target)

for i in range(len(target)): 
    for _ in range(4):
        scramble = "".join(target[j] if j < i else random.choice(chars)
                           for j in range(len(target)))
        print(f"\r{scramble}", end="", flush=True)
        time.sleep(0.02)
    revealed[i] = target[i]


print(f"\r{target}")