# -*- coding: utf-8 -*-
"""
Created on May 29 21:46:46 2022

@author: Jerome Yutai Shen

"""
from typing import List
from common_classes import ListNode


def merge_klists_bottomup_merge(lists: List[list]):
    """
    自底向上的两两归并方法
    lists = [[1,4,5],[1,3,4],[2,6]]

    list1   list2   list3   list idx ... list n - 1    list n
      |_______|       |        |             |            |
          |___________|        |             |            |
              |________________|             |            |
                      |        ...           |            |
                               ...           |            |
                               |_____________|            |
                                      |___________________|
                                                 |

    while lists 元素数大于1：
        for 循环：
            0, new_list: [1 -> 1 -> 3 -> 4 -> 5], next_lists: [[1 -> 1 -> 3 -> 4 -> 5]]
            2, new_list: [2 -> 6] next_lists: [[1 -> 1 -> 3 -> 4 -> 5], [2 -> 6]]

        for 循环：
            0, [1 -> 1 -> 3 -> 4 -> 5] 与 [2 -> 6]] 合并
        lists 元素数等于1
        退出while循环
    """
    if not lists:
        return None

    while len(lists) > 1:
        next_lists = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                new_list = merge_two_lists(lists[i], lists[i + 1])
            else:
                new_list = lists[i]
            next_lists.append(new_list)

        lists = next_lists

    return lists[0]


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