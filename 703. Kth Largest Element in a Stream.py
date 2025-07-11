# -*- coding: utf-8 -*-
"""
Created on Jul 05 15:55:27 2025

@author: Jerome Yutai Shen

"""


import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)  # 转换为最小堆
        while len(self.heap) > k:
            heapq.heappop(self.heap)  # 保留 k 个最大的

    def add(self, val: int) -> int:
        """最安全写法就是：不让堆超过 k 个元素
        这个写法没有逻辑路径使得heap长度超过k
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)  # 替换堆顶（更快）
        return self.heap[0]