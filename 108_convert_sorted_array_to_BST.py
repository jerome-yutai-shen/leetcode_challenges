# -*- coding: utf-8 -*-
"""
Created on Jun 14 04:37:19 2022

@author: Jerome Yutai Shen

"""
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> refs/remotes/origin/main
from typing import Optional, List
from common_classes import BinaryTreeNode


def sortedArrayToBST(nums: List[int]) -> BinaryTreeNode:
    return helper(nums, 0, len(nums) - 1)


def helper(nums: List[int], p_left: int, p_right: int) -> Optional[BinaryTreeNode]:
    if p_left > p_right:
        return None

    # always choose left middle node as a root
    p = (p_left + p_right) // 2

    # preorder traversal: node -> left -> right
    root = BinaryTreeNode(nums[p])
    root.left = helper(nums, p_left, p - 1)
    root.right = helper(nums, p + 1, p_right)
    return root


if __name__ == "__main__":
<<<<<<< HEAD
    pass
=======
    pass
=======





if __name__ == "__main__":
>>>>>>> 9b01741 (linux)
>>>>>>> refs/remotes/origin/main
