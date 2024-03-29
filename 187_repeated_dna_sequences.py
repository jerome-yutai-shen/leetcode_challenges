# -*- coding: utf-8 -*-
"""
Created on Oct 16 03:18:19 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        seen, output = set(), set()

        # iterate over all sequences of length L
        for start in range(n - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                output.add(tmp)
            seen.add(tmp)
        return list(output)


if __name__ == "__main__":
    _ = Solution()
    print(_.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print(_.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
