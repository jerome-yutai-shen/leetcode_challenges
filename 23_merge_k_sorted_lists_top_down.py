# -*- coding: utf-8 -*-
"""
Created on May 29 21:45:52 2022

@author: Jerome Yutai Shen

"""
from typing import List
from common_classes import ListNode


def merge_klists_top_down_merge(lists: List[list]):
    """
    自顶向下的归并的方法。 归并排序写熟练
    输入的list分成两半，
    之后合并两个有序链表

    lists = [[1,4,5],[1,3,4],[2,6]]

                   ___________________|_______________________
           _______|_______                        ____________|_____________
       ___|____       ____|____             _____|_______             ______|_____
      |        |     |         |           |             |           |            |
    list1   list2   list3   list4 ...  list n - 3    list n - 2  list n - 1    list n

    """
    if not lists:
        return None
    return merge_range_lists(lists, 0, len(lists) - 1)


def merge_range_lists(lists, start, end):
    if start == end:
        return lists[start]

    mid = (start + end) // 2
    left = merge_range_lists(lists, start, mid)
    right = merge_range_lists(lists, mid + 1, end)
    return merge_two_lists(left, right)


def merge_two_lists(head1, head2):
    tail = dummy = ListNode(0)
    while head1 and head2:
        if head1.val < head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1:
        tail.next = head1
    if head2:
        tail.next = head2

    return dummy.next


