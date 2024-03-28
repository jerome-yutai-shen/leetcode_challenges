# -*- coding: utf-8 -*-
"""
Created on Aug 31 16:07:30 2023

@author: Jerome Yutai Shen

"""
from collections import Counter
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        counter_dict = Counter(n - int(str(n)[::-1]) for n in nums).values()
        counts = tuple(count * (count - 1) // 2 for count in counter_dict)
        print(counts)

        return sum(counts) % (10 ** 9 + 7)


if __name__ == "__main__":
    solution = Solution()
    solution.countNicePairs([42,11,1,97])
    solution.countNicePairs([13,10,35,24,76])
