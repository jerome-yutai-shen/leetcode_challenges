# -*- coding: utf-8 -*-
"""
Created on May 27 14:18:25 2022

@author: Jerome Yutai Shen

"""

class ListNode:

    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next


def merge_sorted_lists(list1, list2)-> ListNode:
    dummy = ListNode(-1)
    pntr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            pntr.next = list1
            list1 = list1.next
        else:
            pntr.next = list2
            list2 = list2.next
        pntr = pntr.next

    pntr.next = list1 or list2
    return dummy.next


