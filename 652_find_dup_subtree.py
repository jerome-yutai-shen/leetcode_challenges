# -*- coding: utf-8 -*-
"""
Created on Jun 20 13:57:22 2023

@author: Jerome Yutai Shen

"""
from typing import List
from common_classes import BinaryTreeNode
from collections import defaultdict


class Solution:

    def findDuplicateSubtress(self, root: BinaryTreeNode) -> List[BinaryTreeNode]:

        def dfs(root: BinaryTreeNode):
            if not root:
                return None

            res = (root.val, dfs(root.left), dfs(root.right))
            d[res].append(root)
            return res

        d = defaultdict(list)
        dfs(root)

        return [d.get(k)[0] for k in d if len(d.get(k)) > 1]

    def findDuplicateSubtrees2(self, root: BinaryTreeNode) -> List[BinaryTreeNode]:

        def traverse(node):
            if not node:
                return 0

            triplet = (traverse(node.left), node.val, traverse(node.right))
            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1

            id = triplet_to_id[triplet]
            cnt[id] += 1
            if cnt[id] == 2:
                res.append(node)
            return id

        triplet_to_id = dict()
        cnt = defaultdict(int)
        res = []
        traverse(root)
        return res