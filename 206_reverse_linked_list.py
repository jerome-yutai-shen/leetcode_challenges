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


class Solution:
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归
        """
        if (not head) or (not head.next):
            if not head:
                print(f"head type: {type(head)}")
            else:
                print(f"head is a node, and head is {head.val}, head.next is {head.next}")

            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

    def reverseList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        头插
        """
        if not head:
            return head

        new_head = ListNode(-1)

        while head:
            next = head.next # 断开重连
            head.next = new_head.next # 断开重连
            new_head.next = head # 断开重连

            head = next # 整体移动，冒名顶替

        return new_head.next

    def reverseList21(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        leetcoe 迭代
        """

        prev = None

        while head:
            next = head.next # 断开重连
            head.next = prev # 断开重连

            prev = head # 整体移动，冒名顶替
            head = next # 整体移动，冒名顶替

        return prev

    def reverseList_3p(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        p_prev = None
        p_curr = head

        while p_curr:
            p_next, p_curr.next  = p_curr.next, p_prev # 交换

            p_prev = p_curr # 整体移动，冒名顶替
            p_curr = p_next # 整体移动，冒名顶替

        return head

    def reverseList_iter(self, head):
        if not head or not head.next:
            return head

        p_begin = None
        p_mid = head
        p_end = head.next

        while True:
            p_mid.next = p_begin
            if p_end is None:
                break
            """
            整体向后移动 3 个指针
            """
            p_begin = p_mid
            p_mid = p_end
            p_end = p_end.next
            """
            最后修改 head 头指针的指向
            """
            head = p_mid

        return head




if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    new_head =solution.reverseList3(head)