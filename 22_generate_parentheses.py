# -*- coding: utf-8 -*-
"""
Created on May 29 11:43:48 2022

@author: Jerome Yutai Shen

"""
from typing import List


def generate_parenthesis(n):
    result = []
    dfs(0, 0, '', n, result)
    return result


def dfs(left_count, right_count, nowSeq, n, result):
    # 每边的括号数小于等于 n
    if left_count > n or right_count > n:
        return
    # 左括号个数一定小于等于右括号
    if left_count < right_count:
        return

    # 满足条件，将nowSeq加入result
    if left_count == n and right_count == n:
        result.append(nowSeq)

    # 搜索加左括号的情况
    dfs(left_count + 1, right_count, nowSeq + '(', n, result)

    # 搜索加右括号的情况
    dfs(left_count, right_count + 1, nowSeq + ')', n, result)


"""
令狐冲
回溯. 逐个字符添加, 生成每一种组合.

一个状态需要记录的有: 当前字符串本身, 左括号数量, 右括号数量.

递归过程中解决:

如果当前右括号数量等于括号对数 n, 那么当前字符串即是一种组合, 放入解中.
如果当前左括号数量等于括号对数 n, 那么当前字符串后续填充满右括号, 即是一种组合.
如果当前左括号数量未超过 n:
如果左括号多于右括号, 那么此时可以添加一个左括号或右括号, 递归进入下一层
如果左括号不多于右括号, 那么此时只能添加一个左括号, 递归进入下一层
"""
class Solution:
    # @param an integer
    # @return a list of string
    # @draw a decision tree when n == 2, and you can understand it!
    def generate_parenthesis(self, n: int) -> List[str]:
        all_patterns = []
        if n:
            self.helpler(n, n, '', all_patterns)
        return all_patterns

    def helpler(self, num_lp: int, num_rp: int, pattern: str, all_patterns: List[str]):
        if num_rp < num_lp:
            return
        if num_lp == 0 and num_rp == 0:
            all_patterns.append(pattern)
        if num_lp > 0:
            self.helpler(num_lp - 1, num_rp, pattern + '(', all_patterns)
        if num_rp > 0:
            self.helpler(num_lp, num_rp - 1, pattern + ')', all_patterns)


"""
n = 1
的时候一对括号 （）。 n = 2
的时候拿到n = 1
的结果，然后一对括号从左到右插一遍。 n = 3
的时候拿到n = 2
的结果，然后一对括号从左到右插一遍。 每次拆解为n - 1。
"""


def generate_parenthesis2(n):
    # write your code here
    # print(f"n {n}")
    if n == 0:
        return []
    if n == 1:
        return ['()']

    all_patterns = set([])
    for ptn in generate_parenthesis2(n - 1):
        # print(f"ptn {ptn}, n {n}")
        for i in range(1, len(ptn) + 1):
            new_pattern = ptn[:i] + '(' + ptn[i:i + 1] + ')' + ptn[i + 1:]
            if new_pattern not in all_patterns:
                all_patterns.add(new_pattern)
    # print(f"all_patterns {all_patterns}")
    return list(all_patterns)


if __name__ == "__main__":
    generate_parenthesis2(3)

