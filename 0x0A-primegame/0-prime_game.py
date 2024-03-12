#!/usr/bin/python3

"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    if x < 1 or not nums:
        return None

    for n in nums:
        if n < 0:
            return None

    def is_prime(number):
        """Check if a number is prime"""
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def play_game(max_n):
        """Play a round of the prime game and return the winner"""
        numbers = [(n, int(is_prime(n))) for n in range(1, max_n + 1)]
        turn = True
        for n in numbers:
            if n and n[1]:
                turn = not turn
                for j in numbers:
                    if j and j[0] % n[0] == 0:
                        numbers[numbers.index(j)] = None
        return int(turn)

    wins = [0, 0]
    for max_n in nums:
        wineer = play_game(max_n)
        wins[wineer] += 1

    if wins[0] == wins[1]:
        return None
    else:
        return ['Maria', 'Ben'][wins.index(max(wins))]
