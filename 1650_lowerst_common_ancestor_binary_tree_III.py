# -*- coding: utf-8 -*-
"""
Created on Sep 27 00:23:39 2023

@author: Jerome Yutai Shen

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None



"""
https://cloud.tencent.com/developer/article/1969857
一文秒杀 5 道最近公共祖先问题


Node
lowestCommonAncestor(Node
p, Node
q) {
   // 
Node
a = p, b = q;
while (a != b) {
// a 走一步，如果走到根节点，转到 q 节点
if (a == null) a = q;
else a = a.parent;
// b 走一步，如果走到根节点，转到 p 节点
if (b == null) b = p;
else b = b.parent;
}
return a;
}
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        给你输入一棵存在于二叉树中的两个节点p和q，请你返回它们的最近公共祖先，函数签名如下：
        Node lowestCommonAncestor(Node p, Node q);
        由于节点中包含父节点的指针，所以二叉树的根节点就没必要输入了。
        这道题其实不是公共祖先的问题，而是单链表相交的问题，你把parent指针想象成单链表的next指针，题目就变成了：
        给你输入两个单链表的头结点p和q，这两个单链表必然会相交，请你返回相交点。
        """
        pntr1, pntr2 = p, q # 施展链表双指针技巧
        while pntr1 != pntr2:
            if pntr1: # pntr1 走一步，如果走到根节点，就跳转到 q 节点， 即pntr2起始位置
                pntr1 = pntr1.parent
            else:
                pntr1 = q

            if pntr2: # pntr2 走一步，如果走到根节点，就跳转到 p 节点， 即pntr1起始位置
                pntr2 = pntr2.parent
            else:
                pntr2 = p
        # 此时两个指针重合
        assert pntr1 == pntr2
        return pntr1