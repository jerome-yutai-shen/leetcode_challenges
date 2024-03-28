# -*- coding: utf-8 -*-
"""
Created on Dec 17 23:46:52 2023

@author: Jerome Yutai Shen

"""
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map: character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1