# -*- coding: utf-8 -*-
"""
Created on Jul 10 20:55:17 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode


RIGHT_CODE = 3
LEFT_CODE = 2
ROOT_CODE = 1
CHILD_CODE = 0


def hasPathSum(root: BinaryTreeNode, target_sum: int):
    """
    :type root: TreeNode
    :type target_sum: int
    :rtype: bool
    """
    if not root:
        return False

    de = [(root, target_sum - root.val), ]
    while de:
        node, curr_sum = de.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.right:
            de.append((node.right, curr_sum - node.right.val))
        if node.left:
            de.append((node.left, curr_sum - node.left.val))
    return False


if __name__ == "__main__":
    pass
