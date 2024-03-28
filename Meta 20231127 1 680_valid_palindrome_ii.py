# -*- coding: utf-8 -*-
"""
Created on Nov 27 10:50:16 2023

@author: Jerome Yutai Shen
2023年11月27日面试题

"""
def is_palindrome(s: str, left: int, right: int) -> bool:
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True


class Solution2:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1: return True

        res = True
        l, r = 0, len(s) - 1

        def palindrome(a):
            l, r = 0, len(a) - 1
            while l < r:
                if a[l] == a[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if palindrome(s[:l] + s[l + 1:]) or palindrome(s[:r] + s[r + 1:]) is True:
                    return True
                else:
                    return False
        return res