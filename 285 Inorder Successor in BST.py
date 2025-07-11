# -*- coding: utf-8 -*-
"""
Created on Jul 09 15:09:48 2025

@author: Jerome Yutai Shen

"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        """其实还是二分查找的变体
        时间复杂度在平衡的情况下才是O(logN)即O(h)，其中 h 是树的高度。
        在最坏的情况下退化成ON
        空间复杂度O1
        """
        successor = None
        while root:
            # 只关心：
            # 当前节点是否 有可能成为比 p 大的后继节点？
            # 	•	如果 root.val > p.val：
            # 	•	当前节点可能是答案，记下它（successor = root），然后往左子树找更小的合适值。
            # 	•	如果 root.val ≤ p.val：
            # 	•	当前节点不可能成为后继，直接往右子树找大一点的。

            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor