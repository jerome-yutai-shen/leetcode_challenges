# -*- coding: utf-8 -*-
"""
Created on Nov 22 08:52:19 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        # construct a dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][subset_sum]

    def canPartition2(self, nums: List[int]) -> bool:
        """
        判断是否可以将一个数组划分为两个元素和相同的子数组，假设总元素和为sum且sum是偶数，那么划分的两个子数组元素和为sum/2；
        若sum为奇数则无解。因此，我们可以将这题转化为求“从给定数组中选取元素放入容量为sum/2的背包，询问是否能装满”的问题。
令dp[i]表示是否有这样一种可行方案使得元素和为i，则状态转移方程： dp[i] = dp[i] or dp[i - x]
即对于元素x，对于已存在的每一个元素和∈[x,sum/2]，都要重新判断可行性：已经可行或者现在加上x可行都算可行，否则算不可行。
对于每一个元素和，需要从大到小依次转移，这样就能排除重复选择的干扰。
        :param nums:
        :return:
        """
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False] * target
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        print(dp)
        return dp[target]


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    _ = Solution()
    __ = _.canPartition2(nums)

