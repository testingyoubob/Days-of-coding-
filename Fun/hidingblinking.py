from helper import *

sys.stdout.write("\033[?25l")
sys.stdout.flush()

try: 
    for i in range(5, 0, -1):
        print(f"\rSelf-destruction in {i}...", end="", flush=True)
        time.sleep(0.8)
    print("\rBOOM!                          ")
finally:
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

