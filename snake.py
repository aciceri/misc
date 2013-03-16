#!/usr/bin/env python3

import curses
from time import sleep


class Screen:
    def __init__(self, fps):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(False)
        self.stdscr.keypad(True)
        self.stdscr.timeout(int(1000 / fps))

    def get_char(self):
        char = self.stdscr.getch()
        if char != -1:
            return chr(char)

    def put_char(self, x, y, char):
        self.stdscr.addch(y, x, ord(char))

    def update(self):
        self.stdscr.refresh()

    def clear(self):
        self.stdscr.clear()

    def draw_snake(self, snake):
        for block in snake.body:
            x, y = block
            self.put_char(x, y, '0')

    def get_size(self):
        return self.stdscr.getmaxyx()

    def destroy(self):
        curses.endwin()


class Snake:
    def __init__(self, start_x, start_y, lenght, scr_width, scr_height):
        self.scr_width, self.scr_height = scr_width, scr_height
        self.body = [(start_x + x, start_y) for x in range(lenght)]
        self.alive = True
        self.direction = 'LEFT'

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == 'UP':
            if head_y == 0:
                delta = (0, self.scr_height - 1)
            else:
                delta = (0, -1)

        elif self.direction == 'LEFT':
            if head_x == 0:
                delta = (self.scr_width - 1, 0)
            else:
                delta = (-1, 0)

        elif self.direction == 'DOWN':
            if head_y == self.scr_height - 1:
                delta = (0, -(self.scr_height - 1))
            else:
                delta = (0, 1)

        elif self.direction == 'RIGHT':
            if head_x == self.scr_width - 1:
                delta = (-(self.scr_width - 1), 0)
            else:
                delta = (1, 0)

        self.body.pop()
        self.body.insert(0, tuple(map(sum, zip(self.body[0], delta))))

    def is_crashed(self):
        if self.body[0] in self.body[1:]:
            return True
        return False


class Game:
    def __init__(self):
        self.screen = Screen(12)
        height, width = self.screen.get_size()
        self.snake = Snake(5, 5, 70, width, height)
        self.still_play = True

    def play(self):
        while self.still_play:
            self.read_keyboard()  # Delay
            self.screen.clear()

            self.snake.move()
            if self.snake.is_crashed():
                self.still_play = False


            self.screen.draw_snake(self.snake)
            self.screen.update()

        self.exit()

    def exit(self):
        sleep(0.5)
        self.screen.destroy()
        print('Gioco terminato con successo :)')
        print('Hai fatto %d punti ' % len(self.snake.body))

    def read_keyboard(self):
        char = self.screen.get_char()

        if char == 'w':
            self.snake.direction = 'UP'
        elif char == 'a':
            self.snake.direction = 'LEFT'
        elif char == 's':
            self.snake.direction = 'DOWN'
        elif char == 'd':
            self.snake.direction = 'RIGHT'
        elif char == 'q':
            self.still_play = False


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
