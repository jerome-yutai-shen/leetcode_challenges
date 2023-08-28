# -*- coding: utf-8 -*-
"""
Created on Jun 15 01:32:30 2022

@author: Jerome Yutai Shen

"""


def firstBadVersion(n: int) -> int:
    start = 1
    end = n
    while start + 1 < end:
        mid = (start + end) // 2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid
    if isBadVersion(start):
        return start
    elif isBadVersion(end):
        return end


if __name__ == "__main__":
    pass
