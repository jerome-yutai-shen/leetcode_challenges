# -*- coding: utf-8 -*-
"""
Created on Nov 11 18:26:48 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        words = set(wordDict)
        mem = {}
        def wordBreak(s):
          if s in mem: return mem[s]
          ans = []
          if s in words: ans.append(s)
          for i in range(1, len(s)):
            right = s[i:]
            if right not in words: continue
            ans += [w + " " + right for w in wordBreak(s[0:i])]
          mem[s] = ans
          return mem[s]
        return wordBreak(s)