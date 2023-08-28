# -*- coding: utf-8 -*-
"""
Created on Jun 08 11:41:02 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[BinaryTreeNode]) -> List[int]:
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

    def inorderTraversal_jiuzhang(self, root):
        if root is None:
            return []
        dummy = BinaryTreeNode(0)
        dummy.right = root
        stack = [dummy]

        inorder = []
        # 每次将 iterator 挪到下一个点
        # 也就是调整 stack 使得栈顶到下一个点
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder.append(stack[-1].val)

        return inorder

    def inorderTraversal2(self, root):
        stack = [(root, 0)]
        values = []

        while stack:
            node, count = stack.pop()
            if node is None:
                continue

            if count == 0:
                stack.append((node, 3))
                stack.append((node.right, 0))
                stack.append((node, 2))
                stack.append((node.left, 0))
                stack.append((node, 1))

            if count == 2:
                values.append(node.val)

        return values

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