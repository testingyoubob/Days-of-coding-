from helper import curses as hc 
from helper import random as rh
from helper import time as th 

def draw_matrix(stdscr):
    hc.curs_set(0)
    hc.start_color()
    hc.init_pair(1, hc.COLOR_RED, hc.COLOR_BLACK)
    hc.init_pair(2, hc.COLOR_YELLOW, hc.COLOR_BLACK)
    hc.init_pair(3, hc.COLOR_GREEN, hc.COLOR_BLACK)

    stdscr.nodelay(True)

    max_y, max_x = stdscr.getmaxyx()
    columns = [rh.randint(0, max_y) for _ in range(max_x)]
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*()"
    tail_length = 1000 

    color_order = [1, 2, 3, 2]  # Red -> Yellow -> Green
    current_index = 0
    ticks = 0
    ticks_per_color = 60

    while True:
        key = stdscr.getch()
        if key == 27:
            break

            # Progress the color transition
        ticks += 1
        if ticks >= ticks_per_color:
            current_index = (current_index + 1) % len(color_order)
            ticks = 0

        active_color = hc.color_pair(color_order[current_index])
            
        stdscr.erase()
        for i, row in enumerate(columns):
            for t in range(tail_length):
                tail_row = row - t
                if 0 <= tail_row < max_y:
                    char = rh.choice(chars)
                    try:
                        stdscr.addstr(tail_row, i, char, active_color)
                    except hc.error:
                        pass
            if row >= max_y - 1 or rh.random() > 0.95:
                columns[i] = 0 
            else: 
                columns[i] += 1 

        stdscr.refresh()
        th.sleep(0.05)
if __name__ == "__main__":
    hc.wrapper(draw_matrix)

