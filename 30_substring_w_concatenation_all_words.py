# -*- coding: utf-8 -*-
"""
Created on Jun 07 00:12:30 2022

@author: Jerome Yutai Shen

"""
from typing import List
import collections

from itertools import permutations
import re


class Solution2:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        错误解法
        """
        results = []
        all_perms = self.get_perm(len(words))
        for _ in all_perms:
            word = "".join(words[idx] for idx in _)
            results.extend([_.start() for _ in (re.finditer(word, s))]) # 这一步错了，"aa", "aaa" 只返回0 "aa", "aaaa"只返回0，2=
        return list(set(results))

    def get_perm(self, num_words: int) -> tuple:
        return tuple(permutations(range(num_words)))


class Solution:

    def findSubstring0(self, s, words):
        """
        O(n*a*b - (a*b) ** 2), O(a+b)
        """
        dict_w = collections.Counter(words)
        w_size = len(words[0])
        total = w_size * len(words)

        n = len(s)
        res = []
        for i in range(n - total + 1):

            strings = [s[k:k + w_size] for k in range(i, i + total, w_size)]
            print(f"strings {strings}")
            dict_s = collections.Counter(strings)

            if dict_s == dict_w:
                res.append(i)
        return res

    def findSubstring2(self, s, words):

        return [i for i in range(len(s) - len(words[0]) * len(words) + 1)
                if collections.Counter(words) == collections.Counter(
                [s[k:k + len(words[0])] for k in range(i, i + len(words[0]) * len(words), len(words[0]))])]

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def check(i):
            # Copy the original dictionary to use for this index
            remaining = word_count.copy()
            words_used = 0

            # Each iteration will check for a match in words
            for j in range(i, i + substring_size, word_length):
                sub = s[j: j + word_length]
                if remaining[sub] > 0:
                    remaining[sub] -= 1
                    words_used += 1
                else:
                    break

            # Valid if we used all the words
            return words_used == k

        answer = []
        for i in range(n - substring_size + 1):
            if check(i):
                answer.append(i)

        return answer

    def findSubstring3(self, s: str, words: List[str]) -> List[int]:
        """
        Given n as the length of s, a as the length of words, and b as the length of each word
        O(a+n⋅b), O(a+b)
        """
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def sliding_window(left):
            words_found = collections.defaultdict(int)
            words_used = 0
            excess_word = False

            # Do the same iteration pattern as the previous approach - iterate
            # word_length at a time, and at each iteration we focus on one word
            for right in range(left, n, word_length):
                if right + word_length > n:
                    break

                sub = s[right: right + word_length]
                if sub not in word_count:
                    # Mismatched word - reset the window
                    words_found = collections.defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length  # Retry at the next index
                else:
                    # If we reached max window size or have an excess word
                    while right - left == substring_size or excess_word:
                        # Move the left bound over continously
                        leftmost_word = s[left: left + word_length]
                        left += word_length
                        words_found[leftmost_word] -= 1

                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            # This word was the excess word
                            excess_word = False
                        else:
                            # Otherwise we actually needed it
                            words_used -= 1

                    # Keep track of how many times this word occurs in the window
                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        # Found too many instances already
                        excess_word = True

                    if words_used == k and not excess_word:
                        # Found a valid substring
                        answer.append(left)

        answer = []
        for i in range(word_length):
            sliding_window(i)

        return answer


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    sol = Solution()
    _1 = sol.findSubstring0(s, words)
    _2 = sol.findSubstring(s, words)