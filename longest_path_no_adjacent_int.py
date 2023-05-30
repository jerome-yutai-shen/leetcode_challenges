# -*- coding: utf-8 -*-
"""
Created on Apr 13 17:25:11 2023

@author: Jerome Yutai Shen

"""
from collections import deque

def solution_bfs(S: str, A: list):
    # Implement your solution here
    n = len(A)
    children_count = [0] * n
    for idx in range(1, n):
        children_count[A[idx]] += 1
    print(children_count)

    queue = deque([])
    longest_path = 1
    longest_chains = [[0, 0]] * n

    for node in range(1, n):
        if children_count[node] == 0:
            longest_chains[node][0] = 1
            queue.append(node)

    while queue:
        current_node = queue.popleft()
        parent_node = A[current_node]
        longest_path_from_current_node = longest_chains[current_node][0]
        if S[current_node] != S[parent_node]:
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


def get_tree(A: list) -> dict:
    children_count = {}
    for idx, p in enumerate(A):
        if idx > 0:
            if p not in children_count:
                children_count[p] = set()
            children_count[p].add(idx)
    return children_count

def solution_dfs(S, A):

    children_count = get_tree(A)
    def dfs(now):
        res = 1
        chain = 1

        for child in children_count.get(now, set()):
            r, c = dfs(child)
            res = max(res, r)
            if S[now] != S[child]:
                res = max(res, chain + c)
                chain = max(chain, c + 1)

        return res, chain

    return dfs(0)[0]


if __name__ == "__main__":
    print(get_tree([-1, 0, 0, 0, 2]))
