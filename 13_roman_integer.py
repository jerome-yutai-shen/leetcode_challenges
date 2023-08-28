# -*- coding: utf-8 -*-
"""
Created on May 23 12:42:45 2022

@author: Jerome Yutai Shen

"""


class Solution:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}

    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and self.values[s[i]] < self.values[s[i + 1]]:
                total += self.values[s[i + 1]] - self.values[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += self.values[s[i]]
                i += 1
        return total
