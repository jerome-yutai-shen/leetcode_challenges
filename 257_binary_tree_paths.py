# -*- coding: utf-8 -*-
"""
Created on Jul 11 10:06:51 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode
from typing import List, Optional


def binary_tree_paths(root: BinaryTreeNode):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if not root:
        return []

    paths = []
    stack = [(root, str(root.val))]
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            paths.append(path)

        if node.right:
            stack.append((node.right, path + '->' + str(node.right.val)))

        if node.left:
            stack.append((node.left, path + '->' + str(node.left.val)))


    return paths


def binary_tree_paths2(root: BinaryTreeNode):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if not root:
        return []

    paths = []
    stack = [(root, [root.val])]
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            paths.append(path)
        if node.left:
            stack.append((node.left, tuple(path) + (node.left.val, )))
        if node.right:
            stack.append((node.right, tuple(path) + (node.right.val, )))

    return paths




if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(4)
    root.left.left.right = BinaryTreeNode(5)

    root.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.right.right.left = BinaryTreeNode(8)

    print(binary_tree_paths(root))
    print(binary_tree_paths2(root))
