# -*- coding: utf-8 -*-
"""
Created on Jun 14 00:56:57 2022

@author: Jerome Yutai Shen

"""
from typing import Optional, List
from common_classes import BinaryTreeNode


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[BinaryTreeNode]:
        if not inorder: return None # inorder is empty
        root = BinaryTreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : 1 + root_idx], inorder[ : root_idx])
        root.right = self.buildTree(preorder[root_idx + 1 : ], inorder[root_idx + 1 : ])
        return root

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[BinaryTreeNode]:
        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = BinaryTreeNode(root_value)

            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)


if __name__ == "__main__":
    pass