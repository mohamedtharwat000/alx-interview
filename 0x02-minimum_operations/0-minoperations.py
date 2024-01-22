#!/usr/bin/python3

"""
minOperations
"""


def minOperations(n) -> int:
    """ minOperations """
    if n <= 1:
        return 0

    result = n
    operations = 0

    while result % 2 == 0:
        operations += 2
        result //= 2

    for i in range(3, result + 1, 2):
        while result % i == 0:
            operations += i
            result //= i

    return operations

print(minOperations(8))
