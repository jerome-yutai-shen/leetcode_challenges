# -*- coding: utf-8 -*-
"""
Created on Jun 07 05:12:49 2022

@author: Jerome Yutai Shen

"""


class Solution:

    def countAndSay(self, n: int) -> str:
        prev = "1"
        for i in range(n - 1):
            curr = ""
            pos = 0
            start = 0

            while pos < len(prev):
                while pos < len(prev) and prev[pos] == prev[start]:
                    pos += 1
                curr += str(pos - start) + prev[start]
                start = pos
            prev = curr

        return prev