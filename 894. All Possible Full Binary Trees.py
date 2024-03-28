# -*- coding: utf-8 -*-
"""
Created on Nov 25 01:24:36 2023

@author: Jerome Yutai Shen

"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        """
        o(2 ** (n/2)), O(n * 2** (n/2))
        """
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode()]

        res = []
        for i in range(1, n, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - i - 1)

            for l in left:
                for r in right:
                    root = TreeNode(0, l, r)
                    res.append(root)

        return res


class Solution2:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        """
        o(2 ** (n/2)), O(n * 2** (n/2))
        """
        if n % 2 == 0:
            return []

        dp = [[] for _ in range(n + 1)]
        dp[1].append(TreeNode(0))

        for count in range(3, n + 1, 2):
            for i in range(1, count - 1, 2):
                j = count - 1 - i
                for left in dp[i]:
                    for right in dp[j]:
                        root = TreeNode(0, left, right)
                        dp[count].append(root)

        return dp[n]