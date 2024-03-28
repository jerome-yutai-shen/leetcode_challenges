# -*- coding: utf-8 -*-
"""
Created on Oct 16 05:18:25 2023

@author: Jerome Yutai Shen

"""


class LargerNumKey(str):
    def __lt__(x, y):
        # print(f"x{x}y{y}")
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


if __name__ == "__main__":
    _ = Solution()
    nums = [10, 2]
    print(_.largestNumber(nums))
    nums = [3, 30, 34, 5, 9]
    print(_.largestNumber(nums))