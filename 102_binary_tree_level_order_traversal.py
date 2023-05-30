# -*- coding: utf-8 -*-
"""
Created on Jun 13 06:03:36 2022

@author: Jerome Yutai Shen

"""
from typing import Optional, List
from common_classes import BinaryTreeNode
from collections import deque


class Solution:

    def levelOrder(self, root: Optional[BinaryTreeNode]) -> List[List[int]]:
        nodes_bfs = [] # leetcode 107, nodes_bfs = deque([]), deque
        if not root:
            return nodes_bfs
        nodes_q = deque([root])
        while nodes_q:
            len_q = len(nodes_q)
            nodes_current_level = []
            for _ in range(len_q):
                node = nodes_q.popleft()
                if node.left:
                    nodes_q.append(node.left)
                if node.right:
                    nodes_q.append(node.right)
                nodes_current_level.append(node.val) # node.val, instead of node
            nodes_bfs.append(nodes_current_level) # leetcode 107, use appendleft
        return nodes_bfs
