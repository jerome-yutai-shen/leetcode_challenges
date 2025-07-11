# -*- coding: utf-8 -*-
"""
Created on Jul 04 19:03:29 2025

@author: Jerome Yutai Shen

你不能直接删自己 —— 但你可以“伪装”成下一个节点，然后删掉下一个节点

✅ 操作过程是：
	1.	把 node.next.val 赋给 node.val（即“变身”成后一个节点）
	2.	让 node.next = node.next.next（跳过原来的下一个节点）

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next