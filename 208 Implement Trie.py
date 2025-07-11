# -*- coding: utf-8 -*-
"""
Created on Jul 03 21:35:28 2025

@author: Jerome Yutai Shen

"""

class Trie:

    def __init__(self):
        self._dict = {}

    def insert(self, word: str) -> None:
        node = self._dict
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]

        node["#"] = True

    def search(self, word: str) -> bool:
        node = self._dict
        for ch in word:
            if not ch in node:
                return False
            node = node[ch]

        return node.get("#") is True


    def startsWith(self, prefix: str) -> bool:
        node = self._dict
        for ch in prefix:
            if not ch in node:
                return False
            node = node[ch]

        return True