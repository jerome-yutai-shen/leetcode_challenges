# -*- coding: utf-8 -*-
"""
Created on Nov 09 16:54:24 2023

@author: Jerome Yutai Shen

"""
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ O(n log k), O(k) """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0] # heapq.heappop(heap)


"""
算法：快速选择算法
最容易想到的就是直接排序，返回第k大的值。时间复杂度是O(nlogn)，这里提供O(n)的解法。

这题其实是快速排序算法的变体。
通过快速排序算法的partition步骤，可以将小于pivot的值划分到pivot左边，大于pivot的值划分到pivot右边，所以可以直接得到pivot的rank，从而缩小范围继续找第k大的值。

partition步骤：

令left = start，right = end，pivot = nums[left]。
当nums[left] < pivot时，left指针向右移动。
当nums[right] > pivot时，right指针向左移动。
交换两个位置的值，right指针左移，left指针右移。
直到两指针相遇，否则回到第2步。
每次partition后根据pivot的位置，寻找下一个搜索的范围。

复杂度分析
设数组长度为n

时间复杂度O(n)
对一个数组进行partition的时间复杂度为O(n)。
分治，选择一边继续进行partition。
所以总的复杂度为T(n) = T(n / 2) + O(n)，总时间复杂度依然为O(n)。
空间复杂度O(1)
只需要快速选择游标的O(1)额外空间。
"""


class SolutionQS:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, k, nums):
        n = len(nums)
        # 为了方便编写代码，这里将第 k 大转换成第 k 小问题。
        k = n - k
        return self.partition(nums, 0, n - 1, k)

    def partition(self, nums, start, end, k):
        left, right = start, end
        pivot = nums[left]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 如果第 k 小在右侧，搜索右边的范围，否则搜索左侧。
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)
        return nums[k]


class Solution2:
    def findKthLargest(self, nums, k):
        """ O(n) avg O(n ** 2) worst, O(n) """
        import random
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quick_select(left, k)

            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))

            return pivot

        return quick_select(nums, k)

