# -*- coding: utf-8 -*-
"""
Created on Jun 13 06:24:56 2022

@author: Jerome Yutai Shen

"""
from typing import Optional, List, Deque
from common_classes import BinaryTreeNode
from collections import deque


class Solution:

    def levelOrderBottom(self, root: Optional[BinaryTreeNode]) -> Deque[List[int]]:
        nodes_bfs = deque([]) # leetcode 102, nodes_bfs = [], list
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
            nodes_bfs.appendleft(nodes_current_level) # leetcode 102, use append
        return nodes_bfs