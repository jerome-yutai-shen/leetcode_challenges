# -*- coding: utf-8 -*-
"""
Created on Jul 05 15:51:53 2025

@author: Jerome Yutai Shen

"""
from collections import deque


LIMITATION = 300 # s


class HitCounter:
    def __init__(self):
        self.q = deque()

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # 清除超过300秒的旧点击
        while self.q and self.q[0] <= timestamp - LIMITATION:
            self.q.popleft()
        return len(self.q)