# -*- coding: utf-8 -*-
"""
Created on Dec 13 09:47:25 2023

@author: Jerome Yutai Shen

"""
import itertools

class Solution:
  def diffWaysToCompute(self, input):
    ops = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           '*': lambda x, y: x * y}
    def ways(s):
      ans = []
      for i in range(len(s)):
        if s[i] in "+-*":
          ans += [ops[s[i]](l, r) for l, r in itertools.product(ways(s[0:i]), ways(s[i+1:]))]
      if not ans: ans.append(int(s))
      return ans
    return ways(input)