# -*- coding: utf-8 -*-
"""
Created on Sep 26 23:08:07 2023

@author: Jerome Yutai Shen

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_0x3f(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """

    x = root.val
    if p.val > x and q.val > x:
        return find_0x3f(root.right, p, q)
    elif p.val < x and q.val < x:
        return find_0x3f(root.left, p, q)
    return root


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node.
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node