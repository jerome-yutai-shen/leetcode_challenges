# -*- coding: utf-8 -*-
"""
Created on Jun 13 19:21:51 2022

@author: Jerome Yutai Shen

"""
from typing import Optional, List, Deque
from common_classes import BinaryTreeNode
from collections import deque


def maxDepth(root: Optional[BinaryTreeNode]) -> int:
    """
    :type root: TreeNode
    :rtype: int
    """
    stack = []
    depth = 0

    if root is not None:
        current_depth = 1
        stack.append((current_depth, root))

    while stack:
        current_depth, node = stack.pop()
        if node is not None:
            depth = max(depth, current_depth)
            stack.append((current_depth + 1, node.left))
            stack.append((current_depth + 1, node.right))

    return depth


def maxDepth_bfs(self, root: Optional[BinaryTreeNode]) -> int:
    #nodes_bfs = [] # leetcode 107, nodes_bfs = deque([]), deque
    idx_level = 0
    if not root:
        return idx_level

    nodes_q = deque([root])
    while nodes_q:
        len_q = len(nodes_q)
        for _ in range(len_q):
            node = nodes_q.popleft()
            if node.left:
                nodes_q.append(node.left)
            if node.right:
                nodes_q.append(node.right)
        idx_level += 1

    return idx_level


def max_depth_bfs2(self, root: Optional[BinaryTreeNode]) -> int:
    nodes_bfs = []  # leetcode 107, nodes_bfs = deque([]), deque
    if not root:
        return len(nodes_bfs)
    nodes_q = deque([root])
    while nodes_q:
        len_q = len(nodes_q)
        nodes_current_level = []
        for _ in range(len_q):
            node = nodes_q.popleft()
            if node.left:
                nodes_q.append(node.left)
            if node.right:
                nodes_q.append(node.right)
            nodes_current_level.append(node.val)  # node.val, instead of node
        nodes_bfs.append(nodes_current_level)  # leetcode 107, use appendleft
    return len(nodes_bfs)


if __name__ == "__main__":
    root = BinaryTreeNode(1)
    maxDepth(root)

    root = BinaryTreeNode(3)
    root.left = BinaryTreeNode(9)
    root.right = BinaryTreeNode(20)
    root.right.left = BinaryTreeNode(15)
    root.right.right = BinaryTreeNode(7)
    maxDepth(root)

