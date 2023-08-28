# -*- coding: utf-8 -*-
"""
Created on Jun 08 05:51:01 2022

@author: Jerome Yutai Shen

"""
from common_classes import ListNode
from typing import Optional


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def delete_duplicates(head: ListNode) -> ListNode:
        # write your code here
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head
