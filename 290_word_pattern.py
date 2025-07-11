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

    def wordPattern3(self, pattern: str, s: str) -> bool:
        """严谨写法"""
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        pattern_word = { }
        word_pattern = { }

        for char, word in zip(pattern, words):
            has_c = char in pattern_word
            has_w = word in word_pattern

            if has_c and has_w:
                if pattern_word[char] != word or word_pattern[word] != char:
                    return False
            elif not has_c and not has_w:
                pattern_word[char] = word
                word_pattern[word] = char
            else:
                # 只有一个存在（单向映射），违反双射规则
                return False

        return True

    def wordPattern4(self, pattern: str, s: str) -> bool:
        """不够严谨， 因为用None做了值比较"""
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        pattern_word = { }
        word_pattern = { }

        for char, word in zip(pattern, words):

            if char not in pattern_word and word not in word_pattern:

                pattern_word[char] = word
                word_pattern[word] = char

            else:
                if pattern_word.get(char) != word or word_pattern.get(word) != char:
                    return False

        return True

if __name__ == "__main__":
    pattern = "abba"
    s = "dog dog dog dog"
    solution = Solution()
    solution.wordPattern(pattern, s)