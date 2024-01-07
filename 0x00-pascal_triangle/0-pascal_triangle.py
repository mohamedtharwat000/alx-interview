#!/usr/bin/python3

"""
Pascal_Triangle
"""


def pascal_triangle(n):
    """
    pascal_triangle
    arg:
        n: int
    return pascal triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for row_num in range(1, n):
        row = [1] * (row_num + 1)
        triangle.append(row)
        for i in range(1, len(row) - 1):
            row[i] = triangle[row_num - 1][i - 1] + triangle[row_num - 1][i]

    return triangle
