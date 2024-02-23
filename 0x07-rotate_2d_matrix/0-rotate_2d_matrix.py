#!/usr/bin/python3

"""rotate_2d_matrix.py: Rotate a 2D matrix by 90 degrees in place."""


def rotate_2d_matrix(matrix: list[list[int]]) -> None:
    """Rotate a 2D matrix by 90 degrees in place."""
    length = len(matrix)
    for row in range(length // 2):
        _row = length - row - 1
        for column in range(row, _row):
            _column = length - column - 1
            temp = matrix[row][column]
            matrix[row][column] = matrix[_column][row]
            matrix[_column][row] = matrix[_row][_column]
            matrix[_row][_column] = matrix[column][_row]
            matrix[column][_row] = temp
