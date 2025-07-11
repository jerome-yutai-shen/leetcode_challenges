# -*- coding: utf-8 -*-
"""
Created on Jul 02 10:16:27 2025

@author: Jerome Yutai Shen

"""
from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        set_ = SortedList()
        for i in range(len(nums)):
            # Find the successor of current element
            idx = set_.bisect_left(nums[i])
            if idx != len(set_) and set_[idx] <= nums[i] + t:
                return True

            # Find the predecessor of current element
            if idx > 0 and nums[i] <= set_[idx - 1] + t:
                return True

            set_.add(nums[i])
            if len(set_) > k:
                set_.remove(nums[i - k])

        return False

    def containsNearbyAlmostDuplicate_bucket_sort(self, nums, indexDiff, valueDiff):
        """bucket sort"""
        if valueDiff < 0 or indexDiff < 0:
            return False

        def getID(x, w):
            return (
                x // w
            )  # Floor division to handle both positive and negative integers correctly


        bucket = {}
        w = valueDiff + 1

        for i, num in enumerate(nums):
            bucket_id = getID(num, w)
            print(num, bucket_id)
            if bucket_id in bucket:
                return True
            if (bucket_id - 1 in bucket and abs(num - bucket[bucket_id - 1]) <= valueDiff):
                return True
            if (bucket_id + 1 in bucket and abs(num - bucket[bucket_id + 1]) <= valueDiff):
                return True

            bucket[bucket_id] = num

            if i >= indexDiff:
                old = nums[i - indexDiff]
                old_id = getID(old, w)
                del bucket[old_id]

        return False


class Solution:
    # Get the ID of the bucket from element value x and bucket width w
    # Division '/' in Python with '//' performs floor division, which is necessary for correct bucketing.
    def getID(self, x, w):
        return (
            x // w
        )  # Floor division to handle both positive and negative integers correctly

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0:
            return False
        buckets = {}
        w = t + 1  # Increment by 1 to handle the range correctly
        for i in range(len(nums)):
            bucket = self.getID(nums[i], w)
            # Check if current bucket is empty, each bucket may contain at most one element
            if bucket in buckets:
                return True
            # Check the neighbor buckets for almost duplicates
            if bucket - 1 in buckets and abs(nums[i] - buckets[bucket - 1]) < w:
                return True
            if bucket + 1 in buckets and abs(nums[i] - buckets[bucket + 1]) < w:
                return True
            # Now bucket is empty and no almost duplicates in neighbor buckets
            buckets[bucket] = nums[i]
            if i >= k:
                del buckets[self.getID(nums[i - k], w)]
        return False