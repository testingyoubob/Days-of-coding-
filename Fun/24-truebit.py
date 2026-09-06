from helper import *

text = "=================== SYSTEM BREACH DETECTED ==================="

for step in range(100):
    output = []
    for i, char in enumerate(text):

        r = int(math.sin(i * 0.15 + step * 0.2) * 127 + 128)
        g = int(math.sin(i * 0.15 + step * 0.2 + 2) * 60)
        b = int(math.sin(i * 0.15 + step * 0.2 + 4) * 127 + 128)
        output.append(f"\033[38;2;{r};{g};{b}m{char}")

    print(f"\r{''.join(output)}\033[0m", end="", flush=True)
    time.sleep(0.05)

print()