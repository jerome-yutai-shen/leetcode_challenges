# -*- coding: utf-8 -*-
"""
Created on Nov 22 12:56:53 2023

@author: Jerome Yutai Shen

leetcode 987

"""
from typing import Optional, List
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        如果不用min_column、max_column，
        那么最后返回的时候就得[columnTable[x] for x in sorted(columnTable.keys())]
        时间复杂度就成了O(NlogN)
        用了min_column、max_column
        时间复杂度就成了O(N)
        空间复杂度是O(N)
        """
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(min_column, max_column + 1)]


if __name__ == "__main__":
    _ = Solution()

    xx = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(xx[0])
    root.left = TreeNode(xx[1])
    root.right = TreeNode(xx[2])
    root.right.left = TreeNode(xx[-2])
    root.right.right = TreeNode(xx[-1])
    q, ct = _.verticalOrder(root)

    xx = [3,9,8,4,0,1,7]
    root = TreeNode(xx[0])
    root.left = TreeNode(xx[1])
    root.right = TreeNode(xx[2])
    root.left.left = TreeNode(xx[3])
    root.left.right = TreeNode(xx[4])
    root.right.left = TreeNode(xx[-2])
    root.right.right = TreeNode(xx[-1])
    q1, ct1 = _.verticalOrder(root)

    xx = [3,9,8,4,0,1,7,None,None,None,2,5]
    root = TreeNode(xx[0])
    root.left = TreeNode(xx[1])
    root.right = TreeNode(xx[2])
    root.left.left = TreeNode(xx[3])
    root.left.right = TreeNode(xx[4])
    root.right.left = TreeNode(xx[5])
    root.right.right = TreeNode(xx[6])
    root.left.right.right = TreeNode(xx[-2])
    root.right.left.left = TreeNode(xx[-1])
    q2, ct2 = _.verticalOrder(root)
