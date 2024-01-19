#!/usr/bin/python3

"""
minOperations
"""


def minOperations(n) -> int:
    """ minOperations """
    if n <= 1:
        return 0
    i = 0
    count = i
    while i <= n:
        if n % i == 0:
            count += i
            n = n / i
        else:
            i += 1
    return count
