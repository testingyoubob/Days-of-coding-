import curses
import random
import time

def draw_matrix(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    stdscr.nodelay(True)

    max_y, max_x = stdscr.getmaxyx()
    columns = [random.randint(0, max_y) for _ in range(max_x)]
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

        active_color = curses.color_pair(color_order[current_index])
            
        stdscr.erase()
        for i, row in enumerate(columns):
            for t in range(tail_length):
                tail_row = row - t
                if 0 <= tail_row < max_y:
                    char = random.choice(chars)
                    try:
                        stdscr.addstr(tail_row, i, char, active_color)
                    except curses.error:
                        pass
            if row >= max_y - 1 or random.random() > 0.95:
                columns[i] = 0 
            else: 
                columns[i] += 1 

        stdscr.refresh()
        time.sleep(0.05)
if __name__ == "__main__":
    curses.wrapper(draw_matrix)

