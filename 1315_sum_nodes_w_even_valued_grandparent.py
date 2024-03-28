# -*- coding: utf-8 -*-
"""
Created on Oct 12 16:54:15 2023

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


def dfs_sum2(node: TreeNode, parent_value: int, gparent_value: int):
    if node is None:
        return 0

    increment = node.value if gparent_value % 2 == 0 else 0
    return dfs_sum2(node.left, node.value, parent_value) + dfs_sum2(node.right, node.value, parent_value) + increment


def dfs_sum(node: TreeNode, parent_value: int, gp_even: bool):
    if node is None:
        return 0

    increment = node.value if gp_even else 0
    print(gp_even, increment, node.value)
    gp_even = parent_value % 2 == 0  # update the parent_value

    return dfs_sum(node.left, node.value, gp_even) + dfs_sum(node.right, node.value, gp_even) + increment


#  面试考过简化版本
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs_sum_w_subfunc面试考过(root: TreeNode):

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


def dfs_sum面试考过(node: TreeNode):
    results = 0
    if node is None:
        return 0

    if node.value % 2 == 0:
        if node.left:
            results += node.left.value
        if node.right:
            results += node.right.value

    results += dfs_sum面试考过(node.left)
    results += dfs_sum面试考过(node.right)
    return results




class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # print(dfs_sum(root, -1, False))
        assert (dfs_sum(root, -1, False) == dfs_sum2(root, -1, -1))
        assert (dfs_sum2(root, -1, True) == bfs_sum(root))
        return dfs_sum2(root, -1, True)


def get_value(node: TreeNode) -> int:
    return node.value if node else 0


def get_children_value(node: TreeNode) -> int:
    left_value =  node.left.value if node.left else 0
    right_value = node.right.value if node.right else 0
    return left_value + right_value

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
                    results += get_children_value(node.left)

            if node.right:
                q.append(node.right)
                if node.value % 2 == 0:
                    results += get_children_value(node.right)

    return results


def sum_children_w_even_parent(root: TreeNode):
    results = dfs_sum(root, -1, False)
    results2 = dfs_sum2(root, -1, -1)
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