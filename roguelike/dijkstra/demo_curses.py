#!/usr/bin/env python3
from sys import argv
from dijkstra import Dungeon, Dijkstra
import curses


def main(stdscr, filename, playerX, playerY):
    curses.noecho()
    stdscr.keypad(True)

    for y, line in enumerate(open(filename, 'r').read()[:-1].split('\n')):
        for x, char in enumerate(line):
            if char == 'A':
                goalAX, goalAY = x, y
            elif char == 'B':
                goalBX, goalBY = x, y
            elif char == 'C':
                goalCX, goalCY = x, y
            elif char == 'D':
                goalDX, goalDY = x, y
            elif char == 'E':
                goalEX, goalEY = x, y

    dungeon = Dungeon(filename)

    while True:
        stdscr.clear()

        dijkstra = Dijkstra(dungeon, playerX, playerY)
        dijkstra.find()
        pathA = list(dijkstra.pathFrom(goalAX, goalAY))
        #pathB = list(dijkstra.pathFrom(goalBX, goalBY))

        for y, line in enumerate(dungeon.cells):
            for x, cell in enumerate(line):
                if cell in pathA[1:]:
                    stdscr.addch(y, x, '.')
                elif x == playerX and y == playerY:
                    stdscr.addch(y, x, '@')
                else:
                    stdscr.addch(y, x, cell.char)

        distA = len([c.dist for c in pathA] if pathA else [0])
        #distB = len([c.dist for c in pathB] if pathB else [0])

        stdscr.addstr(len(dungeon.cells), 0, 'A: %s' % str(distA))
        #stdscr.addstr(len(dungeon.cells), 10, 'B: %s' % str(distB))

        key = stdscr.getkey()
        if key == 'q':
            break
        elif key == 'h' or key == 'a':
            playerX -= 1
            if playerX < 0:
                playerX += 1
        elif key == 'l' or key == 'd':
            playerX += 1
            if playerX >= len(dungeon.cells[0]):
                playerX -= 1
        elif key == 'k' or key == 'w':
            playerY -= 1
            if playerY < 0:
                playerY += 1
        elif key == 'j' or key == 's':
            playerY += 1
            if playerY > len(dungeon.cells) - 1:
                playerY -= 1


if __name__ == '__main__':
    if len(argv) == 4:
        curses.wrapper(main, argv[1], *map(int, argv[2:]))
    else:
        print('Usage: %s X Y' % argv[0])
