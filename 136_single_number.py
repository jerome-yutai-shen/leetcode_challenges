# -*- coding: utf-8 -*-
"""
Created on Oct 23 19:01:54 2023

@author: Jerome Yutai Shen

"""
from collections import defaultdict, Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i


class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)


class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i # 异或满足结合律交换律
            print(i, a)
        return a


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for num in counter:
            if counter.get(num) == 1:
                return num