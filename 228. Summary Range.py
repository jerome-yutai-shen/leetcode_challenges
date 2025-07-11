# -*- coding: utf-8 -*-
"""
Created on Jul 04 19:27:46 2025

@author: Jerome Yutai Shen

"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res

        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                # 断了，要把前面的区间保存
                if start == nums[i - 1]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i - 1]}")
                start = nums[i]  # 新的起点

        # 收尾
        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")

        return res