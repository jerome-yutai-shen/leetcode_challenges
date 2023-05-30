# -*- coding: utf-8 -*-
"""
Created on Jun 03 16:47:42 2022

@author: Jerome Yutai Shen

"""
from common_classes import ListNode


def reverse_linked_list(head, k):
    # Reverse k nodes of the given linked list.
    # This function assumes that the list contains
    # atleast k nodes.
    new_head, ptr = None, head
    while k:
        # Keep track of the next node to process in the
        # original list
        next_node = ptr.next

        # Insert the node pointed to by "ptr"
        # at the beginning of the reversed list
        ptr.next = new_head
        new_head = ptr

        # Move on to the next node
        ptr = next_node

        # Decrement the count of nodes to be reversed by 1
        k -= 1

    # Return the head of the reversed list
    return new_head


def reverse_kgroup(head: ListNode, k: int) -> ListNode:
    ptr = head
    ktail = None

    # Head of the final, moified linked list
    new_head = None

    # Keep going until there are nodes in the list
    while ptr:
        count = 0

        # Start counting nodes from the head
        ptr = head

        # Find the head of the next k nodes
        while count < k and ptr:
            ptr = ptr.next
            count += 1

        # If we counted k nodes, reverse them
        if count == k:
            # Reverse k nodes and get the new head
            rev_head = reverse_linked_list(head, k)

            # new_head is the head of the final linked list
            if not new_head:
                new_head = rev_head

            # ktail is the tail of the previous block of
            # reversed k nodes
            if ktail:
                ktail.next = rev_head

            ktail = head
            head = ptr

    # attach the final, possibly un-reversed portion
    if ktail:
        ktail.next = head

    return new_head if new_head else head