# -*- coding: utf-8 -*-
"""
Created on Feb 21 08:58:53 2024

@author: Jerome Yutai Shen

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            total_sum, count = 0, 0
            temp = deque([])

            while queue:
                node = queue.popleft()
                total_sum += node.val
                count += 1

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            queue = temp
            res.append(total_sum / count)

        return res