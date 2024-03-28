# -*- coding: utf-8 -*-
"""
Created on Nov 26 22:30:19 2023

@author: Jerome Yutai Shen

To figure out an O(1) space requirement,
we would need to get this simple intuition first. For an array of length n:

There can be at most one majority element which is more than ⌊n/2⌋ times.
There can be at most two majority elements which are more than ⌊n/3⌋ times.
There can be at most three majority elements which are more than ⌊n/4⌋ times.
and so on.

"""


class Solution:

    def majorityElement(self, nums):
        if not nums:
            return []

        # 1st pass
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        # 2nd pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums) // 3:
                result.append(c)

        return result