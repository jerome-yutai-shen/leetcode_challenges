# -*- coding: utf-8 -*-
"""
Created on Jun 26 12:06:03 2023

@author: Jerome Yutai Shen

A $ 100
|
+---B $ 100
+---C $ 200
    |
    +----D $ 60

"""
from typing import List, Optional


class TreeNode:
     def __init__(self, name: str, salary: int, children: Optional[List] = None):
         self.name = name
         self.salary = salary
         self.children = children
         self.num_members = 0
         self.sum_members_salary = 0


class Solution:

    def __init__(self, root: TreeNode):
        self.root = root
        self.num_underpaid_managers = 0

    def find_underpaid_managers(self, if_debug: bool = False) -> int:
        self.dfs_recurrsion(self.root, if_debug)
        return self.num_underpaid_managers

    def dfs_recurrsion(self, root: TreeNode, if_debug: bool = False) -> (int, int):
        if root is None or not root.children:
            return 0, 0

        for child in root.children:
            count, sum_memebers_salary = self.dfs_recurrsion(child)
            root.num_members += (count + 1)
            root.sum_members_salary += (child.salary + sum_memebers_salary)

            if if_debug:
                print(root.name, root.num_members, root.sum_members_salary, root.salary, root.sum_members_salary / root.num_members)

        if root.salary < root.sum_members_salary/root.num_members:
            self.num_underpaid_managers += 1

        return root.num_members, root.sum_members_salary


if __name__ == "__main__":
    root = TreeNode("A", 100, [TreeNode("B", 100, None), TreeNode("C", 200, [TreeNode("D", 600, None)])])
    solution = Solution(root)
    print(solution.find_underpaid_managers())