# -*- coding: utf-8 -*-
"""
Created on Nov 26 22:42:06 2023

@author: Jerome Yutai Shen

"""
from typing import List
import collections


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """Let N be the length of strings and
        K be the maximum length of a string in strings.
        O(N*K), O(N*k)"""
        def shift_letter(letter: str, shift: int):
            return chr((ord(letter) - shift) % 26 + ord('a'))

        # Create a hash value
        def get_hash(string: str):
            # Calculate the number of shifts to make the first character to be 'a'
            shift = ord(string[0])
            return ''.join(shift_letter(letter, shift) for letter in string)

        # Create a hash_value (hashKey) for each string and append the string
        # to the list of hash values i.e. mapHashToList["abc"] = ["abc", "bcd"]
        groups = collections.defaultdict(list)
        for string in strings:
            hash_key = get_hash(string)
            groups[hash_key].append(string)

        # Return a list of all of the grouped strings
        return list(groups.values())