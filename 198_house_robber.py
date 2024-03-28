# -*- coding: utf-8 -*-
"""
Created on Oct 21 22:22:41 2023

@author: Jerome Yutai Shen

"""
from typing import Optional, List

class Solution:

    def rob(self, nums: List[int]) -> int:

        # Special handling for empty case.
        if not nums:
            return 0

        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)

        # Base case initialization.
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]

        # DP table calculations.
        for i in range(N - 2, -1, -1):
            # Same as recursive solution.
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])

        return maxRobbedAmount[0]

    def rob2(self, nums: List[int]) -> int:

        # Special handling for empty case.
        if not nums:
            return 0

        N = len(nums)

        rob_next_plus_one = 0
        rob_next = nums[N - 1]

        # DP table calculations.
        for i in range(N - 2, -1, -1):
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])

            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current

        return rob_next

    def houseRobber(self, A):
        if A == []:
            return 0

        n = len(A)
        dp = [[0] * 2 for _ in range(n)]

        dp[0][0], dp[0][1] = 0, A[0]

        for i in range(1, n):
            # 如果不抢第 i 个，取前 i - 1 个位置 dp 较大值
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            # 如果抢第 i 个，前一个不抢，考虑从前 i - 2 个位置的dp值转移
            dp[i][1] = A[i] + dp[i - 1][0]
        print(dp)
        return max(dp[n - 1][0], dp[n - 1][1])

    def houseRobber2(self, A):
        if not A:
            return 0
        if len(A) <= 2:
            return max(A)

        f = [0] * 3
        f[0], f[1] = A[0], max(A[0], A[1])

        for i in range(2, len(A)):
            f[i % 3] = max(f[(i - 1) % 3], f[(i - 2) % 3] + A[i])
            print(f)
        return f[(len(A) - 1) % 3]


    def rob3(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
            # write your code here
        dp = [0 for i in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[:2])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


    def rob4(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums[:2])

        t1 = t2 = 0

        for current in nums:
            t1, t2 = max(current + t2, t1), t1
            print(t1, t2)

        return t1

if __name__ == "__main__":
    nums = [2, 1, 7, 9, 3, 1]
    _ = Solution()
    _.houseRobber(nums)
    _.houseRobber2(nums)
