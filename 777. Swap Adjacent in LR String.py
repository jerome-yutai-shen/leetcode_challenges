# -*- coding: utf-8 -*-
"""
Created on Jan 28 02:21:22 2024

@author: Jerome Yutai Shen

"""

"""
Explanation
Key observations:

There are three kinds of characters, ‘L’, ‘R’, ‘X’.

Replacing XL with LX = move L to the left by one

Replacing RX with XR = move R to the right by one

If we remove all the X in both strings, the resulting strings should be the same.

Additional observations:

Since a move always involves X, an L or R cannot move through another L or R.

Since anL can only move to the right, for each occurrence of L in the start string, 
its position should be to the same or to the left of its corresponding L in the end string.
# 97. Interleaving String
"""

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end): return False

        # check L R orders are the same
        # 题目说了：当且仅当存在一系列移动操作使得start可以转换成end时， 返回True
        if start.replace('X', '') != end.replace('X', ''): return False
        """
        如果替换为
        if Counter(start).get("L") != Counter(end).get("L") or Counter(start).get("R") != Counter(end).get("R"):
            return False
        就错
        因为无法正确处理start = "LR"; end = "RL"
        LR频数相等是字符串相等的必要条件
        """
        n = len(start)
        Lstart = [i for i in range(n) if start[i] == 'L']
        Lend = [i for i in range(n) if end[i] == 'L']

        Rstart = [i for i in range(n) if start[i] == 'R']
        Rend = [i for i in range(n) if end[i] == 'R']
        # check L positions are correct
        for i, j in zip(Lstart, Lend):
            if j > i: # L只能左移, 移动后index变小
                return False

        # check R positions are correct
        for i, j in zip(Rstart, Rend):
            if j < i:
                return False

        return True

    def canTransform2(self, start: str, end: str) -> bool:
        if len(start) != len(end): return False

        # check L R orders are the same
        # 题目说了：当且仅当存在一系列移动操作使得start可以转换成end时， 返回True
        if start.replace('X', '') != end.replace('X', ''): return False
        """
        如果替换为
        if Counter(start).get("L") != Counter(end).get("L") or Counter(start).get("R") != Counter(end).get("R"):
            return False
        就错
        因为无法正确处理start = "LR"; end = "RL"
        LR频数相等是字符串相等的必要条件
        """
        n = len(start)
        Lstart = [i for i in range(n) if start[i] == 'L']
        Lend = [i for i in range(n) if end[i] == 'L']

        Rstart = [i for i in range(n) if start[i] == 'R']
        Rend = [i for i in range(n) if end[i] == 'R']
        # check L positions are correct
        for i, j in zip(Lstart, Lend):
            if j > i: # L只能左移, 移动后index变小
                return False

        # check R positions are correct
        for i, j in zip(Rstart, Rend):
            if j < i:
                return False

        return True