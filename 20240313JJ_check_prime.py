# -*- coding: utf-8 -*-
"""
Created on Mar 13 16:28:16 2024

@author: Jerome Yutai Shen

"""



def func(num: int) -> bool:
    if num < 2:
        return False
    if num == 4:
        return False
    elif num in {2, 3, 5}:
        return True

    assert num > 5
    if num % 2 ==0 or num % 3 == 0 or num % 5 == 0:
        return False

    max_factor = num // 2 + 2
    for factor in range(5, max_factor, 2):
        if num % factor == 0:
            # print(f"{num} has a larger than 5 factor {factor}")
            return False

    return True


def is_prime2(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    for x in range(-1, 200000):
        # is_prime = func(x)
        # print(f"{x}: {is_prime}")
        assert(func(x) == is_prime2(x))

