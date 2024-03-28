# -*- coding: utf-8 -*-
"""
Created on Dec 17 23:50:24 2023

@author: Jerome Yutai Shen

"""


class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        ans, cnt = 0, 0
        pre = "."
        for ch in word:
            if abs(ord(ch) - ord(pre)) <= 1:
                cnt += 1
            else:
                ans += cnt // 2
                cnt = 1
            pre = ch
        ans += cnt // 2
        return ans


if __name__ == "__main__":
    _ = Solution()
    