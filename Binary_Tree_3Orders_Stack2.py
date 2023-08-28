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


from enum import Enum, unique

@unique
class NoteCode(Enum):
    as_child = 0
    as_root = 1
    as_left = 2
    as_right = 3


def dfs_traversal(root: Optional[BinaryTreeNode], node_print_code: int, if_debug:bool = False) -> List[int]:
    stack = [(root, NoteCode(0))]
    if if_debug:
        stack2 = [(root.val, NoteCode(0))]
    values = []

    while stack:
        node, code = stack.pop()
        if if_debug:
            print(f"stack poped {node.val if node else node, code.name}")
            _ = stack2.pop()
            print(f"pop {_}, stack2 remains {stack2}")
        if node is None:
            if if_debug:
                print(f"node is {node}, continue")
            continue

        if code == NoteCode(0):
            stack.append((node, NoteCode(3)))
            stack.append((node.right, NoteCode(0)))
            stack.append((node, NoteCode(2)))
            stack.append((node.left, NoteCode(0)))
            stack.append((node, NoteCode(1)))

        if if_debug and code == NoteCode(0):
            stack2.append((node.val if node else None, NoteCode(RIGHT_CODE).name))
            stack2.append((node.right.val if node.right else None, NoteCode(CHILD_CODE).name))
            stack2.append((node.val if node else None, NoteCode(LEFT_CODE).name))
            stack2.append((node.left.val if node.left else None, NoteCode(CHILD_CODE).name))
            stack2.append((node.val if node else None, NoteCode(ROOT_CODE).name))
            print(f"stack2: {stack2}")
        if code == NoteCode(node_print_code):
            values.append(node.val)
        if if_debug:
            print(f"values: {values}\n-------")
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


def in3(root: Optional[BinaryTreeNode]) -> List[int]:
    if root is None:
        return []

    output, stack = [], [root]
    node = stack.pop()
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        msg = "---\n"
        for _ in stack:
            msg += f"{_.val},"
        msg += "\n___"
        print(msg)
        node = stack.pop()
        output.append(node.val)
        node = node.right
    return output


def post3(root: Optional[BinaryTreeNode]) -> List[int]:
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


def pre3(root: Optional[BinaryTreeNode]) -> List[int]:
    if root is None:
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


def in4(root: Optional[BinaryTreeNode]) -> List[int]:
    if not root:
        return []

    output, stack = [], [root]
    curr_node = stack.pop()

    while stack or curr_node:
        if curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        else:
            curr_node = stack.pop()
            output.append(curr_node.val)
            curr_node = curr_node.right
    return output


def pre4(root: Optional[BinaryTreeNode]) -> List[int]:
    if not root:
        return []

    output, stack = [], [root]
    curr_node = stack.pop()
    
    while stack or curr_node:
        if curr_node:            
            stack.append(curr_node)
            output.append(curr_node.val)
            curr_node = curr_node.left
        else:
            curr_node = stack.pop()
            curr_node = curr_node.right

    return output


def post4(root: Optional[BinaryTreeNode]) -> List[int]:
    if not root:
        return []

    output, stack = [], [root]
    curr_node = stack.pop()
    
    while stack or curr_node:
        if curr_node:
            stack.append(curr_node)
            output.append(curr_node.val)
            curr_node = curr_node.right
        else:
            curr_node = stack.pop()
            curr_node = curr_node.left

    return output[::-1]


from enum import Enum, unique


@unique
class AppendCode(Enum):
    right = 3
    left = 2
    root = 1
    child = 0

def uni_traverse(root: Optional[BinaryTreeNode], append_code: int) -> List[int]:
    stack = [(root, CHILD_CODE)]
    values = []

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

        if count == append_code:
            values.append(node.val)

    return values


if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)

    root.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.right.left.left = BinaryTreeNode(8)
    root.right.right.left = BinaryTreeNode(9)

    # print(inorder_traversal1(root) == inorder_traversal2(root))
<<<<<<< HEAD:Binary_Tree_3Orders_Stack2.py
    assert in3(root) == in4(root)
    assert pre3(root) == pre4(root)
    assert post3(root) == post4(root)
=======
    # print(inorder_traversal1(root))
    # print(preorder_traversal1(root))
    # print(postorder_traversal1(root))
>>>>>>> 3b63afa41887e4b8d6777d50bea244ef0bf69c92:Binary_Tree_3Orders_Stack.py

    print(dfs_traversal(root, RIGHT_CODE))
    print(dfs_traversal(root, LEFT_CODE))
    print(dfs_traversal(root, ROOT_CODE))
    print(dfs_traversal(root, CHILD_CODE))


    """
    for _ in [RIGHT_CODE, LEFT_CODE, ROOT_CODE]:
        print(dfs_traversal(root, _))


    """