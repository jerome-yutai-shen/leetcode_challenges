# -*- coding: utf-8 -*-
"""
Created on Jul 05 22:23:38 2025

@author: Jerome Yutai Shen

必须用后序遍历
必须先检查子树，才能判断根节点是否成立。

"""
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return True  # 空节点视为 univalue

            left_uni = dfs(node.left)
            right_uni = dfs(node.right)

            # 任意一边不是 univalue，当前也不是
            if not left_uni or not right_uni:
                return False

            # 左节点存在且值不等于当前节点
            if node.left and node.left.val != node.val:
                return False

            # 右节点存在且值不等于当前节点
            if node.right and node.right.val != node.val:
                return False

            # 当前节点是 univalue subtree
            self.count += 1
            return True

        dfs(root)
        return self.count