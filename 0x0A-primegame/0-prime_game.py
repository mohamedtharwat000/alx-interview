#!/usr/bin/python3

"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None

    n = max(nums)
    primes = [True for _ in range(max(n + 1, 2))]
    primes[0], primes[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    primes_count = [0 for _ in range(max(n + 1, 2))]
    for i in range(1, len(primes_count)):
        primes_count[i] = primes_count[i - 1] + int(primes[i])

    player = 0
    for n in nums:
        player ^= primes_count[n] % 2 == 0

    return ["Maria", "Ben"][player]
