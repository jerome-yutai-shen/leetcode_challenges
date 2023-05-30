# -*- coding: utf-8 -*-
"""
Created on Jun 14 05:11:51 2022

@author: Jerome Yutai Shen

"""
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> refs/remotes/origin/main
from typing import Optional, List
from common_classes import BinaryTreeNode, ListNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[BinaryTreeNode]:
        return self.dfs(head)

    def dfs(self, head):

        if head == None:
            return None

        if head.next == None:
            return BinaryTreeNode(head.val)

        dummy = ListNode(0)
        dummy.next = head
        fast = head
        slow = dummy

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        parent = BinaryTreeNode(temp.val)

        parent.left = self.dfs(head)
        parent.right = self.dfs(temp.next)

        return parent
<<<<<<< HEAD
=======
=======



>>>>>>> 9b01741 (linux)
>>>>>>> refs/remotes/origin/main


if __name__ == "__main__":
    pass
