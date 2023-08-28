# -*- coding: utf-8 -*-
"""
Created on May 29 21:48:13 2022

@author: Jerome Yutai Shen

"""
from typing import Optional, Union, List


class ListNode:
    def __init__(self, val: Union[int, None], next: Optional[None] = None):
        self.val = val
        self.next = next


class BinaryTreeNode:
    def __init__(self, val: int = 0, left: Optional[None] = None, right: Optional[None] = None, next: Optional[None] = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class GraphNode:
    def __init__(self, val = 0, neighbors = Optional[List]):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def print_bitwise_shift(x: int):
    x_right, x_left = x, x
    while x_right > 0:
        x_right >>= 1
        x_left <<= 1
        print(f"right: {x_right}, left: {x_left}")