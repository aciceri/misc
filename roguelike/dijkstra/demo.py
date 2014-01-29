#!/usr/bin/env python3
from sys import argv
from dijkstra import Dungeon, Dijkstra


def main(filename):
    dungeon = Dungeon(filename)

    for y, line in enumerate(open(filename, 'r').read()[:-1].split('\n')):
        for x, char in enumerate(line):
            if char == 'A':
                Ax, Ay = x, y
            elif char == 'B':
                Bx, By = x, y

    dijkstra = Dijkstra(dungeon, Ax, Ay)
    dijkstra.find()
    path = dijkstra.path(Bx, By)
    dijkstra.show(path)


if __name__ == '__main__':
    if len(argv) == 2:
        main(argv[1])
    else:
        print('Usage: %s FILE' % argv[0])
