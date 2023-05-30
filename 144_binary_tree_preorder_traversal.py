# -*- coding: utf-8 -*-
"""
Created on Jul 06 15:46:45 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode
from typing import List, Optional


RIGHT_CODE = 3
LEFT_CODE = 2
ROOT_CODE = 1
CHILD_CODE = 0


def preorder_traversal(root: Optional[BinaryTreeNode]) -> List[int]:
    if not root:
        return []

    stack = [root]
    stack2 = [root.val]
    nodes_values_list = []

    while stack:
        current_node = stack.pop()
        current_node_val = stack2.pop()
        nodes_values_list.append(current_node.val)
        #print(f"stack: {stack2} {current_node_val}\n")
        if current_node.right:
            stack.append(current_node.right)
            stack2.append(current_node.right.val)

        if current_node.left:
            stack.append(current_node.left)
            stack2.append(current_node.left.val)
        #print(f"stack: {stack2}\n")

    return nodes_values_list


def preorder_traversal1(root):
    """
    不一样的非递归，为你拓宽思路
    一路向左，到头回溯，能右转右
    """
    output, stack = [], []

    while root or stack:
        if root:
            output.append(root.val)
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            root = root.right

    return output


def preorder_traversal2(root: Optional[BinaryTreeNode]) -> List[int]:
    stack = [(root, 0)]
    values = []
    node_print_code = ROOT_CODE

    while stack:
        node, count = stack.pop()
        if node is None:
            continue

        if count == CHILD_CODE:
            stack.append((node, RIGHT_CODE))
            stack.append((node.right, CHILD_CODE))
            stack.append((node, LEFT_CODE))
            stack.append((node.left, CHILD_CODE))
            stack.append((node, ROOT_CODE))

        if count == node_print_code:
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

    nodes_values_list = preorder_traversal(root)
    print(nodes_values_list)