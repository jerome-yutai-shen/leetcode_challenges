# -*- coding: utf-8 -*-
"""
Created on Nov 16 12:01:38 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:

    def findAllConcatenatedWordsInADict(self, words):
        words = set(words)

        def concatenated(word, memo = {}):
            if word not in memo:
                for j in range(1, len(word)):
                    if word[:j] in words and (word[j:] in words or concatenated(word[j:], memo)):
                        memo[word] = True
                        break
                else:
                    memo[word] = False
            return memo[word]

        return list(filter(concatenated, words))


class SolutionDP:
    """
    @param words: List[str]
    @return: return List[str]
    """

    def wordBreak(self, word, cands):
        if not cands:
            return False
        dp = [False] * (len(word) + 1)  # store whether w.substr(0, i) can be formed by existing words
        dp[0] = True  # empty string is always valid
        for i in range(1, len(word) + 1):
            for j in reversed(range(0, i)):
                if not dp[j]:
                    continue
                if word[j:i] in cands:
                    dp[i] = True
                    break
        return dp[-1]

    def findAllConcatenatedWordsInADict(self, words):
        # write your code here
        words.sort(key=lambda x: -len(x))
        cands = set(words)  # using hash for acceleration
        ans = []
        for i in range(0, len(words)):
            cands -= { words[i] }
            print(f"cands {cands}")
            if self.wordBreak(words[i], cands):
                ans += words[i],
        return ans