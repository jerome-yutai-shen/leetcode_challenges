# -*- coding: utf-8 -*-
"""
Created on Nov 26 16:30:08 2023

@author: Jerome Yutai Shen

"""
import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """O(n), O(n)"""
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


class SolutionSorting:
    """O(nlogn), O(1) or O(n)"""
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

    def majorityElementBM(self, nums):
        """
        Boyer-Moore Voting Algorithm
        O(n), O(1)
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]