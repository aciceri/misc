#!/usr/bin/env python3
from random import choice, randrange


class Area:
    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x, self.start_y = start_x, start_y
        self.end_x, self.end_y = end_x, end_y
        self.sub_a, self.sub_b = None, None

    def __repr__(self):
        return '%d,%d:%d,%d' % (self.start_x, self.start_y,
                                self.end_x, self.end_y)


class Room:
    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x + randrange(4) + 1
        self.start_y = start_y + randrange(4) + 1
        self.end_x = end_x - randrange(4) - 1
        self.end_y = end_y - randrange(4) - 1


class Dungeon:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.cells = [['#' for cell in range(self.width)]
                      for line in range(self.height)]

    def __repr__(self):
        string = ''
        for line in self.cells:
            for char in line:
                string += char
            string += '\n'
        return string

    def create_tree(self, iterations):
        def recursive_tree(area, n):
            n -= 1

            if n > 0:
                if choice([True, False]):  # Horizontal split
                    middle = (area.end_x - area.start_x) // 2 + 3 - randrange(6)
                    sub_a = Area(area.start_x, area.start_y,
                                 middle, area.end_y)
                    sub_b = Area(middle, area.start_y,
                                 area.end_x, area.end_y)
                else:  # Vertical split
                    middle = (area.end_y - area.start_y) // 2 + 3 - randrange(6)
                    sub_a = Area(area.start_x, area.start_y,
                                 area.end_x, middle)
                    sub_b = Area(area.start_x, middle,
                                 area.end_x, area.end_y)

                area.sub_a = recursive_tree(sub_a, n)
                area.sub_b = recursive_tree(sub_b, n)

            return area

        return recursive_tree(Area(0, 0, self.width, self.height), iterations)

    def create_rooms(self, tree):
        rooms = []

        def recursive_rooms(tree):
            if tree.sub_a is not None and tree.sub_b is not None:
                recursive_rooms(tree.sub_a)
                recursive_rooms(tree.sub_b)
            else:
                return rooms.append(Room(tree.start_x, tree.start_y,
                                         tree.end_x, tree.end_y))

        recursive_rooms(tree)
        return rooms

    def generate(self, iterations):
        self.tree = self.create_tree(iterations)
        self.rooms = self.create_rooms(self.tree)
        for room in self.rooms:
            print(room.start_x, room.start_y)
            print(room.end_x, room.end_y)
        for y, line in enumerate(self.cells):
            for x, char in enumerate(line):
                for room in self.rooms:
                    if (room.start_x < x < room.end_x - 1 and room.start_y < y < room.end_y - 1):
                        self.cells[y][x] = '.'


def main():
    d = Dungeon(80, 30)
    d.generate(3)
    print(d)

if __name__ == '__main__':
    main()
