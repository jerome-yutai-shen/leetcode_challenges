# -*- coding: utf-8 -*-
"""
Created on Jun 06 18:24:02 2022

@author: Jerome Yutai Shen

"""
from common_classes import ListNode
from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while right:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            right -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head
