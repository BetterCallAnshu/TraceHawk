import curses
import random
import time

PIPE_WIDTH = 3
GAP_SIZE = 8
BIRD_CHAR = "Q>"
FLAP_HEIGHT = 2
GRAVITY = 0.5
TICK_RATE = 0.1

def draw_bird(win, y, x):
    try:
        win.addstr(int(y), int(x), BIRD_CHAR)
    except curses.error:
        pass

def draw_pipe(win, pipe_x, gap_y, max_y):
    height, width = win.getmaxyx()
    if pipe_x < 0 or pipe_x + PIPE_WIDTH >= width:
        return

    for y in range(max_y):
        if 0 <= y < height and not (gap_y <= y < gap_y + GAP_SIZE):
            try:
                win.addstr(y, pipe_x, "|" * PIPE_WIDTH)
            except curses.error:
                pass

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(0)

    sh, sw = stdscr.getmaxyx()
    bird_y = sh // 2
    bird_x = sw // 4
    velocity = -3

    pipes = []
    score = 0

    for i in range(3):
        x = sw + i * 30
        gap_y = random.randint(5, sh - GAP_SIZE - 5)
        pipes.append([x, gap_y])

    while True:
        stdscr.clear()

        draw_bird(stdscr, bird_y, bird_x)

        key = stdscr.getch()
        if key == ord(" ") or key == curses.KEY_UP:
            velocity = -FLAP_HEIGHT

        velocity += GRAVITY
        bird_y += velocity

        for pipe in pipes:
            pipe[0] -= 1
            draw_pipe(stdscr, pipe[0], pipe[1], sh)

        for pipe in pipes:
            if pipe[0] < bird_x < pipe[0] + PIPE_WIDTH:
                if not (pipe[1] <= bird_y < pipe[1] + GAP_SIZE):
                    stdscr.addstr(sh // 2, sw // 2 - 10, f"GAME OVER! Score: {score}")
                    stdscr.refresh()
                    time.sleep(2)
                    return

        if bird_y < 0 or bird_y >= sh:
            stdscr.addstr(sh // 2, sw // 2 - 10, f"GAME OVER! Score: {score}")
            stdscr.refresh()
            time.sleep(2)
            return

        if pipes[0][0] < -PIPE_WIDTH:
            pipes.pop(0)
            new_x = pipes[-1][0] + 30
            new_gap_y = random.randint(5, sh - GAP_SIZE - 5)
            pipes.append([new_x, new_gap_y])
            score += 1

        stdscr.addstr(1, 2, f"Score: {score}")

        stdscr.refresh()
        time.sleep(TICK_RATE)


if __name__ == "__main__":
    curses.wrapper(main)
