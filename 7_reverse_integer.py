# -*- coding: utf-8 -*-
"""
Created on May 21 13:34:26 2022

@author: Jerome Yutai Shen

"""


def check_overflow(a: int, b: int, num_bit: int = 32) -> bool:
    int_max = pow(2, (num_bit - 1)) - 1
    if a > int_max / 10 or (a == int_max / 10 and b > 7):
        return True

    int_min = pow(-2, (num_bit - 1))
    if a < int_min / 10 or (a == int_min / 10 and b < -8):
        return True

    return False

def reverse(x: int)-> int:
    result = 0
    divisor = 10 if x > 0 else -10 # in python, -123 % 10 ==  7. -1 % 10 == 9

    while x != 0:
        pop = x % divisor
        if_over_flow = check_overflow(result, pop)
        if if_over_flow:
            return int(not if_over_flow)
        result = result * abs(divisor) + x % divisor
        x = int(x / abs(divisor)) # in 9 palindrome number, can use //, here can't use // must use int(x / abs(divisor)), why?
        # because python // is different from C++/Java when x is negative

    return result


if __name__ == "__main__":
    print(reverse(321))
    print(reverse(-123))
    print(reverse(1534236469))
