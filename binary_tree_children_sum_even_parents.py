# -*- coding: utf-8 -*-
"""
Created on Oct 12 15:31:23 2023

@author: Jerome Yutai Shen

"""
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs_sum_w_subfunc(root: TreeNode):

    results = 0
    def helper(node: TreeNode):
        nonlocal results

        if node is None:
            return 0

        if node.value % 2 == 0:
            if node.left:
                results += node.left.value
            if node.right:
                results += node.right.value

        helper(node.left)
        helper(node.right)

    helper(root)
    return results


def dfs_sum(node: TreeNode):
    results = 0
    if node is None:
        return 0

    if node.value % 2 == 0:
        if node.left:
            results += node.left.value
        if node.right:
            results += node.right.value

    results += dfs_sum(node.left)
    results += dfs_sum(node.right)
    return results


def dfs_sum2(node: TreeNode, parent_even: bool):
    if node is None:
        return 0

    increment = node.value if parent_even else 0
    parent_even = node.value % 2 == 0 # update the parent
    return dfs_sum2(node.left, parent_even) + dfs_sum2(node.right, parent_even) + increment


def bfs_sum(root: TreeNode):
    if not root:
        return 0

    results = 0
    q = deque([root])

    while q:
        num_element = len(q)

        for idx in range(num_element):
            node = q.popleft()

            if node.left:
                q.append(node.left)
                if node.value % 2 == 0:
                    results += node.left.value

            if node.right:
                q.append(node.right)
                if node.value % 2 == 0:
                    results += node.right.value

    return results


def sum_children_w_even_parent(root: TreeNode):
    results = dfs_sum(root)
    results2 = dfs_sum_w_subfunc(root)
    results3 = bfs_sum(root)
    assert results == results2 == results3
    return results


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left.left = TreeNode(8)
    root.right.right.left = TreeNode(9)
    """
                      1
                  /       \
                2          3
              /   \      /   \
             4     5    6     7
                       /     /
                      8     9

    """

    sum_children_w_even_parent(root)

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    """
                      1
                  /       \
                3          4
              /           /   \
             5          6      7
  

    """
    sum_children_w_even_parent(root)
