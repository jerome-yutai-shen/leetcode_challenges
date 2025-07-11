# -*- coding: utf-8 -*-
"""
Created on Jul 02 18:39:25 2025

@author: Jerome Yutai Shen

"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        b_nodes = set()

        #traverse B
        while headB is not None:
            b_nodes.add(headB)
            headB = headB.next

        while headA is not None:
            if headA in b_nodes:
                return headA
            headA = headA.next

        return None