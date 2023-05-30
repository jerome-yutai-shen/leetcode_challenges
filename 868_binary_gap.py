# -*- coding: utf-8 -*-
"""
Created on Apr 11 23:02:54 2023

@author: Jerome Yutai Shen

"""
from collections import deque


def binary_gap(num: int) -> int:
    max_distance = 0
    splitted_digits = bin(num)[2:].split("1")
    # print(splitted_digits)
    if splitted_digits[-1]:
        splitted_digits.pop()

    tmp_deque = deque([splitted_digits[0]])
    for _ in splitted_digits[1:]:
        tmp_deque.append(_)
        distance = len(_)
        print(_, tmp_deque, distance)
        if _ == tmp_deque[0]:
            while len(tmp_deque) > 1:
                str1 = tmp_deque.popleft()
                distance += max(1, len(str1))
        max_distance = max(max_distance, distance)

    return max_distance


if __name__ == "__main__":

    for num in [1, 6, 7, 8, 22]:
        print(num, bin(num), binary_gap(num))

