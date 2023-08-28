# -*- coding: utf-8 -*-
"""
Created on Apr 18 18:56:02 2023

@author: Jerome Yutai Shen

"""
from common_classes import ListNode


class Solution:
    """
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here
        s1, s2 = 0, 0
        while l1:
            s1 = s1*10 + l1.val
            l1 = l1.next
        while l2:
            s2 = s2*10 + l2.val
            l2 = l2.next
        res = s1 + s2
        dummy = ListNode(0)
        head = dummy
        string = str(res)
        for k in range(len(string)):
            tmp = string[k]
            dummy.next = ListNode(int(tmp))
            dummy = dummy.next
        return head.next