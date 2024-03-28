# -*- coding: utf-8 -*-
"""
Created on Sep 07 19:13:28 2023

@author: Jerome Yutai Shen

"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        pattern_word = {}
        word_pattern = {}

        if len(pattern) != len(words):
            return False

        for char, word in zip(pattern, words):
            if char not in pattern_word:
                if word in word_pattern:
                    assert word_pattern.get(word) != char
                    return False
                pattern_word[char] = word
                word_pattern[word] = char
            else:
                if pattern_word.get(char) != word:
                    return False

        return True


    def wordPattern2(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        pattern_word = {}
        word_pattern = {}

        if len(pattern) != len(words):
            return False

        for char, word in zip(pattern, words):
            if char not in pattern_word:
                pattern_word[char] = word
                word_pattern[word] = char

            if word_pattern.get(word) != char:
                return False

            if pattern_word.get(char) != word:
                return False




        return True


if __name__ == "__main__":
    pattern = "abba"
    s = "dog dog dog dog"
    solution = Solution()
    solution.wordPattern(pattern, s)