# -*- coding: utf-8 -*-
"""
Created on Nov 26 11:45:45 2023

@author: Jerome Yutai Shen

"""
class Solution:
    """双指针"""
    def numberOfSubstrings(self, s: str) -> int:
        end = 0
        count_a = count_b = count_c = 0
        result = 0

        for start in range(len(s)):

            while end < len(s) and (not count_a * count_b * count_c):
                if s[end] == "a":
                    count_a += 1
                elif s[end] == "b":
                    count_b += 1
                elif s[end] == "c":
                    count_c += 1
                end += 1
            if count_a * count_b * count_c:
                result += len(s) - (end - 1) # while循环结束前加了1， 要减去

            # 接下来要右移左端点，那就会丢元素
            if s[start] == "a":
                count_a -= 1
            elif s[start] == "b":
                count_b -= 1
            elif s[start] == "c":
                count_c -= 1

        return result