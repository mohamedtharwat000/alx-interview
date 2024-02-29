#!/usr/bin/python3

"""Fewest number of coins needed to meet a given amount."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet a given amount."""
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
