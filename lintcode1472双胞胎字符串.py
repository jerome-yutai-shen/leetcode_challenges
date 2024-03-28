# -*- coding: utf-8 -*-
"""
Created on Dec 09 21:16:22 2023

@author: Jerome Yutai Shen

"""


def isTwin(s, t) -> bool:
    # Write your code here
    if (len(s) != len(t)):
        return False
    n = len(s)
    s1 = list(s)
    t1 = list(t)

    oddS = []
    evenS = []
    oddT = []
    evenT = []
    for i in range(n):
        if (i & 1):
            oddS.append(s1[i])
            oddT.append(t1[i])
        else:
            evenS.append(s1[i])
            evenT.append(t1[i])
    oddS.sort()
    oddT.sort()
    evenS.sort()
    evenT.sort()
    flag = 0
    len1 = len(oddS)
    len2 = len(evenS)
    for i in range(len1):
        if (oddS[i] != oddT[i]):
            flag = 1
    for i in range(len2):
        if (evenS[i] != evenT[i]):
            flag = 1
    if (flag):
        return False
    else:
        return True


def isTwin2(s: str, t: str) -> bool:
    from collections import Counter

    # Write your code here
    if (len(s) != len(t)):
        return False

    s_odd_cnt = Counter(s[0::2])
    t_odd_cnt = Counter(t[0::2])
    s_even_cnt = Counter(s[1::2])
    t_even_cnt = Counter(t[1::2])

    return s_odd_cnt == t_odd_cnt and s_even_cnt == t_even_cnt


if __name__ == "__main__":
    for s, t in (("abcd", "cdab"), ("abcd", "bcda")):
        assert isTwin(s, t) == isTwin2(s, t)