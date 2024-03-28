# -*- coding: utf-8 -*-
"""
Created on Aug 31 16:35:51 2023

@author: Jerome Yutai Shen

"""
import numpy as np

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Initialize numbers[0] and numbers[1] as False because 0 and 1 are not prime.
        # Initialze numbers[2] through numbers[n-1] as True because we assume each number
        # is prime until we find a prime number (p) that is a divisor of the number
        numbers = [False, False] + [True] * (n - 2)
        for p in range(2, int(np.sqrt(n)) + 1):
            if numbers[p]:
                # Set all multiples of p to false because they are not prime.
                for multiple in range(p * p, n, p):
                    numbers[multiple] = False

        # numbers[index] will only be true where index is a prime number
        # return the number of indices whose value is true.
        return sum(numbers)