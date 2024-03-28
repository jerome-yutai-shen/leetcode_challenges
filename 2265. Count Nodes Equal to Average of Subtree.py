# -*- coding: utf-8 -*-
"""
Created on Nov 25 14:29:16 2023

@author: Jerome Yutai Shen


Google 6月22日面试题的变种
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0, 0

            leftSum, leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)

            if (leftSum + rightSum + node.val) // (leftCount + rightCount + 1) == node.val:
                self.ans += 1

            return leftSum + rightSum + node.val, leftCount + rightCount + 1

        dfs(root)
        return self.ans

    def averageOfSubtree2(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0, 0

            leftCount, leftSum = dfs(node.left)
            rightCount, rightSum = dfs(node.right)

            if (leftSum + rightSum + node.val) // (leftCount + rightCount + 1) == node.val:
                self.ans += 1

            return leftCount + rightCount + 1, leftSum + rightSum + node.val

        dfs(root)
        return self.ans