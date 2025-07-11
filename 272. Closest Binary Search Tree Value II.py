# -*- coding: utf-8 -*-
"""
Created on Jul 05 19:11:42 2025

@author: Jerome Yutai Shen


中序遍历+双指针

O(n + k) O(n)


"""
import bisect


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # Step 1: 中序遍历，得到升序数组
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        nums = inorder(root)

        # Step 2: 找到 target 插入点（第一个 >= target 的位置）
        idx = bisect.bisect_left(nums, target)
        left, right = idx - 1, idx  # 初始化两个指针

        # Step 3: 双指针扩展，取 k 个最接近 target 的值
        res = []
        while k > 0:
            # 左边越界，只能取右边
            if left < 0:
                res.append(nums[right])
                right += 1
            # 右边越界，只能取左边
            elif right >= len(nums):
                res.append(nums[left])
                left -= 1
            else:
                # 距离比较 + tie-break: 距离相等时取较小的值
                if abs(nums[left] - target) <= abs(nums[right] - target):
                    res.append(nums[left])
                    left -= 1
                else:
                    res.append(nums[right])
                    right += 1
            k -= 1

        return res