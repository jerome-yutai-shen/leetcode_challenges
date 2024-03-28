# -*- coding: utf-8 -*-
"""
Created on Nov 21 17:06:34 2023

@author: Jerome Yutai Shen

"""


def reverseWords2(s: str) -> str:
    """
    O(n), O(n)
    """
    tmp = s.split()
    ans = []
    while tmp:
        ans.append(tmp.pop())
    return " ".join(ans)