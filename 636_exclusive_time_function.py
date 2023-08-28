# -*- coding: utf-8 -*-
"""
Created on Jun 20 20:57:35 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0 for i in range(n)]
        last_timestamp = 0
        for str in logs:
            log = str.split(':')
            func_id, action, timestamp = int(log[0]), log[1], int(log[2])
            if action == 'start':
                if stack:
                    result[stack[-1]] += timestamp - last_timestamp
                stack.append(func_id)
            else:
                timestamp += 1
                func_id = stack.pop()
                result[func_id] += timestamp - last_timestamp
            last_timestamp = timestamp
        return result