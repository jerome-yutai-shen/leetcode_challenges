# -*- coding: utf-8 -*-
"""
Created on Jun 14 01:18:20 2022

@author: Jerome Yutai Shen

"""
from typing import Optional, List
from common_classes import BinaryTreeNode


class Solution:
    """
    @param postorder : A list of integers that postorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[BinaryTreeNode]:
        if not inorder: return None # inorder is empty
        root = BinaryTreeNode(postorder[-1])
        root_idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[ : root_idx], postorder[ : root_idx])
        root.right = self.buildTree(inorder[root_idx + 1 : ], postorder[root_idx : -1])
        return root

    def buildTree2(self, inorder: List[int], postorder: List[int]) -> Optional[BinaryTreeNode]:
        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None

            # pick up the last element as a root
            val = postorder.pop()
            root = BinaryTreeNode(val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[val]

            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)
            return root

        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)

if __name__ == "__main__":
    pass