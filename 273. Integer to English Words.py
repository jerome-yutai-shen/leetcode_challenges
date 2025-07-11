# -*- coding: utf-8 -*-
"""
Created on Jul 05 19:56:22 2025

@author: Jerome Yutai Shen

"""


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # 1~19 的特殊读法
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six",
                    "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                    "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                    "Eighteen", "Nineteen"]

        # 整十位读法
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]

        # 单位：每三位一级
        thousands = ["", "Thousand", "Million", "Billion"]

        # 把三位以内的数变成英文
        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        i = 0  # thousand 单位索引
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + thousands[i] + " " + res
            num = num // 1000
            i += 1

        return res.strip()