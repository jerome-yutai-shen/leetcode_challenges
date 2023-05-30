# -*- coding: utf-8 -*-
"""
Created on Jun 08 12:01:52 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode
from typing import List, Optional


def generate_trees(start, end):
    if start > end:
        return [None, ]

    all_trees = []
    for i in range(start, end + 1):  # pick up a root
        # all possible left subtrees if i is choosen to be a root
        left_trees = generate_trees(start, i - 1)

        # all possible right subtrees if i is choosen to be a root
        right_trees = generate_trees(i + 1, end)

        # connect left and right subtrees to the root i
        for l in left_trees:
            for r in right_trees:
                current_tree = BinaryTreeNode(i)
                current_tree.left = l
                current_tree.right = r
                all_trees.append(current_tree)

    return all_trees


class Solution:
    def generateTrees(self, n: int) -> List[Optional[BinaryTreeNode]]:
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        return generate_trees(1, n) if n else []