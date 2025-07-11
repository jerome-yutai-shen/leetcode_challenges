# -*- coding: utf-8 -*-
"""
Created on Jul 02 20:28:37 2025

@author: Jerome Yutai Shen

"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """
        一些cornercases没考虑到比如
        s = "c"
        t = "c"
        s = "a"
        t = ""
        s = "ca"
        t = "c"
        """
        ns, nt = len(s), len(t)
        if abs(ns - nt) > 1 or s == t:
            return False

        for idx in range(min(ns, nt)):
            if s[idx] != t[idx]:
                if ns == nt:
                    return s[idx+1:] == t[idx+1:]
                elif ns > nt:
                    return s[idx+1:] == t[idx:]
                else:
                    return s[idx:] == t[idx+1:]
        return abs(ns - nt) == 1