# -*- coding: utf-8 -*-
"""
Created on Jun 08 03:22:57 2022

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not words:
            return []

        n = len(words)
        wordLens = [len(word) for word in words]
        results = []

        i = 0
        while i < n:
            temp, count, taken = [], 0, 0
            while i < n and maxWidth - count >= wordLens[i]:
                temp.append(words[i])
                count += wordLens[i] + 1
                taken += wordLens[i]
                i += 1

            if i == n:
                line = self.parse_last_line(temp, maxWidth, taken)
            else:
                line = self.parse_line(temp, maxWidth, taken)

            results.append(line)

        return results

    def parse_line(self, arr, maxWidth, taken):
        n_word, remains = len(arr), maxWidth - taken

        if n_word == 1:
            return arr[0] + ' ' * remains

        base, left = divmod(remains, n_word - 1)
        bases = [base] * (n_word - 1) + [0]

        for i in range(left):
            bases[i] += 1

        line = ''
        for i in range(n_word):
            line += arr[i] + ' ' * bases[i]

        return line

    def parse_last_line(self, arr, maxWidth, taken):
        n_word = len(arr)
        remains = maxWidth - taken - (n_word - 1)

        return ' '.join(arr) + ' ' * remains