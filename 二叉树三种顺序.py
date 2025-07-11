# -*- coding: utf-8 -*-
"""
Created on Jul 04 21:52:57 2025

@author: Jerome Yutai Shen

"""



def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def preorder2(root):
    if not root:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:  # 右子节点先入栈，确保左边先处理
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def inorder2(root):
    stack = []
    res = []
    curr = root
    while curr or stack:
        while curr:             # 一路向左走到底
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)    # 访问中间节点
        curr = curr.right       # 转向右子树
    return res


def postorder2(root):
    if not root:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:           # 左右顺序反过来
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]            # 翻转结果变成 左 → 右 → 根