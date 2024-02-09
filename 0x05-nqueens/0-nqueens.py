#!/usr/bin/python3
"""0. N queens"""


import sys


class Queen:
    '''Queen class'''

    def __init__(self, row, col):
        self.row = row
        self.col = col


def is_safe(queens, new_row):
    '''Check if a queen can be placed in the given row without attacks'''
    for queen in queens:
        if queen.row == new_row or abs(queen.col - queens[-1].col) == abs(new_row - queens[-1].row):
            return False
    return True


def solve_n_queens(n, col=0, queens=[]):
    '''Base case: all queens placed successfully'''
    if col == n:
        solution = [q.col for q in queens]
        print(solution)
        return

    for row in range(n):
        if is_safe(queens, row):
            queens.append(Queen(row, col))
            solve_n_queens(n, col + 1, queens)
            queens.pop()  # Backtrack


def main():
    '''Parse and validate input arguments'''
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    print("Solutions:")
    solve_n_queens(n)


if __name__ == "__main__":
    main()
