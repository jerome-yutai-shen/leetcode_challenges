# -*- coding: utf-8 -*-
"""
Created on Jun 08 12:06:50 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode
from typing import List, Optional
import math

class Solution:

    def isValidBST(self, root: Optional[BinaryTreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

    def isValidBST_inorder(self, root: BinaryTreeNode) -> bool:
        stack, prev = [], -math.inf
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True