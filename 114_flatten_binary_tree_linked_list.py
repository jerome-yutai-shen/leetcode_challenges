# -*- coding: utf-8 -*-
"""
Created on Jul 11 11:32:04 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode
from typing import List, Optional


def flatten(root: Optional[BinaryTreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if not root:
        return

    stack = [root]

    while stack:
        node = stack.pop()

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        node.left = None

        if stack:
            node.right = stack[-1]
        else:
            node.right = None


if __name__ == "__main__":
    pass
