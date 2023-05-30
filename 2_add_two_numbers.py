# -*- coding: utf-8 -*-
"""
Created on Jun 07 20:05:48 2022

@author: Jerome Yutai Shen

"""
from common_classes import ListNode

class Solution:
    def addTwoNumbers(self, l1, l2) -> ListNode:
        dummy = ListNode(None)
        tail = dummy
        carry = 0
        while l1 or l2:  # or carry:

            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            digit, carry = carry % 10, carry // 10
            node = ListNode(digit)
            tail.next, tail = node, node

        return dummy.next

    """ """


class Solution2:
    def addTwoNumbers(self, l1, l2) -> ListNode:
        s1, s2 = 0, 0
        while l1:
            s1 = s1 * 10 + l1.val
            l1 = l1.next
        while l2:
            s2 = s2 * 10 + l2.val
            l2 = l2.next
        res = s1 + s2
        dummy = ListNode(0)
        head = dummy
        string = str(res)[::-1]
        for k in range(len(string)):
            tmp = string[k]
            dummy.next = ListNode(int(tmp))
            dummy = dummy.next
        return head.next