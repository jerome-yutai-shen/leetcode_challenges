# -*- coding: utf-8 -*-
"""
Created on May 25 12:25:41 2022

@author: Jerome Yutai Shen

"""

from typing import Dict, List
import itertools


KEYBOARD: Dict[str, str] = {
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


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []

        def backtrack(index: int, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return  # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            possible_letters = KEYBOARD[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations

    def letterCombinations2(self, digits: str):
        if not digits:
            return []

        res = []

        def backtrack(index: int, path):
            if index == len(digits):
                res.append(path)
                return
            for char in KEYBOARD[digits[index]]:
                backtrack(index + 1, path + char)

        backtrack(0, "")
        return res

    def with_itertools(self, digits: str) -> List[str]:
        if not digits:
            return []

        groups = [KEYBOARD[d] for d in digits]
        return [''.join(p) for p in itertools.product(*groups)]


if __name__ == "__main__":
    digits = "2385"
    print(letterCombinations2(digits))
