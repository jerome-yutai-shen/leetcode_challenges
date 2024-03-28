# -*- coding: utf-8 -*-
"""
Created on Feb 13 03:23:06 2024

@author: Jerome Yutai Shen

"""
from typing import List


def addSpaces(s: str, spaces: List[int]) -> str:
    p1 = p2 = 0
    res = ""
    while p1 < len(s) or p2 < len(spaces):
        if p2 < len(spaces):
            idx = spaces[p2]
            while p1 < idx:
                res += s[p1]
                p1 += 1
            p2 += 1
            res += " "
        res += s[p1]
        p1 += 1
    return res


def addSpaces2(s: str, spaces: List[int]) -> str:
    spaces = [0] + spaces + [len(s)]
    res = []
    for idx in range(1, len(spaces)):
        res.append(s[spaces[idx-1]:spaces[idx]])
    print(res)
    return " ".join(res)


if __name__ == "__main__":
    s = "LeetcodeHelpsMeLearn"; spaces = [8, 13, 15]
    addSpaces2(s, spaces)

    s = "icodeinpython"; spaces = [1, 5, 7, 9]
    addSpaces2(s, spaces)

    s = "spacing"; spaces = [0, 1, 2, 3, 4, 5, 6]
    addSpaces2(s, spaces)