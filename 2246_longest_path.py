N# -*- coding: utf-8 -*-
"""
Created on Apr 14 23:39:45 2023

@author: Jerome Yutai Shen

"""

from collections import deque, defaultdict
from typing import List


class Solution:

    def solution_dfs(self, parent: List[int], s: str) -> int:
        children_count = {}
        for idx, p in enumerate(parent):
            if idx > 0:
                if p not in children_count:
                    children_count[p] = set()
                children_count[p].add(idx)

        def dfs(now):
            res = 1
            chain = 1

            for child in children_count.get(now, set()):
                r, c = dfs(child)
                res = max(res, r)
                if s[now] != s[child]:
                    res = max(res, chain + c)
                    chain = max(chain, c + 1)

            return res, chain

        return dfs(0)[0]

    def solution_dfs2(self, parent: List[int], s: str) -> int:
        children_count = defaultdict(set)
        for idx, p in enumerate(parent):
            if idx > 0:
                children_count[p].add(idx)

        def dfs(now):
            res = 1
            chain = 1

            for child in children_count[now]: # get 方法 dict和defaultdict功能一致，不存在的key会返回None，所以应该用[]
                r, c = dfs(child)
                res = max(res, r)
                if s[now] != s[child]:
                    res = max(res, chain + c)
                    chain = max(chain, c + 1)

            return res, chain

        return dfs(0)[0]

    def solution_bfs(self, parent: List[int], s: str) -> int:
        n = len(parent)
        children_count = [0] * n
        for idx in range(1, n):
            children_count[parent[idx]] += 1
        print(f"children_count: {children_count}")

        queue = deque([])
        longest_path = 1
        longest_chains = []

        for node in range(n):
            longest_chains.append([0, 0])
        print(f"longest_chains: {longest_chains}")

        for node in range(1, n):
            if children_count[node] == 0:
                longest_chains[node][0] = 1
                queue.append(node)
        print(f"queue: {queue}, longest_chains: {longest_chains}")

        while queue:
            current_node = queue.popleft()
            parent_node = parent[current_node]
            longest_path_from_current_node = longest_chains[current_node][0]
            if s[current_node] != s[parent_node]:
                if longest_path_from_current_node > longest_chains[parent_node][0]:
                    longest_chains[parent_node][1] = longest_chains[parent_node][0]
                    longest_chains[parent_node][0] = longest_path_from_current_node
                elif longest_path_from_current_node > longest_chains[parent_node][1]:
                    longest_chains[parent_node][1] = longest_path_from_current_node

            longest_path = max(longest_path,
                               longest_chains[parent_node][0] + longest_chains[parent_node][1] + 1)

            children_count[parent_node] -= 1

            if children_count[parent_node] == 0 and parent_node != 0:
                longest_chains[parent_node][0] += 1
                queue.append(parent_node)

        return longest_path


