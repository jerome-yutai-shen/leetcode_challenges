# -*- coding: utf-8 -*-
"""
Created on Oct 23 14:49:19 2023

@author: Jerome Yutai Shen

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        # reform tree into array-based tree
        tree = []
        graph = { -1: [] }
        index = -1
        q = [(root, -1)]
        while q:
            node, parent_index = q.pop(0)
            if node:
                index += 1
                tree.append(node.val)
                graph[index] = []
                graph[parent_index].append(index)
                q.append((node.left, index))
                q.append((node.right, index))

        # represent the maximum start by node i with robbing i
        dp_rob = [0] * (index + 1)

        # represent the maximum start by node i without robbing i
        dp_not_rob = [0] * (index + 1)

        for i in reversed(range(index + 1)):
            if not graph[i]:  # if is leaf
                dp_rob[i] = tree[i]
                dp_not_rob[i] = 0
            else:
                dp_rob[i] = tree[i] + sum(dp_not_rob[child]
                                          for child in graph[i])
                dp_not_rob[i] = sum(max(dp_rob[child], dp_not_rob[child])
                                    for child in graph[i])

        return max(dp_rob[0], dp_not_rob[0])

    def rob2(self, root: TreeNode) -> int:
        def dp(root):
            if not root:
                return 0, 0

            left = dp(root.left)
            right = dp(root.right)

            # 抢当前，则两个下家不抢
            do = root.val + left[0] + right[0]
            # 不抢当前，则下家随意
            do_not = max(left) + max(right)

            return do_not, do

        return max(dp(root))