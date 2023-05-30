# -*- coding: utf-8 -*-
"""
Created on May 26 20:26:10 2022

@author: Jerome Yutai Shen

"""
PARENTHESES = {")": "(",
               "}": "{",
               "]": "["}


def is_valid(s: str) -> bool:
    if len(s) % 2: # length of s is 2*n + 1, odd
        return False
    stack = []
    for char in s:
        if char in PARENTHESES:
            if not stack:
                return False
            top_element = stack.pop()
            if PARENTHESES[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack


if __name__ == "__main__":
    print(is_valid("[[[{}]]]"))
    print(is_valid(""))
    print(is_valid("){"))