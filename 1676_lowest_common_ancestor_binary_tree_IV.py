# -*- coding: utf-8 -*-
"""
Created on Sep 27 00:31:56 2023

@author: Jerome Yutai Shen

"""
"""
236:

TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
 return find(root, p.val, q.val);
}

// 在二叉树中寻找 val1 和 val2 的最近公共祖先节点
TreeNode find(TreeNode root, int val1, int val2) {
 if (root == null) {
 return null;
    }
 // 前序位置
 if (root.val == val1 || root.val == val2) {
 // 如果遇到目标值，直接返回
 return root;
    }
    TreeNode left = find(root.left, val1, val2);
    TreeNode right = find(root.right, val1, val2);
 // 后序位置，已经知道左右子树是否存在目标值
 if (left != null && right != null) {
 // 当前节点是 LCA 节点
 return root;
    }

 return left != null ? left : right;
}

1676:

TreeNode lowestCommonAncestor(TreeNode root, TreeNode[] nodes) {
 // 将列表转化成哈希集合，便于判断元素是否存在
    HashSet<Integer> values = new HashSet<>();
 for (TreeNode node : nodes) {
        values.add(node.val);
    }

 return find(root, values);
}

// 在二叉树中寻找 values 的最近公共祖先节点
TreeNode find(TreeNode root, HashSet<Integer> values) {
 if (root == null) {
 return null;
    }
 // 前序位置
 if (values.contains(root.val)){
 return root;
    }

    TreeNode left = find(root.left, values);
    TreeNode right = find(root.right, values);
 // 后序位置，已经知道左右子树是否存在目标值
 if (left != null && right != null) {
 // 当前节点是 LCA 节点
 return root;
    }

 return left != null ? left : right;
}
"""
from typing import Optional, List, Set

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """

    # Stack for tree traversal
    stack = [root]

    # Dictionary for parent pointers
    parent = { root: None }

    # Iterate until we find both the nodes p and q
    while p not in parent or q not in parent:

        node = stack.pop()

        # While traversing the tree, keep saving the parent pointers.
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    # Ancestors set() for node p.
    ancestors = set()

    # Process all ancestors for node p using parent pointers.
    while p:
        ancestors.add(p)
        p = parent[p]

    # The first ancestor of q which appears in
    # p's ancestor set() is their lowest common ancestor.
    while q not in ancestors:
        q = parent[q]
    return q


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    return find236(root, p.val, q.val)


def find236(root: 'TreeNode', p_val: int, q_val: int) -> Optional[TreeNode]:
    if not root:
        return None
    # 前序位置
    if root.val == p_val or root.val == q_val: # 如果遇到目标值，直接返回
        return root

    left_node = find236(root.left, p_val, q_val)
    right_node = find236(root.right, p_val, q_val) # 后序位置，已经知道左右子树是否存在目标值
    if left_node and right_node: #  当前节点是 LCA 节点
        return root

    return left_node if left_node else right_node


def lowestCommonAncestor1676(root: 'TreeNode', nodes: List[TreeNode]) -> 'TreeNode':
    values = set()
    for node in nodes:
        values.add(node.val)
    return find1676(root, values)


def find1676(root: 'TreeNode', values: Set[int]) -> Optional[TreeNode]:
    """
    在二叉树中寻找 values 的最近公共祖先节点
    """
    if not root:
        return None
    # 前序位置
    if root.val in values:
        return root

    left_node = find1676(root.left, values)
    right_node = find1676(root.right, values)  # 后序位置，已经知道左右子树是否存在目标值
    if left_node and right_node: # 当前节点是 LCA 节点
        return root

    return left_node if left_node else right_node

