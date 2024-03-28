# -*- coding: utf-8 -*-
"""
Created on Oct 03 02:01:23 2023

@author: Jerome Yutai Shen

"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reversed_words = [word[::-1] for word in words]

        reversed_s = ' '.join(reversed_words)

        return reversed_s


if __name__ == "__main__":
    for s in ["Let's take LeetCode contest", "God Ding"]:
        print(Solution().reverseWords(s))