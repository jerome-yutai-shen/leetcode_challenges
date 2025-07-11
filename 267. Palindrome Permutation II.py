# -*- coding: utf-8 -*-
"""
Created on Jul 10 12:18:32 2025

@author: Jerome Yutai Shen

"""
from collections import Counter
from typing import List

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        count = Counter(s)
        odd_chars = [char for char, freq in count.items() if freq % 2 == 1]
        if len(odd_chars) > 1:
            return []  # 无法构成回文

        # 构造一半字符
        half = []
        for char, freq in count.items():
            half.extend([char] * (freq // 2))

        # 中间字符（若有）
        mid = odd_chars[0] if odd_chars else ''

        res = []
        used = [False] * len(half)
        # 排序后可以跳过重复元素
        half.sort()

        def backtrack(path):
            if len(path) == len(half):
                half_str = ''.join(path)
                res.append(half_str + mid + half_str[::-1])
                return
            for i in range(len(half)):
                if used[i]:
                    continue
                # 避免重复排列
                if i > 0 and half[i] == half[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                backtrack(path + [half[i]])
                used[i] = False

        backtrack([])

        return res


# 47 47 中的 path 是在原地维护的、共用的 list，所以要手动 push/pop。
# 267 中的 path 是递归参数，使用的是 path + [half[i]] 这种“复制延伸”的方式，所以不需要 pop。
class Solution47:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)
        nums.sort()

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue  # 去重的关键：同层中避免重复使用相同元素
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return res


class Solution复用path:
    def generatePalindromes(self, s: str) -> List[str]:
        count = Counter(s)
        odd_chars = [ch for ch, freq in count.items() if freq % 2 == 1]
        if len(odd_chars) > 1:
            return []

        half = []
        for ch, freq in count.items():
            half.extend([ch] * (freq // 2))
        half.sort()

        mid = odd_chars[0] if odd_chars else ''
        used = [False] * len(half)
        res = []
        path = []

        def backtrack():
            if len(path) == len(half):
                half_str = ''.join(path)
                res.append(half_str + mid + half_str[::-1])
                return
            for i in range(len(half)):
                if used[i]:
                    continue
                if i > 0 and half[i] == half[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(half[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return res
