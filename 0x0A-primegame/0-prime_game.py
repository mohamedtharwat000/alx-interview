#!/usr/bin/python3

"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    if x < 1 or not nums:
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
        """Play a round of the prime game"""
        if max_n < 2:
            return None
        numbers = [(n, int(is_prime(n))) for n in range(1, max_n + 1)]
        turn = False
        for n in numbers:
            if n[1]:
                turn = not turn
                for j in numbers[n[0]:]:
                    if j[0] % n[0] == 0:
                        numbers.pop(numbers.index(j))
        return turn

    wins = [0, 0]
    for max_n in nums:
        winer = play_game(max_n)
        if winer:
            wins[winer] += 1

    if wins[0] == wins[1]:
        return None
    else:
        return ['Maria', 'Ben'][wins.index(max(wins))]
