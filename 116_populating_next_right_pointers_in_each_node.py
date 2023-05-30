# -*- coding: utf-8 -*-
"""
Created on May 30 08:32:42 2022

@author: Jerome Yutai Shen

"""
from typing import Optional
from collections import deque
from common_classes import BinaryTreeNode as Node


class Solution:
    NULL_NODE = "#"

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        nodes_queue = deque([root])
        while nodes_queue:
            len_queue = len(nodes_queue)
            for idx in range(len_queue):
                node = nodes_queue.popleft()

                if idx < len_queue - 1:
                    node.next = nodes_queue[0]

                if node and node.left:
                    nodes_queue.append(node.left)
                if node and node.right:
                    nodes_queue.append(node.right)

        return root