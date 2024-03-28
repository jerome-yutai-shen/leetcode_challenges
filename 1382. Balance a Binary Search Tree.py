# -*- coding: utf-8 -*-
"""
Created on Nov 27 09:12:00 2023

@author: Jerome Yutai Shen

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionHuaHua:
    """花花代码移植出错了"""
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []
        def inorder(root: TreeNode):
            if not root:
                return
            nonlocal values
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)

        def build(l: int, r: int):
            if l > r:
                return
            m = (r - l) // 2
            root = TreeNode(m)
            root.left = build(l, m - 1)
            root.right = build(m + 1, r)

            return root

        inorder(root)

        return build(0, len(values) - 1)


def InOrderTrav(node):
    vals = []
    if node.left:
        vals.extend(InOrderTrav(node.left))

    vals.append(node.val)

    if node.right:
        vals.extend(InOrderTrav(node.right))

    return vals


def CreateBalTree(vals):
    mid = len(vals) // 2
    head = TreeNode(vals[mid])
    if mid > 0:
        head.left = CreateBalTree(vals[0:mid])

    if mid < len(vals) - 1:
        head.right = CreateBalTree(vals[mid + 1: len(vals)])

    return head


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        return CreateBalTree(InOrderTrav(root))
