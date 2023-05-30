# -*- coding: utf-8 -*-
"""
Created on May 21 23:00:24 2022

@author: Jerome Yutai Shen

"""


def is_palindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverted_num = 0
    while x > reverted_num:
        reverted_num = reverted_num * 10 + x % 10
        x //= 10 # in 7 reverse integer, can't use //, must use int(x / abs(divisor)), why?
        # because python // is different from C++/Java when x is negative

    return x == reverted_num or x == int(reverted_num / 10)


if __name__ == "__main__":
    print(is_palindrome(121))
