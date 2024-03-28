# -*- coding: utf-8 -*-
"""
Created on Nov 13 16:29:31 2023

@author: Jerome Yutai Shen

"""
import heapq
from typing import Optional

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """九章 令狐冲, O(nlogn), O(1)"""
    def sortList(self, head):
        # write your code here
        def merge(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1

            head = None

            if list1.val < list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next

            tmp = head

            while list1 and list2:
                if list1.val < list2.val:
                    tmp.next = list1
                    list1 = list1.next
                else:
                    tmp.next = list2
                    list2 = list2.next
                tmp = tmp.next

            if list1:
                tmp.next = list1
            if list2:
                tmp.next = list2

            return head

        if not head or not head.next:
            return head

        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        list1 = self.sortList(head)
        list2 = self.sortList(mid)

        sorted = merge(list1, list2)
        print("九章 令狐冲")
        return sorted


class SolutionLHC:
    """九章 令狐冲 把merge作为类的一个方法 O(nlogn), O(1)"""

    def sortList(self, head: ListNode):
        # write your code here

        if not head or not head.next:
            return head

        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        list1 = self.sortList(head)
        list2 = self.sortList(mid)

        sorted = self.merge(list1, list2)
        print("九章 令狐冲")
        return sorted

    def merge(self, list1: ListNode, list2: ListNode):
        if not list1:
            return list2
        if not list2:
            return list1

        head = None

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        tmp = head

        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next

        if list1:
            tmp.next = list1
        if list2:
            tmp.next = list2

        return head


class SolutionTopDown:
    """
    Leetcode Top Down Merge Sort, O(nlohgn), O(logn)
    对于getMid存疑
    """

    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, list1, list2):
        dummy_head = ListNode(-1)
        tail = dummy_head

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy_head.next

    def getMid(self, head):
        midPrev = None  # java代码 ListNode midPrev = null;
        while head and head.next:
            midPrev = head if not midPrev else midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid


class SolutionSpaceO1:
    """
    Leetcode 讨论区答案 可行！
    """

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Function to merge two sorted linked lists
        def merge(left, right):
            dummy = ListNode()
            current = dummy

            # Merge elements in ascending order
            while left and right:
                if left.val < right.val:
                    current.next, left = left, left.next
                else:
                    current.next, right = right, right.next

                current = current.next

            # Attach remaining elements, if any
            current.next = left or right
            return dummy.next

        # Function to get the length of the linked list
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        length = get_length(head)
        dummy = ListNode(0)
        dummy.next = head

        step = 1
        while step < length:
            prev, current = dummy, dummy.next

            # Split, merge, and increment step size
            while current:
                left = current
                right = self.split(left, step)
                current = self.split(right, step)

                prev.next = merge(left, right)

                # Move to the end for the next iteration
                while prev.next:
                    prev = prev.next

            step *= 2

        return dummy.next

    # Function to split the linked list into two parts
    def split(self, head, step):
        if not head:
            return None

        # Move to the end of the first part
        for _ in range(step - 1):
            if not head.next:
                break
            head = head.next

        right = head.next
        head.next = None
        return right


# 使用快慢指针找到merge sort的中点，然后merge sorted的两个链表
class Solution2:

    def sortList(self, head):
        # write your code here
        if head is None or head.next is None:
            return head

        #快慢指针
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        return self.merge(self.sortList(head),self.sortList(mid))

    #对有序链表1和2进行merge
    def merge(self, l1, l2):

        dummy = ListNode(None)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next


# 快排版本
class SolutionQ:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """

    def sortList(self, head):
        if not head or not head.next:  # 只有0-1个节点，不用排
            return head

        mid = self.find_mid(head)  # 找pivot节点（用中间节点代替）
        # 创建3个辅助链表，分别存放大于，等于和小于 pivot 的节点
        dummy_l, dummy_m, dummy_r = ListNode(-1), ListNode(-1), ListNode(-1)
        tail_l, tail_m, tail_r = dummy_l, dummy_m, dummy_r

        while head:  # 遍历链表，做partition
            if (head.val < mid.val):
                tail_l.next = head
                tail_l = tail_l.next
            elif (head.val > mid.val):
                tail_r.next = head
                tail_r = tail_r.next
            else:
                tail_m.next = head
                tail_m = tail_m.next
            head = head.next

        tail_l.next = None
        tail_m.next = None
        tail_r.next = None

        sorted_left = self.sortList(dummy_l.next)  # 排好左边（小于Pivot 的节点）
        sorted_right = self.sortList(dummy_r.next)  # 排好右边（大于Pivot 的节点）
        return self.connect(sorted_left, dummy_m.next, sorted_right)  # 连接3个排好的链表成一个

    def find_mid(self, head):  # 快慢指针，快指针每次移两步，慢指针移一步。当快指针到头了，慢指针指向中间。
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def connect(self, left, mid, right):  # 把3个链表连成一个
        dummy = ListNode(-1, left)
        cur = dummy
        while cur.next:
            cur = cur.next
        cur.next = mid
        while cur.next:
            cur = cur.next
        cur.next = right
        return dummy.next


--------------------------------------------------------------------------------------------------------------------


# 归并版本
class SolutionM:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """

    def sortList(self, head):
        if not head or not head.next:
            return head
        # 把链表分成左右两半
        mid = self.find_mid(head)
        left = head
        right = mid.next
        mid.next = None

        sorted_left = self.sortList(left)
        sorted_right = self.sortList(right)

        return self.merge(sorted_left, sorted_right)

    def find_mid(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, l1, l2):  # 参见Lintcode#165
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next


class Solution0:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """

    def sortList(self, head):
        def merge(list1, list2):
            if list1 == None:
                return list2
            if list2 == None:
                return list1

            head = None

            if list1.val < list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next

            tmp = head

            while list1 != None and list2 != None:
                if list1.val < list2.val:
                    tmp.next = list1
                    tmp = list1
                    list1 = list1.next
                else:
                    tmp.next = list2
                    tmp = list2
                    list2 = list2.next

            if list1 != None:
                tmp.next = list1
            if list2 != None:
                tmp.next = list2

            return head

        if head == None:
            return head
        if head.next == None:
            return head

        fast = head
        slow = head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        list1 = self.sortList(head)
        list2 = self.sortList(mid)

        sorted = merge(list1, list2)

        return sorted


class Solution1:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = []
        idx = 0 # idx 的存在就是为了入堆，入堆时比较大小
        while head:
            heapq.heappush(h, (-head.val, idx, head))
            head = head.next
            idx += 1

        node = prev = None
        while h:
            _, _, node = heapq.heappop(h)
            node.next = prev
            prev = node

        return node


if __name__ == "__main__":
    heads = [4,19,14,5,-3,1,8,5,11,15]
    head = ListNode(heads[0])
    p = head
    for _ in heads[1:]:
        p.next = ListNode(_)
        p = p.next

    h = []
    i = 0
    p = head
    while p:
        heapq.heappush(h, (-p.val, p))
        p = p.next