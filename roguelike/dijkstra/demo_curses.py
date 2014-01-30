#!/usr/bin/env python3
from sys import argv
from dijkstra import Dungeon, Dijkstra
import curses

def main(stdscr, filename, playerX, playerY):
	curses.noecho()
	stdscr.keypad(True)

	for y, line in enumerate(open(filename, 'r').read()[:-1].split('\n')):
        	for x, char in enumerate(line):
            		if char == '%':
                		goalX, goalY = x, y

	dungeon = Dungeon(filename)
	dijkstra = Dijkstra(dungeon, goalX, goalY)
	dijkstra.find()
	
	while True:
		stdscr.clear()
		path = dijkstra.path(playerX, playerY)
		for y, line in enumerate(dungeon.cells):
			for x, cell in enumerate(line):
				if cell in path[1:]:
					stdscr.addch(y, x, '.')
				elif x == playerX and y == playerY:
					stdscr.addch(y, x, '@')
				else:
					stdscr.addch(y, x, cell.char)
		stdscr.addstr(len(dungeon.cells), 0, str(len(path)))
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
			if playerY > len(dungeon.cells)-1:
				playerY -= 1
	

if __name__ == '__main__':
	if len(argv) == 4:
		curses.wrapper(main, argv[1], *map(int, argv[2:]))
	else:
		print('Usage: %s' % argv[0])
