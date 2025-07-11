# -*- coding: utf-8 -*-
"""
Created on Jul 05 10:27:01 2025

@author: Jerome Yutai Shen

"""


class TrieNode:
    def __init__(self):
        self.children = { }
        self.is_end = False  # 标记是否是一个单词的结尾


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.is_end

            ch = word[index]
            if ch == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(index + 1, node.children[ch])

        return dfs(0, self.root)
