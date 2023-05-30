# -*- coding: utf-8 -*-
"""
Created on Nov 30 17:25:34 2022

@author: Jerome Yutai Shen

"""

def chk_palindrome(input_str: str) -> bool:
    if_palindrome = True
    if not input_str:
        return not if_palindrome

    pntr_left, pntr_right = 0, len(input_str) - 1

    while pntr_left <= pntr_right:
        if_palindrome = input_str[pntr_left] == input_str[pntr_right]
        if not if_palindrome:
            return if_palindrome
        pntr_left += 1
        pntr_right -= 1

    return if_palindrome



if __name__ == "__main__":
    input_str = "abcd"
    print(chk_palindrome(input_str))
    input_str = "abc"
    print(chk_palindrome(input_str))

