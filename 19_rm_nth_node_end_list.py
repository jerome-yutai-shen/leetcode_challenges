# -*- coding: utf-8 -*-
"""
Created on May 26 17:14:30 2022

@author: Jerome Yutai Shen

"""
from typing import Optional, List, Union


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rm_nth_fromend(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    head = [1,2,3,4,5]
    n = 3
    """
    dummy = ListNode()
    dummy.next = head
    p_slow = dummy

    for _ in range(n):
        head = head.next

    while head:
        head = head.next
        p_slow = p_slow.next

    p_slow.next = p_slow.next.next

    return dummy.next


def init_slinked_list(n: Union[int, List[int]]):
    dummy = ListNode(0)
    if isinstance(n, int):
        n = list(range(1, n + 1))
    pntr = ListNode(n[0])  # 在head前加一个哑节点
    dummy.next = pntr

    for idx in n[1:]:
        pntr.next = ListNode(idx)
        pntr = pntr.next


if __name__ == "__main__":
    head = ListNode(0)
    pntr = ListNode(1)
    head.next = pntr

    for idx in range(2, 6):
        pntr.next = ListNode(idx)
        pntr = pntr.next



