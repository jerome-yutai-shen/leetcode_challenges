# -*- coding: utf-8 -*-
"""
Created on Jul 05 09:19:40 2025

@author: Jerome Yutai Shen

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxlen = 0

        def dfs(node, parent_val, curr_length):
            if not node:
                return

            # 判断是否连续
            if node.val == parent_val + 1:
                curr_length += 1
            else:
                curr_length = 1

            # 更新最大长度
            self.maxlen = max(self.maxlen, curr_length)

            # 递归左右子树
            dfs(node.left, node.val, curr_length)
            dfs(node.right, node.val, curr_length)

        dfs(root, root.val - 1, 0)
        return self.maxlen