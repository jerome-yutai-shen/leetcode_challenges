# -*- coding: utf-8 -*-
"""
Created on Oct 01 00:04:42 2023

@author: Jerome Yutai Shen

"""
class UnionFind:

    def __init__(self):
        self.father = {}
        self.size_set = {}
        self._num_set = 0

    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        self.size_set[x] = 1
        self._num_set += 1

    def merge(self, x, y): # union
        root_x, root_y = self.find(x). self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.size_set[root_y] += self.size_set[root_x]
            self._num_set -= 1

    def find(self, x):
        root = x
        while self.father.get(root):
            root = self.father[root]

        while x is not None:
            x, self.father[x] = self.father[x], root
        return root

    def is_connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    @property
    def get_num_of_set(self):
        return self._num_set

    def get_size_of_set(self, x):
        return self.size_set[self.find(x)]


if __name__ == "__main__":
    uf = UnionFind()
    print(uf.get_num_of_set)
