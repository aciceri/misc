#!/usr/bin/env python3
from random import choice


class Area:
    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x, self.start_y = start_x, start_y
        self.end_x, self.end_y = end_x, end_y
        self.sub_a, self.sub_b = None, None
        self.division = None

    def split(self, division):
        if division:  # Horizontal split
            self.division = 'horizontal'
            middle = self.start_y + (self.end_y - self.start_y) // 2
            self.sub_a = Area(self.start_x, self.start_y,
                              self.end_x, middle)
            self.sub_b = Area(self.start_x, middle + 1,
                              self.end_x, self.end_y)

        else:  # Vertical split
            self.division = 'vertical'
            middle = self.start_x + (self.end_x - self.start_x) // 2
            middle += choice(range(-3, 4))
            self.sub_a = Area(self.start_x, self.start_y,
                              middle, self.end_y)
            self.sub_b = Area(middle + 1, self.start_y,
                              self.end_x, self.end_y)


class BspDungeon:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.cells = [[False for x in range(self.width)] for y in range(self.height)]

    def draw(self):
        for line in self.cells:
            for cell in line:
                if cell:
                    print('.', end='')
                else:
                    print('#', end='')
            print()

    def split(self, depth):
        def recursive_split(area, depth, max_horizontal, max_vertical):
            if depth:
                if max_vertical and max_horizontal:
                    division = choice([True, False])
                elif not max_vertical:
                    division = True
                elif not max_horizontal:
                    division = False

                if division:
                    max_horizontal -= 1
                else:
                    max_vertical -= 1

                area.split(division)  # Random direction
                recursive_split(area.sub_a, depth - 1, max_horizontal, max_vertical)
                recursive_split(area.sub_b, depth - 1, max_horizontal, max_vertical)

                return area

        area = Area(0, 0, self.width - 1, self.height - 1)
        return recursive_split(area, depth, 2, 4)

    def dig_rooms(self, area, division=None):
        if area.sub_a and area.sub_b:
            self.dig_rooms(area.sub_a, area.division)
            self.dig_rooms(area.sub_b, area.division)
        else:
              for y in range(area.start_y, area.end_y):
                for x in range(area.start_x, area.end_x):
                    self.cells[y][x] = True

    def dig_corridors(self, area):
        if area.sub_a and area.sub_b:
            if area.division == 'horizontal':
                x = choice(range(area.sub_a.start_x + 1, area.sub_a.end_x - 1))
                while not self.cells[area.sub_a.end_y - 1][x] or not self.cells[area.sub_b.start_y + 1][x]:
                    x = choice(range(area.sub_a.start_x + 1, area.sub_a.end_x - 1))
                y = area.sub_a.end_y
                while y < self.height - 1 and not self.cells[y][x]:
                    self.cells[y][x] = True
                    y += 1
            else:
                y = choice(range(area.sub_a.start_y + 1, area.sub_a.end_y - 1))
                while not self.cells[y][area.sub_a.end_x - 1] or not self.cells[y][area.sub_b.start_x + 1]:
                    y = choice(range(area.sub_a.start_y + 1, area.sub_a.end_y - 1))
                x = area.sub_a.end_x
                while x < self.width - 1 and not self.cells[y][x]:
                    self.cells[y][x] = True
                    x += 1

            self.dig_corridors(area.sub_a)
            self.dig_corridors(area.sub_b)

    def generate(self, depth):
        main_area = self.split(depth)
        self.dig_rooms(main_area)
        self.dig_corridors(main_area)


def main():
    dungeon = BspDungeon(80, 20)
    dungeon.generate(4)
    dungeon.draw()


if __name__ == '__main__':
    try:
        main()
    except:
        print(':(')
