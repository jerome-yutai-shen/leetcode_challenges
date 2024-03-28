# -*- coding: utf-8 -*-
"""
Created on Nov 25 11:57:57 2023

@author: Jerome Yutai Shen

"""
from typing import List


def beautifulSubsets1(self, nums: List[int], k: int) -> int:
    """O(2 ** n), O(n)"""
    ans = -1  # 去掉空集
    cnt = [0] * (max(nums) + k * 2)  # 用数组实现比哈希表更快
    def dfs(i: int) -> None:
        if i == len(nums):
            nonlocal ans
            ans += 1
            return
        dfs(i + 1)  # 不选
        x = nums[i]
        if cnt[x - k] == 0 and cnt[x + k] == 0:
            cnt[x] += 1  # 选
            dfs(i + 1)
            cnt[x] -= 1  # 恢复现场
    dfs(0)
    return ans


def beautifulSubsets2(self, nums: List[int], k: int) -> int:
    ans = -1  # 去掉空集
    cnt = [0] * (max(nums) + k * 2)  # 用数组实现比哈希表更快
    def dfs(i: int) -> None:  # 从 i 开始选
        nonlocal ans
        ans += 1
        if i == len(nums):
            return
        for j in range(i, len(nums)):  # 枚举选哪个
            x = nums[j]
            if cnt[x - k] == 0 and cnt[x + k] == 0:
                cnt[x] += 1  # 选
                dfs(j + 1)
                cnt[x] -= 1  # 恢复现场
    dfs(0)
    return ans


from collections import defaultdict, Counter
def beautifulSubsets_dp(nums: List[int], k: int) -> int:
    """就是抢劫那道题的翻版 O(nlogn), O(n)"""
    groups = defaultdict(Counter)
    for x in nums:
        groups[x % k][x] += 1
    ans = 1
    for cnt in groups.values():
        g = sorted(cnt.items())
        m = len(g)
        f = [0] * (m + 1)
        f[0] = 1
        f[1] = 1 << g[0][1]
        for i in range(1, m):
            if g[i][0] - g[i - 1][0] == k:
                f[i + 1] = f[i] + f[i - 1] * ((1 << g[i][1]) - 1)
            else:
                f[i + 1] = f[i] << g[i][1]
        ans *= f[m]
    return ans - 1  # -1 去掉空集


if __name__ == "__main__":
    nums = [2, 4, 6]
    beautifulSubsets_dp(nums, 2)

