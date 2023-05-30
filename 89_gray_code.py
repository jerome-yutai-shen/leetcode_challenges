# -*- coding: utf-8 -*-
"""
Created on Jun 08 11:07:05 2022

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:

        # write your code here
        ans = [0]
        for i in range(0, n):
            offset = 1 << i
            for j in reversed(range(len(ans))):
                ans.append(offset + ans[j])

        return ans