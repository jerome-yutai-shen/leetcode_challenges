# -*- coding: utf-8 -*-
"""
Created on Nov 19 10:53:39 2023

@author: Jerome Yutai Shen

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        """O(n), O(n)"""
        self.red_left = self.red_right  = 0
        def count(root: Optional[TreeNode]):
            if not root:
                return 0
            l = count(root.left)
            r = count(root.right)
            if root.val == x:
                self.red_left =  l
                self.red_right = r
            return 1 + l + r

        count(root)
        p = n - (self.red_left + self.red_right + 1)

        return max(p, self.red_left, self.red_right) > n/2