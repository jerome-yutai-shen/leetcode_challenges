# -*- coding: utf-8 -*-
"""
Created on Jun 15 2025

@author: Jerome Yutai Shen

"""

from collections import defaultdict, deque

def alienOrder(words):
    successors = defaultdict(set)
    in_degree = {ch: 0 for word in words for ch in word}

    # 建图（根据相邻单词首个不同字母建立有向边）
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))
        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return ""  # 非法情况：前缀在后面
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in successors[c1]:  # 避免重复加边
                    successors[c1].add(c2)
                    in_degree[c2] += 1
                break
    print(in_degree)
    print(successors)
    # 初始化队列：所有入度为 0 的字母
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    res = []

    while queue:
        u = queue.popleft()
        res.append(u)
        for v in successors[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # 如果结果长度 != 节点数，说明有环（有依赖冲突）
    return "".join(res) if len(res) == len(in_degree) else ""



class Solution:
    def alienOrder(self, words: List[str]) -> str:
        return alienOrder(words)