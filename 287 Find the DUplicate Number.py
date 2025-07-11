# -*- coding: utf-8 -*-
"""
Created on Jul 09 17:25:06 2025

@author: Jerome Yutai Shen

类似于142 不能排序后差分 也不能用set保存访问过的元素
用快慢指针检测环
但是不能真的构造链表 那样就是额外空间
不应该真的 new 链表节点，而应该用数组模拟跳转：next(i) = nums[i]

首先找相遇的点
在相遇之后：
	•	快指针（fast）留在原地，也就是留在环中相遇的那个点；
	•	慢指针（slow）重置到起点 nums[0]；
	•	然后两个指针以每次一步的速度同时前进，直到再次相遇。

这次相遇的位置，就是 环的入口（即题目要求的 重复数字）。

相遇时 慢指针走了x+y。其中起点距离入口x，入口距离相遇点y，假设环的周长是C，那么慢指针退回起点，快指针留在原地，两者速度都设成一样，快指针走完C-y 恰好是慢指针走的x，C-y就等于x。
还可以反过来解释，因为有速度差，那么相对速度，假设慢指针不动，快指针就是以慢指针的速度单独运动，那么肯定是转一圈回到入口。入口就是旋转的相遇点，也就是说慢指针在相遇时走过的路程一定是环的周长。

"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: detect cycle
        slow = nums[0]
        fast = nums[0]
        # 找相遇点（证明有环）：
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # 隐式链表模型 中，nums[i] 相当于“指向下一个节点”，fast多走一步
            if slow == fast:
                break

        # Phase 2: find entry

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow