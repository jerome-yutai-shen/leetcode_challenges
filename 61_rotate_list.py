# -*- coding: utf-8 -*-
"""
Created on Jun 08 02:50:49 2022

@author: Jerome Yutai Shen

"""
from common_classes import ListNode
from typing import Optional


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> Optional[ListNode]:
        # base cases
        if not head:
            return None
        if not head.next:
            return head

        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # break the ring
        new_tail.next = None

        return new_head