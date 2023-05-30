# -*- coding: utf-8 -*-
"""
PyCharm for binary_search.py

Created on Nov 13 15:24:36 2021

@author: Jerome Yutai Shen Y893565

"""

from typing import List, Union, Tuple


class Solution:

    def __init__(self, vals: Union[Tuple[int], List[int]], target: int):
        self.vals = vals
        self.target = target

    def hashmap(self) -> List[int]:
        """
        :return:
        """
        valpair_indices = [-1, -1]

        hash = { }
        for idx, val in enumerate(self.vals):
            if self.target - val in hash:
                valpair_indices = [hash[self.target - val], idx]
            hash[val] = idx
        return valpair_indices

    @classmethod
    def clsm_hashmap(cls, vals: Union[Tuple[int], List[int]], target: int) -> List[int]:
        """
        :param vals:
        :param target:
        :return: index0, index1, and vals[index0] + vals[index1] == target
        """
        valpair_indices = [-1, -1]

        hash = { }
        for idx, val in enumerate(vals):
            """
            vals = [2,4,5]; target = 8
            """

            if target - val in hash:
                valpair_indices = [hash[target - val], idx]
            hash[val] = idx
        return valpair_indices

    @classmethod
    def clsm_hashset(cls, vals: Union[Tuple[int], List[int]], target: int) -> List[int]:
        """
        :param vals:
        :param target:
        :return: number0, number1, not index0, index1
        """
        val_pair = [None, None]

        hash = set()
        for val in vals:
            if target - val in hash:
                val_pair = [target - val, val]
            hash.add(val)
        return val_pair

    @classmethod
    def clsm_two_pntr(cls, vals: Union[Tuple[int], List[int]], target: int) -> List[int]:
        """
        :param vals:
        :param target:
        :return:
        """
        valpair_indices = [-1, -1]

        if vals:
            val_idx_pair = [(val, idx) for idx, val in enumerate(vals)]
            val_idx_pair.sort()

            pntr_left, pntr_right = 0, len(vals) - 1
            while pntr_left < pntr_right:
                if val_idx_pair[pntr_left][0] + val_idx_pair[pntr_right][0] > target:
                    pntr_right -= 1
                elif val_idx_pair[pntr_left][0] + val_idx_pair[pntr_right][0] < target:
                    pntr_left += 1
                else:
                    return sorted([val_idx_pair[pntr_left][1], val_idx_pair[pntr_right][1]])

        return valpair_indices

    def twoSum_2pntr(self, vals: Union[Tuple[int], List[int]], target: int) -> List[int]:
        """
        :param vals:
        :param target:
        :return:
        """
        valpair_indices = [-1, -1]

        if not vals:
            return valpair_indices
        
        val_idx_pair = [(val, idx) for idx, val in enumerate(vals)]
        val_idx_pair.sort()

        pntr_left, pntr_right = 0, len(vals) - 1
        while pntr_left < pntr_right:
            if val_idx_pair[pntr_left][0] + val_idx_pair[pntr_right][0] > target:
                pntr_right -= 1
            elif val_idx_pair[pntr_left][0] + val_idx_pair[pntr_right][0] < target:
                pntr_left += 1
            else:
                return sorted([val_idx_pair[pntr_left][1], val_idx_pair[pntr_right][1]])

        return valpair_indices
        

class TwoSumTwoShiftingPinters:
    """
    @param number: An integer
    @return: nothing
    """

    def __init__(self):
        self.nums = []

    def add(self, number):
        self.nums.append(number)
        index = len(self.nums) - 1

        while index > 0 and self.nums[index - 1] > self.nums[index]:
            self.nums[index - 1], self.nums[index] = \
                self.nums[index], self.nums[index - 1]
            index -= 1

    def find(self, targetValue):
        """
        Two pointers,
        :param targetValue:
        :return:
        """
        left, right = 0, len(self.nums) - 1
        while left < right:
            two_sum = self.nums[left] + self.nums[right]
            if two_sum < targetValue:
                left += 1
            elif two_sum > targetValue:
                right -= 1
            else:
                return True

        return False


class TwoSumDict:
    """
    @param number: An integer
    @return: nothing
    """

    def __init__(self):
        self.num_counts_map = {}

    def add(self, number):
        self.num_counts_map[number] = self.num_counts_map.get(number, 0) + 1

    def find(self, targetValue):
        """
         Find if there exists any pair of numbers which sum is equal to the value.
        :param targetValue:
        :return:
        """
        for num1 in self.num_counts_map:
            num2 = targetValue - num1
            num2_count_threshold = 2 if num1 == num2 else 1
            if self.num_counts_map.get(num2, 0) >= num2_count_threshold:
                return True
        return False


class TwoSumUniquePairs:

    def twoSum6(self, nums, target):
        """
        target = addend1 + addend2
        :param nums:
        :param target:
        :return:
        """
        unique_addend1s = set()
        unique_addends_pairs = set()

        for val in nums:
            addend2 = target - val
            if addend2 in unique_addend1s:
                addens_pair_in_nums = tuple(sorted([val, addend2])) # Necessary to sort?
                addens_pair_in_nums = tuple([val, addend2])  # Necessary to sort?
                unique_addends_pairs.add(addens_pair_in_nums)
            else:
                unique_addend1s.add(val)

        print(f"nums: {nums}, target: {target}")
        print(f"unique_addends_pairs: {unique_addends_pairs}, unique_addend1s: {unique_addend1s}")
        return len(unique_addends_pairs)

    def twoSum6_2(self, nums, target):
        """
        lintcode 会写代码的卡比兽
        :param nums:
        :param target:
        :return:
        """
        unique_value = set()
        unique_num_pairs = set()

        for val in nums:
            supplementary_num = target - val
            if supplementary_num not in unique_value:
                unique_value.add(val)
            else:
                num_pair = tuple(sorted([val, supplementary_num]))
                unique_num_pairs.add(num_pair)

        print(f"unique_num_pairs: {unique_num_pairs}, unique_nums: {unique_value}")
        return len(unique_num_pairs)

    def twoSum6_Wrong(self, nums, target):
        unique_num_pairs = set()

        for val in nums:
            pairing_num = target - val
            num_pair = tuple(sorted([val, pairing_num]))

            if pairing_num not in nums:
                continue

            if pairing_num not in unique_num_pairs:
                unique_num_pairs.add(num_pair)

        print(unique_num_pairs)

        return len(unique_num_pairs)

    def twoSum6_twopointers(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums)- 1
        count = set()

        while left < right:
            if nums[left] + nums[right] == target:
                count.add( (nums[left], nums[right]) )
                left += 1
                right -= 1
            elif nums[left] + nums[right] > target:
                right -=1
            elif nums[left] + nums[right] < target:
                left += 1
        return len(count)

    def twoSum6_set(self, nums, target):
        # write your code here
        if not nums:
            return 0
        result = set()
        hashSet = set()
        for i in nums:
            if target - i in hashSet:
                result.add((i, target - i))
            else:
                hashSet.add(i)
        print(hashSet)
        print(result)
        return len(result)


if __name__ == "__main__":
    # vals = [2,7,11,15]
    # target = 17
    # # solution = Solution(vals, target)
    # # print(solution.hashmap())
    # print(Solution.clsm_two_pntr(vals, target))
    # vals = [2, 7, 11, 15][::-1]
    # target = 18
    # print(Solution.clsm_hashmap(vals, target))

    # two_sum = TwoSumDict()
    # vals = [-12, 25, -20, 22, 12, -39, 11, -15]
    # for val in vals:
    #     two_sum.add(val)
    #
    # print(two_sum.find(-20))
    # print(two_sum.find(20))

    xx = TwoSumUniquePairs()
    # print(xx.twoSum6_set([1, 1, 2, 45, 46, 46], 47))
    print(xx.twoSum6([11, 11, 22, 22, 0, 0,4,4,4,4,4], 8))
    print(xx.twoSum6([11,], 22))
    print(xx.twoSum6([11, 11, 2, 20, 22, 0, 20, 2, 20, 2, 1, 21, 21, 1, 0, -1, 20], 22))