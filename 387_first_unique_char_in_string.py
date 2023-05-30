# -*- coding: utf-8 -*-
"""
Created on Jun 06 18:17:14 2022

@author: Jerome Yutai Shen

"""
from common_classes import ListNode
import collections


class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def firstUniqChar2(self, s):
        # Write your code here
        dummy = ListNode(None)
        tail = dummy
        tab, invalid = {}, object()
        for c in s:

            if c not in tab:
                print(f"c: {c}")
                node = ListNode(c)
                tab[c], tail.next, tail = tail, node, node
                print(f"node: {node}")
                print(f"tail.next {tail.next}")
                print(f"tail: {tail}")
            else:
                if tab[c] is invalid:
                    continue
                prv, nxt = tab[c], tab[c].next.next
                prv.next = nxt
                if nxt:
                    tab[nxt.val] = prv
                else:
                    tail = prv
                tab[c] = invalid

        return dummy.next.val if dummy.next else '0'

    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        print(f"count {count}")
        # find the index
        for idx, ch in enumerate(s):

            if count[ch] == 1:
                return idx  # leetcode asks for the index, not the char, whereas lintcode 209 asks for the char
        return -1