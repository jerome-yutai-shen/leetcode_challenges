# -*- coding: utf-8 -*-
"""
Created on May 29 15:45:50 2022

@author: Jerome Yutai Shen

"""
from typing import List
from common_classes import ListNode


def merge_klists_heap(lists: List[list]):
    """
    使用 heap 的做法。 要注意 python 里需要重载一下 ListNode 的小于比较函数。
    """

    import heapq

    # overwrite the compare function
    # so that we can directly put ListNode into heapq
    ListNode.__lt__ = lambda x, y: (x.val < y.val)

    if not lists:
        return None

    dummy = ListNode(0)
    tail = dummy
    heap = []
    for head in lists:
        if head:
            heapq.heappush(heap, head)

    while heap:
        head = heapq.heappop(heap)
        tail.next = head
        tail = head
        if head.next:
            heapq.heappush(heap, head.next)

    return dummy.next

