#!/usr/bin/python3

"""Fewest number of coins needed to meet a given amount."""

def make_change(coins, amount):
    """Return the fewest number of coins needed to meet a given amount."""
    if amount == 0:
        return 0
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while coin <= amount:
            result.append(coin)
            amount -= coin
    return len(result)
