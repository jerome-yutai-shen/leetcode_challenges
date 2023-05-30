# -*- coding: utf-8 -*-
"""
Created on May 19 16:10:32 2022

@author: Jerome Yutai Shen

"""

"""
- Write a code to print the first N Fibonacci numbers.
A Fibonacci number is defined as x(n) = x(n-1) + x(n-2).
The first two Fibonacci numbers are 0 and 1.
"""

"""
This challenge is different from leetcode 509.
"""

def Fibonacci_iteration(n):
    a, b = 0, 1
    if n == 0:
        return a
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def fibonacci(n: int):
    """
    time complexity O(n)
    space complexity O(n)
    """
    fib_series = [0, 1] + [0] * (n - 2)
    if not n or n < 0:
        print(f"First {n} Fibonacci numbers: None")
        return

    if n > 2:
        for idx in range(2, n):
            fib_series[idx] = fib_series[idx - 2] + fib_series[idx - 1]
    print(f"First {n} Fibonacci numbers: {str(fib_series[:n])[1:-1] or None}")


def fibonacci1(n: int):
    """
    improved
    time complexity O(n)
    space complexity O(1)
    """
    msg = f"First {n} Fibonacci numbers: "
    if not n or n < 0:
        print(msg + "None")
        return
    fib_series = [0, 1]
    if n <= 2:
        msg += str(fib_series[:n])[1:-1]
    else:
        msg += str(fib_series[:2])[1:-1]
        for idx in range(2, n):
            fib_series[idx % 2] = fib_series[0] + fib_series[1]
            msg += f", {str(fib_series[idx % 2])}"
    print(msg)


def fibonacci2(n: int):
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


def fibonacci3(n: int):
    """
    based on the matrix representation, as shown in wikipedia : https://en.wikipedia.org/wiki/Fibonacci_number
    """
    import numpy as np
    fibonacci_square_matrix = np.matrix([[1, 1], [1, 0]])

    print(np.power(fibonacci_square_matrix, n))


if __name__ == "__main__":
    for n in range(-2, 7):
        fibonacci(n)
        fibonacci1(n)
        fibonacci2(n)