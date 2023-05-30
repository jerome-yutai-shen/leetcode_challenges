# -*- coding: utf-8 -*-
"""
Created on May 30 16:02:48 2022

@author: Jerome Yutai Shen

"""
from typing import Optional
from common_classes import ListNode


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    dummy = ListNode(0)
    dummy.next = head
    p = dummy
    while p.next and p.next.next:
        tmp = p.next.next
        p.next.next = tmp.next
        tmp.next = p.next
        p.next = tmp
        p = p.next.next
    return dummy.next


def swap_pairs2(head):
    """
    O  A B C D ...
    ^  <->
    O  B A C D ...
         ^ <->
    O  B A D C
             ^
    """
    dummy = ListNode(0, head)
    head = dummy

    while head.next and head.next.next:
        first, second, rest = head.next, head.next.next, head.next.next.next
        # node second 赋值给 head.next
        # node rest 赋值给 first.next
        # node first 赋值给 second.next
        # 最后 把first节点赋值给下一轮开始的头指针
        head.next, second.next, first.next, head = second, first, rest, first

    return dummy.next