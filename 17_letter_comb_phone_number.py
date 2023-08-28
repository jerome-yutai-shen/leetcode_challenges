# -*- coding: utf-8 -*-
"""
Created on May 25 12:25:41 2022

@author: Jerome Yutai Shen

"""
from typing import List


KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        if not digits:
            return []

        results = []
        self.dfs(digits, 0, [], results)

        return results

    def dfs(self, digits, index, chars, results):
        if index == len(digits):
            results.append(''.join(chars))
            return

        for letter in KEYBOARD[digits[index]]:
            chars.append(letter)
            self.dfs(digits, index + 1, chars, results)
            chars.pop()


#
LETTERS = ("", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")


def letterCombinations2(digits: str) -> List[str]:
    prefixes = []
    for digit in digits:
        stems = []
        letters = LETTERS[int(digit)]
        for letter in letters:
            if prefixes:
                for prefix in prefixes:
                    stems.append(prefix + letter)
            else:
                stems.append(letter)

        prefixes = stems

    return prefixes


if __name__ == "__main__":
    digits = "2385"
    print(letterCombinations2(digits))
