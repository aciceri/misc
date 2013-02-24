#!/usr/bin/python3
from sys import argv
from random import choice


class World:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.cells = [[True if choice(range(100)) < 40 else False
                       for row in range(self.height)]
                      for column in range(self.width)]

    def neighbours(self, x, y):
        counter = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if ((0 <= x + i < self.width) and (0 <= y + j < self.height) and not (i == 0 and j == 0)):
                    if self.cells[x + i][y + j]:
                        counter += 1
        return counter

    def evolve(self, times):
        cells_tmp = [[False for row in range(self.height)] for column in range(self.width)]
        for _ in range(times):
            for x in range(self.width):
                for y in range(self.height):
                    if self.cells[x][y]:
                        if self.neighbours(x, y) >= 4:
                            cells_tmp[x][y] = True
                    else:
                        if self.neighbours(x, y) >= 5:
                            cells_tmp[x][y] = True
            self.cells = cells_tmp

    def draw(self):
        s = ''
        for y in range(self.height):
            for x in range(self.width):
                if self.cells[x][y]:
                    s += '#'
                else:
                    s += '.'
            s += '\n'
        print(s)

if __name__ == '__main__':
    world = World(int(argv[1]), int(argv[2]))
    world.evolve(int(argv[3]))
    world.draw()
