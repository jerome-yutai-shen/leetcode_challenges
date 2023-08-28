# -*- coding: utf-8 -*-
"""
Created on Jun 08 05:52:21 2022

@author: Jerome Yutai Shen

"""
from common_classes import ListNode
from typing import Optional


def deleteDuplicates(head: ListNode) -> ListNode:
    # sentinel
    sentinel = ListNode(0, head)

    # predecessor = the last node
    # before the sublist of duplicates
    pred = sentinel

    while head:
        # if it's a beginning of duplicates sublist
        # skip all duplicates
        if head.next and head.val == head.next.val:
            # move till the end of duplicates sublist
            while head.next and head.val == head.next.val:
                head = head.next
            # skip all duplicates
            pred.next = head.next
            # otherwise, move predecessor
        else:
            pred = pred.next

            # move forward
        head = head.next

    return sentinel.next


