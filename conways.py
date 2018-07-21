# /usr/bin/python3

import random
from time import sleep


def create_grid(rows, cols):
	# Create finite grid and set cell state randomly.
	# Grid is padded around with 0s. 
	grid = []
	for i in range(rows):
		grid.append([])
		for j in range(cols):
			if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
				grid[i].append(0)
			else:
				grid[i].append(random.randrange(0, 2))

	return grid


def count_neighbors(grid, row, col):
	sum = 0

	sum += grid[row-1][col-1]
	sum += grid[row-1][col]
	sum += grid[row-1][col+1]
	sum += grid[row][col-1]
	sum += grid[row][col+1]
	sum += grid[row+1][col-1]
	sum += grid[row+1][col]
	sum += grid[row+1][col+1]
	
	return sum


def display_grid(grid):
	for row in grid:
		for val in row:
			if val:
				print('#', end='')
			else:
				print('.', end='')
		print()
	print()


def main():
	ROWS = 50
	COLS = 50

	curr_grid = create_grid(ROWS, COLS)
	next_grid = [[0 for j in range(COLS)] for i in range(ROWS)]		

	display_grid(curr_grid)

	# Begin life simulation. Apply rules and update grid accordingly.
	while True:

		for i, row in enumerate(curr_grid, 1):
			for j, val in enumerate(row, 1):
				# Ignore the padded 0s
				if j >= COLS - 1 or i >= ROWS - 1:
					continue 
				else:
					number_of_neighbors = count_neighbors(curr_grid, i, j)

					# Cell lives on to next generation
					if curr_grid[i][j] == 1 and number_of_neighbors == 2 or curr_grid[i][j] == 1 and number_of_neighbors == 3:
						next_grid[i][j] = 1
					# Birth of a cell
					elif curr_grid[i][j] == 0 and number_of_neighbors == 3:
						next_grid[i][j] = 1
					# Death of a cell
					else:
						next_grid[i][j] = 0

		sleep(1)
		display_grid(next_grid)

		curr_grid = next_grid
		next_grid = [[0 for j in range(COLS)] for i in range(ROWS)]	


if __name__ == '__main__':
	main()