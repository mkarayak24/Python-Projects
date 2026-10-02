import random
import curses
import time
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Test!")
    stdscr.addstr("\nPress any key to begin...")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target_text, current_text, wpm=0):
    stdscr.addstr(target_text)
    stdscr.addstr(1, 0, f"WPM: {wpm}")  

    for i, char in enumerate(current_text):
        correct_char = target_text[i]
        if char == correct_char:
            stdscr.addstr(0, i, char, curses.color_pair(1))
        else:
            stdscr.addstr(0, i, char, curses.color_pair(2))

def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
    return random.choice(lines).strip()

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    start_time = time.time()
    wpm = 0
    stdscr.nodelay(True)

    while True:
        elapsed_time = max(time.time() - start_time, 1)
        wpm = len(current_text) / (elapsed_time / 60)
        wpm = round(wpm / 5)
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  
            break

        if key in ('KEY_BACKSPACE', '\b', '\x7f'):
            if len (current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "Test completed! Press ESC key to exit.")
        stdscr.getkey()
        if ord(stdscr.getkey()) == 27:  
            break

wrapper(main)
