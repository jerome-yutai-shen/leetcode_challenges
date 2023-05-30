# -*- coding: utf-8 -*-
"""
Created on Jul 06 22:41:08 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode
from typing import List, Optional


RIGHT_CODE = 3
LEFT_CODE = 2
ROOT_CODE = 1
CHILD_CODE = 0


def dfs_traversal(root: Optional[BinaryTreeNode], node_print_code: int, if_debug:bool = False) -> List[int]:
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


def dfs_traversal2(root: Optional[BinaryTreeNode], node_print_code: int) -> List[int]:
    stack = [(root, CHILD_CODE)]
    values = []

    while stack:
        node, code = stack.pop()
        if node is None:
            continue
        print(node.val, code)

        if code == CHILD_CODE:
            stack.append((node, ROOT_CODE))

            stack.append((node, LEFT_CODE))
            stack.append((node.left, CHILD_CODE))

            stack.append((node, RIGHT_CODE))
            stack.append((node.right, CHILD_CODE))

        if code == node_print_code:
            values.append(node.val)

    return values


def inorder_traversal(root: Optional[BinaryTreeNode]) -> List[int]:
    stack = [(root, 0)]
    values = []
    node_print_code = LEFT_CODE

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


def postorder_traversal(root: Optional[BinaryTreeNode]) -> List[int]:
    stack = [(root, 0)]
    stack2 = [(root.val, 0)]
    values = []
    node_print_code = RIGHT_CODE

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


def preorder_traversal(root: Optional[BinaryTreeNode]) -> List[int]:
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


def preorder_traversal1(root: Optional[BinaryTreeNode]) -> List[int]:
    if not root:
        return []

    output, stack = [], [root]

    while stack:
        node = stack.pop()
        output.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return output


def inorder_traversal1(root: Optional[BinaryTreeNode]) -> List[int]:
    if not root:
        return []

    output, stack = [], []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            output.append(node.val)
            node = node.right
    return output


def inorder_traversal2(root: Optional[BinaryTreeNode]) -> List[int]:
    if not root:
        return []

    stack = []
    curr_node = root
    nodes_values_list = []
    while stack or curr_node:
        print(f"stack: {stack}, curr_node: {curr_node}\n")
        if curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        else:
            node = stack.pop()
            nodes_values_list.append(node.val)
            curr_node = node.right
    return nodes_values_list


def preorder_traversal_jiuzhang(root: Optional[BinaryTreeNode]) -> List[int]:
    if not root:
        return []

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
    if not root:
        return []

    output, stack = [], [root]

    node = stack.pop()
    while stack or node:
        if node:
            output.append(node.val)
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            node = node.right

    return output


def postorder_traversal1(root: Optional[BinaryTreeNode]) -> List[int]:
    if root is None:
        return []

    output, stack = [], [root]

    while stack:
        node = stack.pop()
        output.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    print(f"output: {output}")
    return output[::-1]


if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)

    root.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.right.right.left = BinaryTreeNode(8)

    # print(inorder_traversal1(root) == inorder_traversal2(root))
    print(inorder_traversal1(root))
    print(preorder_traversal1(root))
    print(postorder_traversal1(root))

    print(dfs_traversal(root, RIGHT_CODE))
    print(dfs_traversal(root, LEFT_CODE))
    print(dfs_traversal(root, ROOT_CODE))
    print(dfs_traversal(root, CHILD_CODE))


    """
    for _ in [RIGHT_CODE, LEFT_CODE, ROOT_CODE]:
        print(dfs_traversal(root, _))


    """