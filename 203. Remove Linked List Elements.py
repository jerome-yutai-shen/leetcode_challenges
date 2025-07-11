# -*- coding: utf-8 -*-
"""
Created on Jul 03 23:40:27 2025

@author: Jerome Yutai Shen

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while cur:
            if cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next

        return dummy.next

    def removeElements2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while cur and cur.next: # 写 cur也没错
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next

        return dummy.next
