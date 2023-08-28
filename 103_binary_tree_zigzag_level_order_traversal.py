# -*- coding: utf-8 -*-
"""
Created on Jun 13 12:40:57 2022

@author: Jerome Yutai Shen

"""
from typing import Optional, List, Deque
from common_classes import BinaryTreeNode
from collections import deque


class Solution:

    def zigzagLevelOrder(self, root: Optional[BinaryTreeNode]) -> List:
        nodes_bfs = []
        if not root:
            return nodes_bfs
        nodes_q = deque([root])
        idx_level = 0
        while nodes_q:
            len_q = len(nodes_q)
            nodes_current_level = deque([])
            is_reversed = idx_level % 2
            for _ in range(len_q):
                node = nodes_q.popleft()
                if node.left:
                    nodes_q.append(node.left)
                if node.right:
                    nodes_q.append(node.right)

                if is_reversed:
                    nodes_current_level.appendleft(node.val)
                else:
                    nodes_current_level.append(node.val)
            idx_level += 1
            nodes_bfs.append(nodes_current_level)
        return nodes_bfs

    def zigzag_level_order_dfs(self, root: Optional[BinaryTreeNode]) -> List:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = []
        if root is None:
            return results

        # normal level order traversal with DFS
        dfs(root, 0, results)

        return results


def dfs(node: Optional[BinaryTreeNode], level: int, results: List[Deque]):
    if level >= len(results):
        results.append(deque([node.val]))
    else:
        if level % 2 == 0:
            results[level].append(node.val)
        else:
            results[level].appendleft(node.val)

    for next_node in [node.left, node.right]:
        if next_node is not None:
            dfs(next_node, level + 1, results)

"""
[3,9,20,null,null,15,7]

begin level 0 3 [] 0
begin level 1 9 [deque([3])] 1
end level 1 9 [deque([3]), deque([9])] 2
begin level 1 20 [deque([3]), deque([9])] 2
begin level 2 15 [deque([3]), deque([20, 9])] 2
end level 2 15 [deque([3]), deque([20, 9]), deque([15])] 3
begin level 2 7 [deque([3]), deque([20, 9]), deque([15])] 3
end level 2 7 [deque([3]), deque([20, 9]), deque([15, 7])] 3
end level 1 20 [deque([3]), deque([20, 9]), deque([15, 7])] 3
end level 0 3 [deque([3]), deque([20, 9]), deque([15, 7])] 3

"""

if __name__ == "__main__":
    root = BinaryTreeNode(3)
    root.left = BinaryTreeNode(9)
    root.right = BinaryTreeNode(20)
    root.right.left = BinaryTreeNode(15)
    root.right.right = BinaryTreeNode(7)
    sol = Solution()
    sol.zigzag_level_order_dfs(root)


