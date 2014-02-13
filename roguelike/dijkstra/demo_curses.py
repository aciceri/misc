#!/usr/bin/env python3
from sys import argv
from dijkstra import Dungeon, Dijkstra
import curses


def main(stdscr, filename, player_x, player_y):
    curses.noecho()
    stdscr.keypad(True)

    for y, line in enumerate(open(filename, 'r').read()[:-1].split('\n')):
        for x, char in enumerate(line):
            if char == 'A':
                goal_x, goal_y = x, y

    dungeon = Dungeon(filename)
    dijkstra = Dijkstra(dungeon, goal_x, goal_y)
    dijkstra.find()

    while True:
        stdscr.clear()

        #dijkstra.find()
        path = list(dijkstra.pathFrom(player_x, player_y))

        for y, line in enumerate(dungeon.cells):
            for x, cell in enumerate(line):
                if cell in path[1:]:
                    stdscr.addch(y, x, '.')
                elif x == player_x and y == player_y:
                    stdscr.addch(y, x, '@')
                else:
                    stdscr.addch(y, x, cell.char)
        if len(path) != 0:
            dist = path[0].dist
        else:
            dist = float('inf')

        stdscr.addstr(20, 0, 'A: %s' % str(dist))

        key = stdscr.getkey()
        if key == 'q':
            break
        elif key == 'h' or key == 'a':
            player_x -= 1
            if player_x < 0:
                player_x += 1
        elif key == 'l' or key == 'd':
            player_x += 1
            if player_x >= len(dungeon.cells[0]):
                player_x -= 1
        elif key == 'k' or key == 'w':
            player_y -= 1
            if player_y < 0:
                player_y += 1
        elif key == 'j' or key == 's':
            player_y += 1
            if player_y > len(dungeon.cells) - 1:
                player_y -= 1


if __name__ == '__main__':
    if len(argv) == 4:
        curses.wrapper(main, argv[1], *map(int, argv[2:]))
    else:
        print('Usage: %s FILENAME X Y' % argv[0])
