# -*- coding: utf-8 -*-
"""
Created on Oct 02 09:00:23 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry

        for x, y in edges:
            union(x, y)

        return len({ find(i) for i in range(n) })


if __name__ == "__main__":
    n = 5
    # edges = [[0, 1], [1, 2], [3, 4]]
    # print(Solution().countComponents(n, edges))
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(Solution().countComponents(n, edges))
