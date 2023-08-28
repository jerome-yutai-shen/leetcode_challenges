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


if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(4)
    root.left.left.right = BinaryTreeNode(5)

    root.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.right.right.left = BinaryTreeNode(8)

    xx = Solution()
    x1 = xx.inorderTraversal(root)