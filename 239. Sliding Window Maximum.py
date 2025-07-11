# -*- coding: utf-8 -*-
"""
Created on Jul 05 12:22:44 2025

@author: Jerome Yutai Shen

"""
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """单调队列"""
        res = []
        dq = deque()  # store index

        for i in range(len(nums)):
            # 删除不在窗口的元素
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            # 保持单调性：移除小于当前值的元素
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            # print(i,dq)
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res

    def max_sliding_window(self, nums: list[int], k: int) -> list[int]:
        """

        """
        dq = deque()  # 存索引
        res = []

        for i in range(len(nums)):
            # 弹出窗口外的元素
            if dq and dq[0] < i - k + 1: # 这个地方while if都可以
                dq.popleft()

            # 弹出队尾比当前值小的元素，保持单调递减
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # 形成一个完整窗口后，输出最大值
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res