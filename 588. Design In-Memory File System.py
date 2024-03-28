# -*- coding: utf-8 -*-
"""
Created on Dec 28 03:31:40 2023

@author: Jerome Yutai Shen

"""


class FileSystem:

    def __init__(self):
        self.root = { }

    def ls(self, path: str) -> List[str]:
        node, name = self.find_path(path)
        if not node:
            return []
        elif '#' in node:
            return [name]
        else:
            return sorted(node.keys())

    def mkdir(self, path: str) -> None:
        self.create_path(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.create_path(filePath)
        if '#' in node:
            node['#'] += content
        else:
            node['#'] = content

    def readContentFromFile(self, filePath: str) -> str:
        node, _ = self.find_path(filePath)
        return node.get('#', '') if node else ''

    # Helpers
    #########
    def find_path(self, path: str) -> Dict:
        """
        travelse to the trie node if exists, otherwise return None
        """
        if path == '/': return (self.root, path)
        path = path.split('/')[1:]
        node = self.root
        for d in path:
            if d not in node:
                return (None, None)
            node = node[d]
        return (node, path[-1])

    def create_path(self, path: str) -> Dict:
        """
        create dir if any mid dir doesn't exist
        """
        path = path.split('/')[1:]
        node = self.root
        for d in path:
            if d not in node:
                node[d] = { }
            node = node[d]
        return node
