# -*- coding: utf-8 -*-
"""
Created on Feb 12 11:38:09 2024

@author: Jerome Yutai Shen

"""
def merge_alternately(word1: str, word2: str):
    p1 = p2 = 0
    m_str = ""
    if not word1:
        return word2
    elif not word2:
        return word1

    while p1 < len(word1) and p2 < len(word2):
        m_str += word1[p1]
        p1 += 1
        m_str += word2[p2]
        p2 += 1

    if p1 == len(word1) and p2 < len(word2):
        m_str += word2[p2:]
    elif p2 == len(word2) and p1 < len(word1):
        m_str += word1[p1:]

    return m_str