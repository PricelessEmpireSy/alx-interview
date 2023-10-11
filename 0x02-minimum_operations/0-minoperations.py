#!/usr/bin/python3

"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return: number of min operations
    """

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        if n % factor == 0:
            operations += factor
            n = n // factor
        else:
            factor += 1

    return operations
