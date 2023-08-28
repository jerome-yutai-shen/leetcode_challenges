# -*- coding: utf-8 -*-
"""
Created on Jul 10 13:58:10 2023

@author: Jerome Yutai Shen

"""
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes_queue = deque([root])
        most_right_nodes = []

        while nodes_queue:
            tmp = []
            for _ in range(len(nodes_queue)):
                node0 = nodes_queue.popleft()
                if not node0:
                    continue
                tmp.append(node0.val)
                if node0.left:
                    nodes_queue.append(node0.left)
                if node0.right:
                    nodes_queue.append(node0.right)
            if tmp:
                most_right_nodes.append(tmp[-1])
        return most_right_nodes


class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes_queue = deque([root])
        most_right_nodes = []

        while nodes_queue:
            # tmp = []
            for _ in range(len(nodes_queue)):
                node0 = nodes_queue.popleft()
                if not node0:
                    continue
                # tmp.append(node0.val)
                if node0.left:
                    nodes_queue.append(node0.left)
                if node0.right:
                    nodes_queue.append(node0.right)
            if node0:
                most_right_nodes.append(node0.val)
        return most_right_nodes
