# -*- coding: utf-8 -*-
"""
Created on Sep 26 23:41:24 2023

@author: Jerome Yutai Shen

"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        boundary = [root.val]

        def dfs_leftmost(node):
            if not node or (not node.left and not node.right):
                return
            boundary.append(node.val)

            if node.left is not None:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)

        def dfs_leaves(node):

            if not node:
                return
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.right)

        def dfs_rightmost(node):
            if not node or (not node.left and not node.right):
                return

            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            boundary.append(node.val)

        dfs_leftmost(root.left)
        dfs_leaves(root)
        dfs_rightmost(root.right)

        return boundary