# -*- coding: utf-8 -*-
"""
Created on Jun 05 21:24:44 2022

@author: Jerome Yutai Shen

"""
from common_classes import ListNode
from typing import Optional

def iter_three_pointers(head):
    """三指针迭代"""
    if not head or not head.next:
        return head

    begin = None
    mid = head
    end = head.next

    # 一直遍历
    while True:
        # 修改 mid 所指节点的指向
        mid.next = begin
        # 此时判断 end  是否为 NULL，如果成立则退出循环
        if end is None:
            break
        # 整体向后移动 3 个指针
        beg = mid
        mid = end
        end = end.next
        # 最后修改head头指针的指向
        head = mid
    return head


def recursive_approach(head):
    #递归的出口
    if not head or not head.next:
        return head
    #一直递归，找到链表中最后一个节点
    new_head = recursive_approach(head.next)
    # 当逐层退出时，new_head 的指向都不变，一直指向原链表中最后一个节点；
    # 递归每退出一层，函数中 head 指针的指向都会发生改变，都指向上一个节点。
    # 每退出一层，都需要改变 head.next 节点指针域的指向，同时令 head 所指节点的指针域为 None。
    head.next.next = head
    head.next = None
    # 每一层递归结束，都要将新的头指针返回给上一层。由此，即可保证整个递归过程中，能够一直找得到新链表的表头。
    return new_head


def recursive_approach2(head: Optional[ListNode]) -> Optional[ListNode]:
    # 递归终止条件是当前为空，或者下一个节点为空
    if (head == None or head.next == None):
        return head
    # 这里的cur就是最后一个节点
    tmp = head.next
    cur = recursive_approach2(tmp)
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

def head_insert(head):
    # 头插 设置新的头节点，把1->2->3->4->5依次取下来
    # 依次插入新头节点的next，并把该新头节点的现有next变成自己的next
    if head is None or head.next is None:
        return head

    new_head = None
    temp = None

    while head:
        temp = head
        #  将 temp 从 head 中摘除
        head = head.next
        #  将 temp 插入到 new_head 的头部
        temp.next = new_head
        new_head = temp

    return new_head


def reverse_list2(head: Optional[ListNode]) -> Optional[ListNode]:
    # 头插
    prev = ListNode(-1)
    while head:
        next = head.next  
        head.next= prev.next
        prev.next = head 
        head = next
    return prev.next


def in_site(head):
    if head is None or head.next is None:
        return head

    begin = head
    end = head.next
    while end:
        # 将 end 从链表中摘除
        begin.next = end.next;
        # 将 end 移动至链表头
        end.next = head
        head = end
        # 调整 end 的指向，另其指向 beg 后的一个节点，为反转下一个节点做准备
        end = begin.next
    
    return head

def in_site(head):
    if head is None or head.next is None:
        return head

    begin = head
    end = head.next
    head.next = None # 没有这句话就会产生cycle

    while end:
        # 将 end 从链表中摘除
        tmp = end.next
        # 将 end 移动至链表头
        end.next = head
        head = end
        # 调整 end 的指向，另其指向 beg 后的一个节点，为反转下一个节点做准备
        end = tmp
    
    return head

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

        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        """
        上述代码可以写成
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            或者
            curr.next, curr, prev = prev, curr.next, curr
            但是这样就会出错
            curr, prev, curr.next = curr.next, curr, prev
            
        When you write a parallel assignment
        x, y, z = a, b, c
        it's equivalent to
        
        temp = (a, b, c)
        x = temp[0]
        y = temp[1]
        z = temp[2]
            """
        return prev

    def reverseList21(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        leetcode 迭代
        """

        prev = None

        while head:
            next = head.next # 断开重连
            head.next = prev # 断开重连

            prev = head # 整体移动，冒名顶替
            head = next # 整体移动，冒名顶替

        return prev

    def reverseList迭代(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        begin, mid, end = None, head, head.next

        while True:
            mid.next = begin
            if end is None:
                break

            begin = mid
            mid = end
            end = end.next

        return mid

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

    def reverseList头插(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        头插
        """
        if not head or not head.next:
            return head

        new_head = temp = None

        while head:
            temp = head
            # 将temp从head中摘除
            head = head.next
            # 将temp插入到new_head的头部
            temp.next = new_head
            new_head = temp
        return new_head

    def reverseListInSite(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        begin = head
        end = head.next
        while end:
            # 将end从链表中摘除
            begin.next = end.next
            # 将end移动至链表头
            end.next = head
            head = end
            #调整end的指向，令其指向begin后的一个节点，为反转下一个节点做准备
            end = begin.next
        return head

    def reverseListInSite2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        begin, end = head, None
        while begin.next:
            end = begin.next
            begin.next = end.next
            end.next = head
            head = end
        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    new_head =solution.reverseList3(head)