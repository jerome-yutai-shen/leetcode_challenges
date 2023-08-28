# -*- coding: utf-8 -*-
"""
Created on Jun 21 01:49:19 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def min_subarrays_required(max_sum_allowed: int) -> int:
            current_sum = 0
            splits_required = 0

            for element in nums:
                # Add element only if the sum doesn't exceed max_sum_allowed
                if current_sum + element <= max_sum_allowed:
                    current_sum += element
                else:
                    # If the element addition makes sum more than max_sum_allowed
                    # Increment the splits required and reset sum
                    current_sum = element
                    splits_required += 1

            # Return the number of subarrays, which is the number of splits + 1
            return splits_required + 1

        # Define the left and right boundary of binary search
        left = max(nums)
        right = sum(nums)
        while left <= right:
            # Find the mid value
            max_sum_allowed = (left + right) // 2

            # Find the minimum splits. If splits_required is less than
            # or equal to m move towards left i.e., smaller values
            if min_subarrays_required(max_sum_allowed) <= m:
                right = max_sum_allowed - 1
                minimum_largest_split_sum = max_sum_allowed
            else:
                # Move towards right if splits_required is more than m
                left = max_sum_allowed + 1

        return minimum_largest_split_sum

    def splitArray2(self, nums, m):

        def valid(mid):
            cnt = 0
            current = 0
            for n in nums:
                current += n
                if current > mid:	#如果当前连续和大于mid
                    cnt += 1		#计数+1
                    if cnt >= m:
                        return False
                    current = n		#current更新为num
            return True

        l = max(nums)	#确定二分查找的左右端点
        h = sum(nums)

        while l < h:
            mid = l + (h - l) // 2
            if valid(mid):	#二分check
                h = mid
            else:
                l = mid + 1
        return l