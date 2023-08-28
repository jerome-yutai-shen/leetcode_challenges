# -*- coding: utf-8 -*-
"""
Created on Jun 08 10:50:38 2022

@author: Jerome Yutai Shen

"""


class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """

    def isScramble(self, s1, s2):
        n = len(s1)

        f = dict()

        f[(0, 0, 0, 0)] = True

        return self.dfs(s1, s2, 0, n, 0, n, f)

    def dfs(self, s1, s2, i1, j1, i2, j2, f):
        if (i1, j1, i2, j2) in f:
            return f[(i1, j1, i2, j2)]
        elif j1 - i1 != j2 - i2:
            f[(i1, j1, i2, j2)] = False
            return f[(i1, j1, i2, j2)]
        elif i1 + 1 == j1:
            f[(i1, j1, i2, j2)] = s1[i1] == s2[i2]
            return f[(i1, j1, i2, j2)]
        else:
            for k in range(i1 + 1, j1):
                if self.dfs(s1, s2, i1, k, i2, i2 + (k - i1), f) and \
                        self.dfs(s1, s2, k, j1, i2 + (k - i1), j2, f):
                    f[(i1, j1, i2, j2)] = True
                    return f[(i1, j1, i2, j2)]
                if self.dfs(s1, s2, i1, k, j2 - (k - i1), j2, f) and \
                        self.dfs(s1, s2, k, j1, i2, j2 - (k - i1), f):
                    f[(i1, j1, i2, j2)] = True
                    return f[(i1, j1, i2, j2)]
            f[(i1, j1, i2, j2)] = False
            return f[(i1, j1, i2, j2)]