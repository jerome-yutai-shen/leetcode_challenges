# -*- coding: utf-8 -*-
"""
Created on Jul 05 16:31:29 2025

@author: Jerome Yutai Shen

"""
import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []  # max heap for smaller half (use -num)
        self.min_heap = []  # min heap for larger half

    def addNum(self, num: int) -> None:
        # Step 1: 加入到 max_heap（取负数模拟大顶堆）
        heapq.heappush(self.max_heap, -num)
        # Step 2: 把最大堆的最大值（即最小数）移到最小堆
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        # Step 3: 平衡大小（max_heap 至少和 min_heap 一样多）
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # 如果两堆一样大 → 取平均值
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        # 如果不一样大，max_heap 多一个 → 取 max_heap 顶部
        return -self.max_heap[0]