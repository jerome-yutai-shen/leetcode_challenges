# -*- coding: utf-8 -*-
"""
Created on May 21 16:16:18 2022

@author: Jerome Yutai Shen

C language: the atoi() function converts a character string to an integer value.

"""

INT_MAX = pow(2, 31) - 1
INT_MIN = -pow(2, 31)


def myAtoi(src_str: str) -> int:
    sign = 1
    result = 0
    idx = 0
    n = len(src_str)

    # Discard all spaces from the beginning of the input string.
    while idx < n and src_str[idx] == ' ':
        idx += 1
        # print(idx, src_str[idx])

    # sign = +1, if it's positive number, otherwise sign = -1.
    if idx < n and src_str[idx] == '+':
        sign = 1
        idx += 1
    elif idx < n and src_str[idx] == '-':
        sign = -1
        idx += 1

    # Traverse next digits of input and stop if it is not a digit.
    # End of string is also non-digit character.
    while idx < n and src_str[idx].isdigit():
        digit = int(src_str[idx])

        # Check overflow and underflow conditions.
        if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
            # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.
            return INT_MAX if sign == 1 else INT_MIN

        # Append current digit to the result.
        result = 10 * result + digit
        idx += 1

    # We have formed a valid number without any overflow/underflow.
    # Return it after multiplying it with its sign.
    return sign * result


if __name__ == "__main__":
    src_str = " KKK  457 -world -14"
    print(myAtoi(src_str))