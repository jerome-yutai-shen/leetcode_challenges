# -*- coding: utf-8 -*-
"""
Created on Jun 08 02:13:16 2022

@author: Jerome Yutai Shen

"""
import collections


class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for word in strs:
            ans[tuple(sorted(word))].append(word)
        return ans.values()