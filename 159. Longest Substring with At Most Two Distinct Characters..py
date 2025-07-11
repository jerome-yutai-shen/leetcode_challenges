# -*- coding: utf-8 -*-
"""
Created on Jul 01 18:46:04 2025

@author: Jerome Yutai Shen

"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct2(self, s: str) -> int:
        """能跑通但是很笨"""
        if len(s) <= 1:
            return len(s)

        p_left, p_right = 0, 1
        max_len = p_right - p_left
        while p_left < len(s) and p_right < len(s):
            if len(set(list(s[p_left: (p_right + 1)]))) <= 2:
                p_right += 1
            else:
                p_left -= 1
            max_len = max(max_len, p_right - p_left)
            if p_right == len(s):
                break
        return max_len
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)

        from collections import defaultdict

        left = 0
        count = defaultdict(int)
        max_len = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while len(count) > 2:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

