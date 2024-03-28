# -*- coding: utf-8 -*-
"""
Created on Nov 26 12:12:10 2023

@author: Jerome Yutai Shen

题目没说不能覆盖原先的树

"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """新树，但这个办法不如直接覆盖"""
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root


def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1:
        return t2
    if not t2:
        return t1

    t1.val += t2.val
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    return t1


class Solution递归:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


def mergeTrees2(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1:
        return t2
    if not t2:
        return t1

    new_stack = []
    new_stack.append((t1, t2,))
    while new_stack:
        node = new_stack.pop()
        if not node[0] or not node[1]:
            continue
        node[0].val += node[1].val

        if not node[0].left:
            node[0].left = node[1].left
        else:
            new_stack.append([node[0].left, node[1].left])

        if not node[0].right:
            node[0].right = node[1].right
        else:
            new_stack.append([node[0].right, node[1].right])

    return t1


    t1.val += t2.val
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    return t1