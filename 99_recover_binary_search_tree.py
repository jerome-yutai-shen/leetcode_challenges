# -*- coding: utf-8 -*-
"""
Created on Jun 08 11:31:37 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode


class Solution:
    def recoverTree(self, root: BinaryTreeNode):
        """
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = pred = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
                else:
                    break
            pred = root
            root = root.right

        x.val, y.val = y.val, x.val