# -*- coding: utf-8 -*-
"""
Created on Feb 12 14:32:46 2024

@author: Jerome Yutai Shen

253 meeting room

"""
from typing import List
from collections import defaultdict
import collections
import itertools


def maxIntersectionCount(y: List[int]) -> int:

    curr_intv = (min(y[:2]), max(y[:2]))
    count = defaultdict(int)
    count[curr_intv] = 1

    for idx in range(1, len(y) - 1):
        intvl0 = [y[idx], y[idx + 1]]
        intvl_1 = [y[idx - 1], y[idx]]
        intersect = (max(min(intvl0), curr_intv[0]), min(max(intvl0), curr_intv[1]))
        if (intvl0[1] - intvl0[0]) * (intvl_1[1] - intvl_1[0]) > 0:
            continue
        if intersect[0] < intersect[1] and curr_intv[0] <= intersect[0] <= curr_intv[1] and curr_intv[0] <= intersect[1] <= curr_intv[1]:
            count[curr_intv] += 1
        else:
            curr_intv = tuple(intvl_1)
            count[curr_intv] = 2

    max_count = 0
    for k in count:
        max_count = max(max_count, count[k])
    print(count)
    return max_count


def maxIntersectionCount2(y: List[int]) -> int:
    ans = 0
    intersectionCount = 0
    line = collections.Counter()

    for i, (a, b) in enumerate(itertools.pairwise(y)):
      start = 2 * a
      end = 2 * b + (0 if i == len(y) - 2 else -1 if b > a else 1)
      line[min(start, end)] += 1
      line[max(start, end) + 1] -= 1

    for count in sorted(line):
      intersectionCount += line[count]
      ans = max(ans, intersectionCount)

    return ans


def maxIntersectionCount3(y: List[int]) -> int:
    events = {}
    N = len(y)
    for i,x in enumerate(y):
        if x not in events:
            events[x] = [0,0]
        if i == 0:
            if y[0] > y[1]:
                events[x][1] -= 1
            else:
                events[x][0] += 1
        elif i == len(y) - 1:
            if y[N-2] > y[N-1]:
                events[x][0] += 1
            else:
                events[x][1] -= 1
        else:
            if y[i] > y[i-1] and y[i] > y[i+1]:
                events[x][0] -= 1
                events[x][1] -= 1
            elif y[i] < y[i-1] and y[i] < y[i+1]:
                events[x][0] += 1
                events[x][1] += 1

    ys = sorted(list(set(y)))
    print(events, ys)
    res = 0
    curr = 0
    for coor in ys:
        curr += events[coor][0]
        res = max(res,curr)
        curr += events[coor][1]
        res = max(res,curr)

    events1 = {}
    N = len(y)
    for i,x in enumerate(y):
        if x not in events1:
            events1[x] = [0,0]
        if i == 0:
            if y[0] > y[1]:
                events1[x][1] += 1
            else:
                events1[x][0] -= 1
        elif i == len(y) - 1:
            if y[N-2] > y[N-1]:
                events1[x][0] -= 1
            else:
                events1[x][1] += 1
        else:
            if y[i] > y[i-1] and y[i] > y[i+1]:
                events1[x][0] += 1
                events1[x][1] += 1
            elif y[i] < y[i-1] and y[i] < y[i+1]:
                events1[x][0] -= 1
                events1[x][1] -= 1

    ys1 = sorted(list(set(y)), reverse = True)
    print(events1, ys1)
    res2 = 0
    curr2 = 0
    for coor in ys1:
        curr2 += events1[coor][1]
        res2 = max(res2,curr2)
        curr2 += events1[coor][0]
        res2 = max(res2,curr2)
        print(res2)
    print(res, res2)
    return res

def maxIntersectionCount4(y: List[int]) -> int:

    events1 = { }
    N = len(y)
    for i, x in enumerate(y):
        if x not in events1:
            events1[x] = [0, 0]
        if i == 0:
            if y[0] > y[1]:
                events1[x][1] += 1
            else:
                events1[x][0] -= 1
        elif i == len(y) - 1:
            if y[N - 2] > y[N - 1]:
                events1[x][0] -= 1
            else:
                events1[x][1] += 1
        else:
            if y[i] > y[i - 1] and y[i] > y[i + 1]:
                events1[x][0] += 1
                events1[x][1] += 1
            elif y[i] < y[i - 1] and y[i] < y[i + 1]:
                events1[x][0] -= 1
                events1[x][1] -= 1

    ys1 = sorted(list(set(y)), reverse=True)
    print(events1, ys1)
    res2 = 0
    curr2 = 0
    for coor in ys1:
        curr2 += events1[coor][1]
        res2 = max(res2, curr2)
        curr2 += events1[coor][0]
        res2 = max(res2, curr2)
        # print(res2)

    return res2

if __name__ == "__main__":
    y = [2, 1, 3, 4, 5]
    print(maxIntersectionCount3(y),  maxIntersectionCount2(y))

    y = [1, 2, 1, 2, 1, 3, 2]
    print(maxIntersectionCount3(y),  maxIntersectionCount2(y))

    y = [1, 2, 1, 2, 1, 2, 1,20,18,20,18,20,18,20,18,20,18,20,18,20,17,20,17,20,17,21,17,21,17,21,17]
    print(maxIntersectionCount3(y),  maxIntersectionCount2(y))

    y = [1,20,18,20,18,20,18,20,18,20,18,20,18,20,17,20,17,20,17,21,17,21,17,21,17]
    print(maxIntersectionCount3(y),  maxIntersectionCount2(y))

    y = [1,2,3]
    print(maxIntersectionCount3(y),  maxIntersectionCount2(y))

    y = [2,1,3]
    print(maxIntersectionCount3(y),  maxIntersectionCount2(y))

    y = [3,2,1]
    print(maxIntersectionCount3(y),  maxIntersectionCount2(y))

    y = [34,93,84,36]
    print(maxIntersectionCount3(y),  maxIntersectionCount2(y))

    y = [21, 7, 61, 31, 5]
    print(maxIntersectionCount3(y),  maxIntersectionCount2(y))

    y = [1, 2, 1, 2, 1, 100, 95, 100, 95, 100, 95]
    print(maxIntersectionCount3(y),  maxIntersectionCount2(y))

    y = [2,3,4,3,4,1,4,1,2,3,4,2,1,2,1,3,2]
    print(maxIntersectionCount3(y), maxIntersectionCount2(y))

    y = [2,1,100,1,2]
    print(maxIntersectionCount3(y), maxIntersectionCount2(y))


    import pandas as pd
    df = pd.DataFrame(data = {"y": y})
    # df.plot(marker='.', color = 'r')