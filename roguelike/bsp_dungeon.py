#!/usr/bin/env python3
from random import choice, randrange
from functools import reduce


class Area:
    def __init__(self, start_x, start_y, end_x, end_y, split=None):
        '''Area of the dungeon, it contains two sub-maps'''
        self.start_x, self.start_y = start_x, start_y
        self.end_x, self.end_y = end_x, end_y
        self.split = split
        self.sub_a, self.sub_b = None, None


class Room:
    def __init__(self, area):
        '''Create a room into an area'''
        self.split = area.split

        '''if area.end_x - area.start_x > 6:  # If the area is wide enough
            self.start_x = area.start_x + randrange(0, 4)  # Randomize the room
            self.end_x = area.end_x - randrange(0, 4)
        else:
            self.start_x = area.start_x
            self.end_x = area.end_x

        if area.end_y - area.start_y > 6:  # If the area is high enough
            self.start_y = area.start_y + randrange(0, 4)  # Randomize the room
            self.end_y = area.end_y - randrange(0, 4)
        else:
            self.start_y = area.start_y
            self.end_y = area.end_y'''

        self.start_x, self.end_x = area.start_x, area.end_x
        self.start_y, self.end_y = area.start_y, area.end_y

    def check_limits(self, width, height):
        '''Check if the room is outside of the dungeon and correct the room'''
        if self.start_x <= 0:
            self.start_x = 1
        if self.start_y <= 1:
            self.start_y = 1
        if self.end_x > width - 1:
            self.end_x = width - 1
        if self.end_y > height - 1:
            self.end_y = height - 1


class Corridor:
    def __init__(self, room_a, room_b):
        if room_a.split == 'horizontal':
            print('hor')
            self.start_x = room_a.end_x
            self.start_y = (room_a.end_y - room_a.start_y) // 2 + room_a.start_y
            self.end_x = room_b.start_x
            self.end_y = self.start_y
        else:
            print('ver')
            self.start_x = (room_a.end_x - room_a.start_x) // 2 + room_a.start_x
            self.start_y = room_a.end_y
            self.end_x = self.start_x
            self.end_y = room_b.start_y


class Dungeon:
    def __init__(self, width, height):
        '''Initialize a dungeon'''
        self.width, self.height = width, height
        self.cells = [['#' for cell in range(self.width)]
                      for line in range(self.height)]

    def __repr__(self):
        '''Prints out the dungeon'''
        string = ''
        for line in self.cells:
            for char in line:
                string += char
            string += '\n'
        return string

    def create_tree(self, iterations):
        '''Return the tree of the areas in the dungeon'''

        def recursive_tree(area, n, max_vertical):
            n -= 1

            if n > 0:
                # Horizontal split
                if choice([True, False]) or max_vertical == 0:
                    middle = ((area.end_x - area.start_x) // 2
                              + area.start_x + randrange(-1, 2))
                    sub_a = Area(area.start_x, area.start_y,
                                 middle, area.end_y, 'horizontal')
                    sub_b = Area(middle + 1, area.start_y,
                                 area.end_x, area.end_y, 'horizontal')
                # Vertical split only if max_vertical != 0
                else:
                    max_vertical -= 1  # Decrement vertical splits counter
                    middle = ((area.end_y - area.start_y) // 2
                              + area.start_y + randrange(-1, 2))
                    sub_a = Area(area.start_x, area.start_y,
                                 area.end_x, middle, 'vertical')
                    sub_b = Area(area.start_x, middle + 1,
                                 area.end_x, area.end_y, 'vertical')

                area.sub_a = recursive_tree(sub_a, n, max_vertical)
                area.sub_b = recursive_tree(sub_b, n, max_vertical)

            return area

        return recursive_tree(Area(0, 0, self.width, self.height),
                              iterations, 2)

    def create_rooms(self, tree):
        rooms = []

        def recursive_rooms(area):
            if area.sub_a is not None and area.sub_b is not None:
                recursive_rooms(area.sub_a)
                recursive_rooms(area.sub_b)
            else:
                room = Room(area)
                room.check_limits(self.width, self.height)
                rooms.append(room)

        recursive_rooms(tree)
        return rooms

    def create_corridors(self, rooms):
        corridors = []

        def recursive_corridors(rooms):
            if len(rooms) != 2:
                recursive_corridors(rooms[:len(rooms) // 2])
                recursive_corridors(rooms[len(rooms) // 2:])
                room_a = rooms[0]
                room_b = rooms[len(rooms) // 2]

                corridor = Corridor(room_a, room_b)
                corridors.append(corridor)
            else:
                room_a = rooms[0]
                room_b = rooms[1]
                corridor = Corridor(room_a, room_b)
                corridors.append(corridor)

        recursive_corridors(rooms)
        return corridors

    def generate(self, iterations):
        tree = self.create_tree(iterations)
        rooms = self.create_rooms(tree)
        corridors = self.create_corridors(rooms)

        print(len(corridors))

        #for corridor in corridors:
        #    print(corridor.start_x, corridor.start_y)
        #    print(corridor.end_x, corridor.end_y)

        for y, line in enumerate(self.cells):
            for x, char in enumerate(line):
                for room in rooms:
                    if (room.start_x <= x < room.end_x and room.start_y <= y < room.end_y):
                        self.cells[y][x] = '.'
                for corridor in corridors:
                    if ((corridor.start_y <= y < corridor.end_y and corridor.start_x == x) or corridor.start_x <= x < corridor.end_x and corridor.start_y == y):
                        self.cells[y][x] = '+'


def main():
    d = Dungeon(80, 20)
    d.generate(5)
    print(d)

if __name__ == '__main__':
    main()
