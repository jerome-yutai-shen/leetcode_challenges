# -*- coding: utf-8 -*-
"""
Created on Jul 04 22:36:06 2025

@author: Jerome Yutai Shen

"""


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = None

        def inorder(node):
            if not node or self.res is not None:
                return
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.res