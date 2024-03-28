# -*- coding: utf-8 -*-
"""
Created on Nov 10 17:01:02 2023

@author: Jerome Yutai Shen

"""
import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Time Complexity : O(nlogn) OR O(n+klogk).
        Space Complexity: O(n)
        """
        counter = collections.Counter(s)
        ans = []
        for c, ocurr in counter.most_common():
            ans.append(c * ocurr)

        return "".join(ans)


    def frequencySort2(self, s: str) -> str:
        """
        bucket sort
        O(n), O(n)
        """
        if not s:
            return s

        # Determine the frequency of each character.
        counts = collections.Counter(s)
        max_freq = max(counts.values())

        # Bucket sort the characters by frequency.
        buckets = [[] for _ in range(max_freq + 1)]
        for c, i in counts.items():
            buckets[i].append(c)

        # Build up the string.
        string_builder = []
        for i in range(len(buckets) - 1, 0, -1):
            for c in buckets[i]:
                string_builder.append(c * i)

        return "".join(string_builder)