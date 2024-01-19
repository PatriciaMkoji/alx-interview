#!/usr/bin/python3
""" a module for 0-minoperations"""


def minOperations(n):
    """
    it will get fewest # of operations needed to result in exactly n H characters
    """
    # all the outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # when the case is if n evenly divides by root
        if n % root == 0:

            # when case is the total even-divisions by root = total operations
            ops += root

            # when the set n to the remainder
            n = n / root

            # to reduce root to find remaining smaller vals that evenly-divide n
            root -= 1

            # to increment root until its evenly-divides n
            root += 1

            return ops
