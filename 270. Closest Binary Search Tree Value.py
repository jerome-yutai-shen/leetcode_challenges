# -*- coding: utf-8 -*-
"""
Created on Nov 26 23:00:24 2023

@author: Jerome Yutai Shen

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        """
        O(H), O(1)
        """
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: (abs(target - x), x))
            root = root.left if target < root.val else root.right
        return closest