from heapq import heapify, heappush, heappop


class Cell:
    def __init__(self, x, y, dist):
        self.x, self.y = x, y
        self.dist = dist

    def __repr__(self):
        return str(self.dist)

    def __lt__(self, other):
        return self.dist < other.dist


def main():
    l = []
    for y in range(10):
        for x in range(10):
            l.append(Cell(x, y, x + y))
    heapify(l)

    for cell in l:
        print(cell.dist)


if __name__ == '__main__':
    main()
