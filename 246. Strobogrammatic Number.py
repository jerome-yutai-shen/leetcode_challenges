# -*- coding: utf-8 -*-
"""
Created on Nov 26 22:38:17 2023

@author: Jerome Yutai Shen

"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        """
        双指针 O(N), O(1)
        """

        rotated_digits = { '0': '0', '1': '1', '8': '8', '6': '9', '9': '6' }

        left = 0
        right = len(num) - 1

        while left <= right:   # 有等号，可以相遇 只有一个数字比如“2”，应返回False
            if num[left] not in rotated_digits \
                    or rotated_digits[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True