class Cell:
    def __init__(self, x, y, char):
        self.x, self.y = x, y
        self.char = char
        self.walkable = False if self.char == '#' else True
        self.parent = None
        self.dist = float('inf')

    def __repr__(self):
        return self.char

    def __lt__(self, other):
        return self.dist < other.dist


class Dungeon:
    def __init__(self, filename):
        self.string = open(filename, 'r').read()[:-1]  # Last \n
        self.cells = []

        for y, line in enumerate(self.string.split('\n')):
            self.cells.append([])
            for x, char in enumerate(line):
                self.cells[y].append(Cell(x, y, char))

        self.height, self.width = len(self.cells), len(self.cells[0])

    def __repr__(self):
        return self.string

    def adjacent(self, cell):
        deltas = ((0, 1), (1, 1), (1, 0), (1, -1),
                  (0, -1), (-1, -1), (-1, 0), (-1, 1))
        neighbours = []
        valid = lambda cell, dx, dy: (
            (0 <= cell.x + dx < self.width)  # Inside the dungeon (x)
            and (0 <= cell.y + dy < self.height)  # As before (y)
            and self.cells[cell.y + dy][cell.x + dx].walkable)  # Walkable

        for delta_x, delta_y in deltas:
            if valid(cell, delta_x, delta_y):
                #If it's walkable and inside the dungeon
                tmp_cell = self.cells[cell.y + delta_y][cell.x + delta_x]
                neighbours.append(tmp_cell)

        return neighbours

    def distance(self, cell_a, cell_b):
        if cell_a.x == cell_b.x or cell_a.y == cell_b.y:
            return cell_a.dist + 10
        else:
            return cell_a.dist + 14


class Dijkstra:
    def __init__(self, dungeon, x, y):
        self.dungeon = dungeon
        self.start_x, self.start_y = x, y  # Coordinates of the starting cell

    def show(self, path):
        string = ''
        for line in self.dungeon.cells:
            for cell in line:
                if cell in path[1:]:
                    string += '.'
                else:
                    string += str(cell)
            string += '\n'
        print(string)

    def find(self):
        self.dungeon.cells[self.start_y][self.start_x].dist = 0
        q = [cell for c in self.dungeon.cells for cell in c]

        while q:  # While q is not empty
            u = min(q)  # Closest cell
            q.remove(u)

            for cell in self.dungeon.adjacent(u):
                dist = self.dungeon.distance(u, cell)
                if dist < cell.dist:
                    cell.dist = dist
                    cell.parent = u

    def path(self, x, y):
        cell = self.dungeon.cells[y][x]
        cells = []
        while cell.parent is not None:
            cells.append(cell)
            cell = cell.parent
        return cells
