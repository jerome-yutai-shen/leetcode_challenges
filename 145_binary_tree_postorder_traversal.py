# -*- coding: utf-8 -*-
"""
Created on Jul 06 16:47:46 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode
from typing import List, Optional


RIGHT_CODE = 3
LEFT_CODE = 2
ROOT_CODE = 1
CHILD_CODE = 0


def postorder_traversal(root: Optional[BinaryTreeNode]) -> List[int]:
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    print(result)
    return result[::-1]


def dfs_traversal(root: Optional[BinaryTreeNode], node_print_code: int, if_debug: bool = False) -> List[int]:
    stack = [(root, CHILD_CODE)]
    values = []

    while stack:
        node, code = stack.pop()
        if node is None:
            continue
        if if_debug:
            print(node.val, code)

        if code == CHILD_CODE:
            stack.append((node, RIGHT_CODE))
            stack.append((node.right, CHILD_CODE))
            stack.append((node, LEFT_CODE))
            stack.append((node.left, CHILD_CODE))
            stack.append((node, ROOT_CODE))

        if code == node_print_code:
            values.append(node.val)

    return values


if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(4)
    root.left.left.right = BinaryTreeNode(5)

    root.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.right.right.left = BinaryTreeNode(8)

    nodes_values_list = postorder_traversal(root)
    print(nodes_values_list)
    print(dfs_traversal(root, 2))