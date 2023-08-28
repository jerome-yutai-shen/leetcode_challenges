# -*- coding: utf-8 -*-
"""
Created on Jul 13 19:46:16 2023

@author: Jerome Yutai Shen

leetcode 39 原题！！！ 丢死人了！

nums List[int], no duplicate elements, all positive
target: int

find all combinations of elements, so that sum equals to target
each elements can be used as many time as necessary

nums = [2, 3, 6 , 7]
target = 7

ans = [[7], [2, 2, 3]]

nums = [2, 4, 6, 7]
target = 7
ans = [[7]]

nums = [2, 4, 6, 7]
target = 8
ans = [[2, 6], [2, 2, 4], [2, 2, 2, 2]]

"""
from typing import List, Set


def solution(nums: List[int], target: int) -> Set:
    results = set()
    nums.sort()
    if target < nums[0]:
        return results

    p_right = len(nums) - 1
    while p_right >= 0 and target >= nums[p_right]:
        res = helper(nums[: (p_right + 1)], target)
        p_right -= 1
        if res:
            results.add(tuple(res))

    return results

def helper(nums: List[int], target: int) -> List:
    res = []
    if target == nums[-1] or target == nums[0]:
        print(f"target: {target}, nums: {nums}, res: {res}")
        res.append(target)
        return res
    elif target < nums[0]:
        print(f"target: {target}, nums: {nums}, res: {res}")
        return res
    else:
        res.extend(helper(nums, target - nums[-1]))
        if res:
            res.append(nums[-1])

    return res

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:

    results = []

    def backtrack(remain, comb, start):
        if remain == 0:
            # make a deep copy of the current combination
            results.append(list(comb))
            return
        elif remain < 0:
            # exceed the scope, stop exploration.
            return

        for idx in range(start, len(candidates)):
            # add the number into the combination
            comb.append(candidates[idx])
            # give the current number another chance, rather than moving on
            backtrack(remain - candidates[idx], comb, idx)
            # backtrack, remove the number from the combination
            comb.pop()

    backtrack(target, [], 0)

    return results


if __name__ == "__main__":
    nums = [7, 6, 3, 2]
    target = 8
    # print(solution(nums, target))
    print(combinationSum(nums, target))
    """ 
    nums = [2, 4, 6, 7]
    target = 7
    print(solution(nums, target))

    nums = [2, 3, 6, 7]
    target = 8
    print(solution(nums, target))

    nums = [2, 4, 6, 7]
    target = 8
    print(solution(nums, target))
    """


