# -*- coding: utf-8 -*-
"""
Created on Oct 21 16:27:30 2023

@author: Jerome Yutai Shen

"""
from typing import List
import numpy as np


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        nums2 = np.diff([nums[0]] + nums)
        longest_streak = 1
        current_streak = 1

        for num in nums2:
            if num == 1:
                current_streak += num
            elif num != 0:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        return max(longest_streak, current_streak)

    def longestConsecutive2(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)


if __name__ == "__main__":
    _ = Solution()
    for nums in [[100,4,200,1,3,2], [0,3,7,2,5,8,4,6,0,1], [0, 1, 2, 1]]:
        print(_.longestConsecutive(nums))
        print(_.longestConsecutive2(nums))
