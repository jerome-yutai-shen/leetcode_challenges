# -*- coding: utf-8 -*-
"""
Created on Jun 11 19:41:59 2022

@author: Jerome Yutai Shen

lintcode 468, 1360,

class Solution {
    public boolean isSymmetric(TreeNode root) {
        return isMirror(root, root);
    }

    public boolean isMirror(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return true;
        if (t1 == null || t2 == null) return false;
        return (t1.val == t2.val)
            && isMirror(t1.right, t2.left)
            && isMirror(t1.left, t2.right);
    }
}


public boolean isSymmetric(TreeNode root) {
    Queue<TreeNode> q = new LinkedList<>();
    q.add(root);
    q.add(root);
    while (!q.isEmpty()) {
        TreeNode t1 = q.poll();
        TreeNode t2 = q.poll();
        if (t1 == null && t2 == null) continue;
        if (t1 == null || t2 == null) return false;
        if (t1.val != t2.val) return false;
        q.add(t1.left);
        q.add(t2.right);
        q.add(t1.right);
        q.add(t2.left);
    }
    return true;
}


"""
from common_classes import BinaryTreeNode
from typing import Optional


def is_symmetric_reccursive(root: Optional[BinaryTreeNode]) -> bool:
    return is_mirror_reccursive(root, root)


def is_mirror_reccursive(tree_node1: Optional[BinaryTreeNode], tree_node2: Optional[BinaryTreeNode]) -> bool:

    if tree_node1 is None and tree_node2 is None:
        return True
    if tree_node1 is None or tree_node2 is None:
        return False

    return tree_node1.val == tree_node2.val \
           and is_mirror_reccursive(tree_node1.right, tree_node2.left) \
           and is_mirror_reccursive(tree_node1.left, tree_node2.right)


def is_symmetric_bfs(root: Optional[BinaryTreeNode]) -> bool:
    from collections import deque
    tree_node_q = deque([root, root])
    while tree_node_q:
        tree_node1 = tree_node_q.pop()
        tree_node2 = tree_node_q.pop()
        if tree_node1 is None and tree_node2 is None:
            continue
        if tree_node1 is None or tree_node2 is None:
            return False
        if tree_node1.val != tree_node2.val:
            return False

        tree_node_q.append(tree_node1.left)
        tree_node_q.append(tree_node2.right)

        tree_node_q.append(tree_node1.right)
        tree_node_q.append(tree_node2.left)

    return True