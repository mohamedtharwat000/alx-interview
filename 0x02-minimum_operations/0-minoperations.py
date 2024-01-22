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

    for i in range(2, n + 1):
        for _ in range(result // i):
            if result % i == 0:
                operations += i
                result //= i

    return operations
