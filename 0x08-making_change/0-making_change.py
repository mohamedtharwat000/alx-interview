#!/usr/bin/python3

"""Fewest number of coins needed to meet a given amount."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet a given amount."""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    result = []

    for coin in coins:
        while coin <= total:
            result.append(coin)
            total -= coin

    if sum(result) != total + sum(result):
        return -1

    return len(result)
