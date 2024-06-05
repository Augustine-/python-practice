import curses

def main(stdscr):
    curses.curs_set(0) # Hide cursor
    stdscr.clear() # Clear screen
    # stdscr.refresh() # ?

    display_value = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Display Value: {display_value}")
        stdscr.addstr(2, 0, f"'W' to increase, 'S' to decrease, 'Q' to quit.")
        # stdscr.refresh()

        key = stdscr.getch()

        if key == ord('w') or key == ord('W'):
            display_value += 1
        elif key == ord('s') or key == ord('S'):
            display_value -= 1
        elif key == ord('q') or key == ord('Q'):
            break

curses.wrapper(main)