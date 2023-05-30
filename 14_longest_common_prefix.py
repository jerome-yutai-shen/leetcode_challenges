# -*- coding: utf-8 -*-
"""
Created on May 23 17:49:28 2022

@author: Jerome Yutai Shen

"""
from typing import List


def horizontal_scanning(strs: List[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for idx in range(1, len(strs)):
        word = strs[idx]
        print(f"prefix {prefix}, word {word}")

        while word.find(prefix): #
            prefix = prefix[0: len(prefix) - 1]
            print(f"not in {prefix}")
            if not prefix:
                return ""

    return prefix


def vertical_scanning(strs: List[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for idx, char in enumerate(prefix):
        for jdx in range(1, len(strs)):
            if idx == len(strs[jdx]) or strs[jdx][idx] != char:
                return prefix[:idx]
    return prefix


if __name__ == "__main__":
    # strs = ["flower", "flow", "flight"]
    # print(horizontal_scanning(strs))
    # strs = [""]
    # print(horizontal_scanning(strs))
    # strs = ["a"]
    # print(horizontal_scanning(strs))
    # strs = ["", ""]
    # print(horizontal_scanning(strs))
    strs = ["c", "acc", "ccc"]
    pr1 = horizontal_scanning(strs)
    strs = ["abca", "aba", "aaab"]
    pr2 = horizontal_scanning(strs)
    strs = ["abc", "abca", "abcad"]
    pr3 = horizontal_scanning(strs)

