# -*- coding: utf-8 -*-
"""
Created on Dec 29 04:10:49 2023

@author: Jerome Yutai Shen

把原数组的0换成-1，就可以用前缀和来做。

如果折线图在两个不同的下标具有相同的y值，
说明这两个下标之间的连续数组具有相同数量的0和1，
用hash表记录每个y值第一次出现的下标值，
下次再遇到已经存储在hash的y值，就可以直接计算出数组下标的距离间隔.

"""
def find_max_length(nums: list):
    hashmap = { 0: -1 }
    max_len = count = 0
    for idx, num in enumerate(nums):
        count = count + (1 if num else -1)
        if count in hashmap:
            max_len = max(max_len, idx - hashmap.get(count))
        else:
            hashmap[count] = idx

    return max_len