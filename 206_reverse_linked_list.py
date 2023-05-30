# -*- coding: utf-8 -*-
"""
Created on Jun 05 21:24:44 2022

@author: Jerome Yutai Shen

"""
from common_classes import ListNode
from typing import Optional


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # 递归终止条件是当前为空，或者下一个节点为空
    if (head == None or head.next == None):
        return head
    # 这里的cur就是最后一个节点
    tmp = head.next
    cur = reverse_list(tmp)
    # 这里请配合动画演示理解
    # 如果链表是 1->2->3->4->5，那么此时的cur就是5
    # 而head是4，head的下一个是5，下下一个是空
    # 所以head.next.next 就是5->4
    print(f"cur: {cur.val, cur.next}")
    tmp.next = head
    # 防止链表循环，需要将head.next设置为空
    head.next = None
    # 每层递归函数都返回cur，也就是最后一个节点
    print(f"head: {head}， head.next == cur {head.next == cur}, id cur: {id(cur)}, id head: {id(head)}")
    return cur


def reverse_list2(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    prev = None
    while head:
        next = head.next  # current 之后的串 赋值
        head.next = prev  # 断开现在的连接, 改成新连接
        prev = head
        head = next
    return prev


def reverse_list3(head: Optional[ListNode]) -> Optional[ListNode]:
    if (not head) or (not head.next):
        return head

    p = reverse_list3(head.next)
    head.next.next = head
    head.next = None
    return p