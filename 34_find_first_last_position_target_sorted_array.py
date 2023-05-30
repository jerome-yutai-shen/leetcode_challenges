# -*- coding: utf-8 -*-
"""
Created on Jun 07 02:06:10 2022

@author: Jerome Yutai Shen

"""
from typing import List


class SearchRange:

    def binary_search_approach(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.find_bound(nums, target, True)
        if lower_bound == -1:
            return [-1, -1]

        upper_bound = self.find_bound(nums, target, False)
        return [lower_bound, upper_bound]

    def find_bound(self, nums: List[int], target: int, isFirst: bool) -> int:
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = int((begin + end) / 2)

            if nums[mid] == target:

                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    # Search on the left side for the bound.
                    end = mid - 1
                else:

                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid

                    # Search on the right side for the bound.
                    begin = mid + 1

            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1

        return -1


class SearchRange2:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        lower_bound = self.binary_search_first(nums, target)
        if lower_bound == -1:
            return [-1, -1]
        upper_bound = self.binary_search_last(nums, target)
        return [lower_bound, upper_bound]

    def binary_search_first(self, nums: List[int], target: int) -> int:
        p_start, p_end = 0, len(nums) - 1

        while p_start + 1 < p_end:
            p_mid = (p_start + p_end) // 2
            if nums[p_mid] > target:
                p_end = p_mid
            elif nums[p_mid] < target:
                p_start = p_mid
            else:
                p_end = p_mid

        if nums[p_start] == target:
            return p_start

        if nums[p_end] == target:
            return p_end

        return -1

    def binary_search_last(self, nums: List[int], target: int) -> int:
        p_start, p_end = 0, len(nums) - 1

        while p_start + 1 < p_end:
            p_mid = (p_start + p_end) // 2
            if nums[p_mid] > target:
                p_end = p_mid
            elif nums[p_mid] < target:
                p_start = p_mid
            else:
                p_start = p_mid

        if nums[p_end] == target:
            return p_end

        if nums[p_start] == target:
            return p_start

        return -1


def find_bound(nums: List[int], target: int, isFirst: bool) -> int:
    """
    用九章算法模板改写leetcode标准答案
    :param nums:
    :param target:
    :param isFirst: True就是找第一个 False就是找最后一个
    :return:
    """
    begin, end = 0, len(nums) - 1
    while begin + 1 < end:
        mid = (begin + end) // 2

        if nums[mid] == target:

            if isFirst:
                # This means we found our lower bound.
                if mid == begin: # or nums[mid - 1] < target:
                    return mid

                # Search on the left side for the bound.
                end = mid  # - 1
            else:

                # This means we found our upper bound.
                if mid == end: # or nums[mid + 1] >  target:
                    return mid

                # Search on the right side for the bound.
                begin = mid  # + 1

        elif nums[mid] > target:
            end = mid  # - 1
        else:
            begin = mid  # + 1

    if isFirst:
        if nums[begin] == target:
            return begin
        if nums[end] == target:
            return end
    else:
        if nums[end] == target:
            return end
        if nums[begin] == target:
            return begin

    return -1


if __name__ == "__main__":
    for nums, target in [[[1, 2, 3], 2],
                         [[2, 2], 2],
                         [[5, 7, 7, 8, 8, 10], 8]]:
        l_b = find_bound(nums, target, True)
        u_b = find_bound(nums, target, False)
        print(l_b, u_b)