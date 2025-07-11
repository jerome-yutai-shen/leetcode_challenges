# -*- coding: utf-8 -*-
"""
Created on Jul 09 19:05:54 2025

@author: Jerome Yutai Shen

题目要求，以下两种情况返回True：
1 There is no word in dictionary whose abbreviation is equal to word's abbreviation.
2 For any word in dictionary whose abbreviation is equal to word's abbreviation, that word and word are the same.


"""


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbr_dict = { }
        for word in set(dictionary): # 这个题目的陷阱在这里 要用set 去重 而不是直接把list遍历一遍
            abbr = self.get_abbr(word)
            if abbr not in self.abbr_dict:
                self.abbr_dict[abbr] = word
            else:
                self.abbr_dict[abbr] = None

    def get_abbr(self, word: str):
        if len(word) < 3:
            return word
        else:
            return f"{word[0]}{len(word) - 2}{word[-1]}"

    def isUnique(self, word: str) -> bool:
        abbr = self.get_abbr(word)
        if abbr not in self.abbr_dict:
            return True
        else:
            return self.abbr_dict[abbr] == word
