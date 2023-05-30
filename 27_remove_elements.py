    # -*- coding: utf-8 -*-
"""
Created on Jun 03 21:10:23 2022

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Input: nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2,_,_]

        Input: nums = [0,1,2,2,3,0,4,2], val = 2
        Output: 5, nums = [0,1,4,0,3,_,_,_]
        """
        if not nums:
            return 0

        p_start, p_end = 0, len(nums) - 1

        while p_start <= p_end:
            if nums[p_start] != val:
                p_start += 1
            else:
                nums[p_start] = nums[p_end]
                p_end -= 1

        return p_start


if __name__ == "__main__":
    xx = Solution()
    nums, val = [3, 2, 2, 3], 3
    print(xx.removeElement(nums, val))
    nums, val = [0,1,2,2,3,0,4,2], 2
    print(xx.removeElement(nums, val))

