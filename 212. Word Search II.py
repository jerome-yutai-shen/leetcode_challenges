# -*- coding: utf-8 -*-
"""
Created on Jul 05 20:15:08 2025

@author: Jerome Yutai Shen

"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # 表示以该节点结尾的完整单词


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 构建 Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # 标记完整单词的结束

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            next_node = node.children[char]

            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # 去重：避免重复加入结果

            board[r][c] = '#'  # 标记访问

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)

            board[r][c] = char  # 恢复现场

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result