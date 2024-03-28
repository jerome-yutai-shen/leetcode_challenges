# -*- coding: utf-8 -*-
"""
Created on Sep 26 23:57:15 2023

@author: Jerome Yutai Shen

"""
# 此题不同于236之处在于 node p and node q are not always in the binary tree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def LCA(node, p, q):
    """
    错！光这个不够
    还得处理p或者q有一个不在树里的情况
    """
    if node is None or node == p or node == q:
        return node
    left = LCA(node.left, p, q)
    right = LCA(node.right, p, q)
    if left and right:
        return node
    elif left:
        return left
    else:
        return right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, target):
            if node == target:
                return True
            if node is None:
                return False
            return dfs(node.left, target) or dfs(node.right, target)

        def LCA(node, p, q):
            if node is None or node == p or node == q:
                return node
            left = LCA(node.left, p, q)
            right = LCA(node.right, p, q)
            if left and right:
              return node
            elif left:
              return left
            else:
              return right

        ans = LCA(root, p, q)
        if ans == p:  # check if q is in the subtree of p
            return p if dfs(p, q) else None
        elif ans == q:  # check if p is in the subtree of q
            return q if dfs(q, p) else None
        return ans