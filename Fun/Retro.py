from helper import *

message = "Connecting to rempte terminal... Handshake verified."

for char in message: 
    sys.stdout.write(char)
    sys.stdout.flush()

    delay = random.uniform(0.15, 0.3) if char in ".,?!" else random.uniform(0.02, 0.07)
    time.sleep(delay)

print()