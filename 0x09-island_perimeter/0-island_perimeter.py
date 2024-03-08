#!/usr/bin/python3

"""returns the perimeter of the island"""


def island_perimeter(grid):
    """returns the perimeter of the island"""
    perimeter = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            if i == 0 or grid[i - 1][j] == 0:
                perimeter += 1
            if i == len(grid) - 1 or grid[i + 1][j] == 0:
                perimeter += 1
            if j == 0 or grid[i][j - 1] == 0:
                perimeter += 1
            if j == len(row) - 1 or grid[i][j + 1] == 0:
                perimeter += 1
    return perimeter
