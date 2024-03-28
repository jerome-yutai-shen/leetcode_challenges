# -*- coding: utf-8 -*-
"""
Created on Nov 10 17:37:53 2023

@author: Jerome Yutai Shen

"""

from typing import Optional, List
from collections import deque
NULL_NODE = "#"


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        if not root:
            return [[""]]
        else:
            nodes = self.bfs(root)
            idx_col, matrix = self.bfs_indices(nodes)
            for irow, nodes_curr_layer in enumerate(nodes):
                for idx, node in zip(idx_col[irow], nodes_curr_layer):
                    if node != NULL_NODE:
                        matrix[irow][idx] = node
        return matrix

    def bfs0(self, root: Optional[TreeNode]) -> str:
        null_node = "#"
        queue = deque([root])
        _bfs = []
        while queue:
            node = queue.popleft()
            if node:
                _bfs.append(str(node.val))
            else:
                _bfs.append(NULL_NODE)

            if node:
                queue.append(node.left)
                queue.append(node.right)

        return "".join(_bfs)

    def bfs(self, root: Optional[TreeNode]) -> List[List[str]]:
        queue = deque([root])
        nodes_bfs = []
        while queue:
            numel = len(queue)
            curr_layer = []
            for idx in range(numel):
                node = queue.popleft()
                if node:
                    curr_layer.append(str(node.val))
                else:
                    curr_layer.append(NULL_NODE)

                if node:
                    queue.append(node.left)
                    queue.append(node.right)
            nodes_bfs.append(curr_layer)

        return nodes_bfs[:-1]

    def bfs_indices(self, nodes: List[List[str]]) -> [List[List[int]], List[List[int]]]:
        m, n = len(nodes), 2 ** len(nodes) - 1
        matrix = [[""] * n for _ in range(m)]  # [[""] * n] * m 会产生bug

        idx_col = []
        for irow in range(m):
            idx_this_layer = []
            if irow == 0:
                idx_this_layer.append(int((n - 1) / 2))
            else:
                idx_last_layer = idx_col[-1]
                nodes_last_layer = nodes[irow - 1]
                for idx, node in zip(idx_last_layer, nodes_last_layer):
                    if node != NULL_NODE:
                        #print(f"idx, {idx}, node, {node}, irow: {irow}")
                        idx_this_layer.append(int(idx - 2 ** (m - irow - 1)))
                        idx_this_layer.append(int(idx + 2 ** (m - irow - 1)))
            idx_col.append(idx_this_layer)

        return idx_col, matrix

    def bfs_indices2(self, nodes: List[List[str]]) -> [List[List[int]], List[List[int]]]:
        m, n = len(nodes), 2 ** len(nodes) - 1
        matrix = [[""] * n for _ in range(m)]  # [[""] * n] * m 会产生bug

        idx_col = [[int((n - 1) / 2)]]
        for irow in range(m - 1):
            idx_next_layer = []
            assert len(idx_col[-1]) == len(nodes[irow])
            #print(idx_col[-1], nodes[irow], irow)
            for idx, node in zip(idx_col[-1], nodes[irow]):
                if node == NULL_NODE:
                    continue
                idx_next_layer.append(int(idx - 2 ** (m - irow - 2))) # repalce irow with irow + 1, m - irow - 1 -> m - irow - 1 - 1
                idx_next_layer.append(int(idx + 2 ** (m - irow - 2)))
            idx_col.append(idx_next_layer)

        return idx_col, matrix


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left.left = TreeNode(8)
    root.right.right.left = TreeNode(9)

    """
                      1
                  /       \
                2          3
              /   \      /   \
             4     5    6     7
                       /     /
                      8     9

    """
    _ = Solution()
    __ = _.bfs(root)
    __1 = _.bfs_indices(__)
    __10 = _.bfs_indices2(__)
    assert __1[0] == __10[0]
    mat = _.printTree(root)
    print(list(zip(*mat)))

    # [3, null, 30, 10, null, null, 15, null, 45]
    root = TreeNode(3)
    root.right = TreeNode(30)
    root.right.left = TreeNode(10)
    root.right.left.right = TreeNode(15)
    root.right.left.right.right = TreeNode(45)

    """
                      3
                         \
                          30
                        /   
                      10     
                       \     
                        15   
                         \
                         45 

    """
    _ = Solution()
    __ = _.bfs(root)
    __1 = _.bfs_indices(__)
    __10 = _.bfs_indices2(__)
    assert __1[0] == __10[0]
    mat2 = _.printTree(root)
    print(list(zip(*mat2)))

    root = TreeNode(1)
    root.left = TreeNode(2)

    _ = Solution()
    __ = _.bfs(root)
    __1 = _.bfs_indices(__)
    __10 = _.bfs_indices2(__)
    assert __1[0] == __10[0]
    mat2 = _.printTree(root)
    print(list(zip(*mat2)))

    root = TreeNode()
    _ = Solution()
    __ = _.bfs(root)
    __1 = _.bfs_indices(__)
    __10 = _.bfs_indices(__)
    assert __1[0] == __10[0]
    mat2 = _.printTree(root)
    print(list(zip(*mat2)))