# -*- coding: utf-8 -*-
"""
Created on Jul 10 20:54:28 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode
from typing import List, Optional


def recurseTree(node: BinaryTreeNode, remainingSum: int, pathNodes: List, pathsList: List):
    if not node:
        return

    # Add the current node to the path's list
    pathNodes.append(node.val)

    # Check if the current node is a leaf and also, if it
    # equals our remaining sum. If it does, we add the path to
    # our list of paths
    if remainingSum == node.val and not node.left and not node.right:
        pathsList.append(list(pathNodes))
    else:
        # Else, we will recurse on the left and the right children
        recurseTree(node.left, remainingSum - node.val, pathNodes, pathsList)
        recurseTree(node.right, remainingSum - node.val, pathNodes, pathsList)

    # We need to pop the node once we are done processing ALL of it's
    # subtrees.
    pathNodes.pop()


def pathSum2(root: Optional[BinaryTreeNode], target_sum: int) -> List[List[int]]:
    pathsList = []
    recurseTree(root, target_sum, [], pathsList)
    return pathsList


def pathSum(self, root: Optional[BinaryTreeNode], target_sum: int) -> List[List[int]]:
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
        if not node.left and not node.right and sum(path) == target_sum:
            paths.append(path)
        if node.left:
            stack.append((node.left, tuple(path) + (node.left.val, )))
        if node.right:
            stack.append((node.right, tuple(path) + (node.right.val, )))

    return paths


if __name__ == "__main__":
    pass
