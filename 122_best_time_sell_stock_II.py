# -*- coding: utf-8 -*-
"""
Created on Jun 07 01:38:38 2022

@author: Jerome Yutai Shen

"""
from typing import List


def max_profit(prices: List[int]) -> int:
    """
    simple one pass
    :param prices:
    :return:
    """

    maxprofit = 0
    for idx in range(1, len(prices)):
        if (prices[idx] > prices[idx - 1]):
            maxprofit += prices[idx] - prices[idx - 1]

    return maxprofit


def max_profit_peak_valley(prices: List[int]) -> int:
    """
    Peak Valley Approach
    :param prices:
    :return:
    """

    idx = 0
    valley = prices[0]
    peak = prices[0]
    maxprofit = 0

    while idx < len(prices):

        while idx < len(prices) - 1 and  prices[idx] >= prices[idx + 1]:
            idx += 1
            valley = prices[idx]

        while idx < len(prices) - 1 and prices[idx] <= prices[idx + 1]:
            idx += 1
            peak = prices[idx]

        maxprofit += peak - valley

    return maxprofit