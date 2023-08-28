# -*- coding: utf-8 -*-
"""
Created on May 25 17:46:08 2022

@author: Jerome Yutai Shen

无向图 最短路径 用BFS
"""
from typing import List
import collections


INITIAL_PATTERN = "0000"
NUM_WHEELS = 4
WHEEL_ROTATE = (-1, 1, )
IMPOSSIBLE = -1


def openLock(deadends: List[str], target: str) -> int:
    """
    deadends = ["0201","0101","0102","1212","2002"],
    target = "0202"
    """
    dead_set = set(deadends)
    queue = collections.deque()
    queue.append((INITIAL_PATTERN, 0))
    visited = {INITIAL_PATTERN}

    while queue:
        # print(queue)
        pattern, step = queue.popleft()
        if pattern in dead_set:
            continue

        if pattern == target:  # short the circuit
            return step

        for i in range(NUM_WHEELS):
            num = int(pattern[i])
            for dx in WHEEL_ROTATE:
                num_new = (num + dx) % 10
                pattern1 = pattern[:i] + str(num_new) + pattern[i + 1:]

                if pattern in dead_set:
                    continue

                if pattern1 == target: # short the circuit
                    return step + 1

                if pattern1 not in visited:
                    queue.append((pattern1, step + 1))
                    visited.add(pattern1)

    return IMPOSSIBLE


if __name__ == "__main__":
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    xx = openLock(deadends, target)
