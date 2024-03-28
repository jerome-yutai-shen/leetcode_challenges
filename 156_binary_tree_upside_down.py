# -*- coding: utf-8 -*-
"""
Created on Oct 11 23:37:30 2023

@author: Jerome Yutai Shen

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # write your code here

        # this idea is similar to flip linked list
        if not root:
            return None

        prev = None
        prev_right = None
        head = root
        while head:
            # store temp
            temp_left = head.left
            temp_right = head.right
            # flip
            head.left = prev_right
            head.right = prev
            # move next
            prev = head
            prev_right = temp_right
            head = temp_left

        return prev
