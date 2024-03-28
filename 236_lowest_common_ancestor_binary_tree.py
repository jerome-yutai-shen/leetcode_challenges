# -*- coding: utf-8 -*-
"""
Created on Sep 26 18:02:54 2023

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode as TreeNode
from typing import Optional

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = { root: None }

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q



def find236(root: 'TreeNode', p_val: int, q_val: int) -> Optional[TreeNode]:
    """O(n) O(n)"""
    if not root:
        return None

    if root.val == p_val or root.val == q_val:
        return root

    left_node = find236(root.left, p_val, q_val)
    right_node = find236(root.right, p_val, q_val) # 后序位置，已经知道左右子树是否存在目标值
    if left_node and right_node:
        return root
    return left_node if left_node else right_node


def find2360x3f(root: 'TreeNode', p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """O(n) O(n)"""
    if root is None or root is p or root is q:
        return root

    left = find2360x3f(root.left, p, q)
    right = find2360x3f(root.right, p, q)
    if left and right:
        return root
    if left:
        return left
    return right


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return find236(root, p.val, q.val)