# -*- coding: utf-8 -*-
"""
Created on Jan 07 02:29:02 2024

@author: Jerome Yutai Shen

3

"""


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        pass


def findMinLastPos(mm) -> int:
    """贾考博"""
    min_pos = float("inf")
    for key in mm:
        min_pos = min(min_pos, mm[key])

    return min_pos


def smallestSubsequence(s: str) -> str:
    """贾考博"""
    mm = {c: i for i, c in enumerate(s)}

    start = 0
    end = findMinLastPos(mm)

    res = [0] * len(mm)

    for i in range(len(res)):
        min_char = chr(ord('z') + 1)
        for k in range(start, end + 1):
            if ord(s[k]) < ord(min_char) and s[k] in mm:
                min_char = s[k]
                start = k + 1

        res[i] = min_char

        del mm[min_char]

        if s[end] == min_char:
            end = findMinLastPos(mm)

    return "".join(res)


if __name__ == "__main__":
    s = "cbaa"
    ss = smallestSubsequence(s)

    s = "cbacba"
    ss = smallestSubsequence(s)