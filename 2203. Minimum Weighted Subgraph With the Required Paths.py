# -*- coding: utf-8 -*-
"""
Created on Aug 31 16:24:29 2023

@author: Jerome Yutai Shen

"""
import heapq
from collections import defaultdict
from typing import List


def dijkstra(n, graph, start):
    dist = [float('inf')] * n
    dist[start] = 0
    minheap = [(0, start)]
    
    while minheap:
        d, u = heapq.heappop(minheap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(minheap, (dist[v], v))
    return dist


class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
    
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        
        for u, v, w in edges:
            graph[u].append((v, w))
            reverse_graph[v].append((u, w))  # for reverse dijkstra
        
        d1 = dijkstra(n, graph, src1)
        d2 = dijkstra(n, graph, src2)
        d3 = dijkstra(n, reverse_graph, dest)  # reverse graph: compute dist to dest
        
        min_total = float('inf')
        for i in range(n):
            if d1[i] < float('inf') and d2[i] < float('inf') and d3[i] < float('inf'):
                min_total = min(min_total, d1[i] + d2[i] + d3[i])
        
        return min_total if min_total < float('inf') else -1
