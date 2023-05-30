# -*- coding: utf-8 -*-
"""
Created on Apr 18 15:19:28 2023

@author: Jerome Yutai Shen

"""

def Fibonacci_iteration(n: int) -> int:
    a, b = 0, 1
    if n == 0:
        return a
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def fibonacci1(n: int) -> int:
    """
    improved
    time complexity O(n)
    space complexity O(1)
    """
    if n <= 1:
        return n

    fib_series = [0, 1]
    for idx in range(2, n):
        fib_series[idx % 2] = fib_series[0] + fib_series[1]

    print(idx, fib_series)
    return fib_series[0]


def fibonacci2(n: int) -> int:
    """
    based on the matrix representation, as shown in wikipedia : https://en.wikipedia.org/wiki/Fibonacci_number
    """
    import numpy as np
    fibonacci_square_matrix = np.matrix([[1, 1], [1, 0]])
    fib_series = [0, 1] + [0] * (n - 2)

    if not n or n < 0:
        print(f"First {n} Fibonacci numbers: None")
        return

    if n >= 3:
        fib_series[2] = fibonacci_square_matrix[0, 0]
        fib_mat_idx = np.matrix([[1, 1], [1, 0]])
        for idx in range(3, n):
            fib_mat_idx *= fibonacci_square_matrix
            fib_series[idx] = fib_mat_idx[0, 0]
    print(f"First {n} Fibonacci numbers: {str(fib_series[:n])[1:-1] or None}")


if __name__ == "__main__":
    for num in range(8, 51):
        print(fibonacci1(num))