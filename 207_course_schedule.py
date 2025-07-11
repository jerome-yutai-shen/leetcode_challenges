# -*- coding: utf-8 -*-
"""
Created on Sep 28 17:39:59 2023

@author: Jerome Yutai Shen

"""
from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        # print(adj)

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1
        print(indegree)

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        print(queue)
        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return nodesVisited == numCourses


class Solution2:
    def canFinish(self, numCourses, prerequisites) -> bool:

        return num_finished == numCourses

if __name__ == "__main__":
    func = Solution().canFinish
    func(2, [[1, 0]])
    func(2, [[1, 0], [0, 1]])