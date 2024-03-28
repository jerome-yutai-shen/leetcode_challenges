# -*- coding: utf-8 -*-
"""
Created on Sep 11 15:01:47 2023

@author: Jerome Yutai Shen

"""
import scipy
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for _ in range(0, rowIndex + 1):
            ans.append(scipy.special.comb(rowIndex, _, exact=True))

        return ans
    def getRowDP(self, rowIndex: int) -> List[int]:
        ans = [0] * (rowIndex + 1)
        ans[0] = 1
        for idx in range(rowIndex + 1):

            for idx2 in range(idx, 0, -1):
                ans[idx2] = ans[idx2] + ans[idx2 - 1]
            # while idx2 > 0:
            #     print(idx2, idx2 - 1, ans[idx2], ans[idx2 - 1], ans)
            #     ans[idx2] = ans[idx2] + ans[idx2 - 1]
            #     idx2 -= 1
            #     print(ans)
        # ans.append(1)
        return ans
"""
java DP

class Solution {
  public List<Integer> getRow(int rowIndex) {
    List<Integer> row =
        new ArrayList<>(rowIndex + 1) {
          {
            add(1);
          }
        };

    for (int i = 0; i < rowIndex; i++) {
      for (int j = i; j > 0; j--) {
        row.set(j, row.get(j) + row.get(j - 1));
      }
      row.add(1);
    }

    return row;
  }
}

"""


if __name__ == "__main__":
    solution = Solution()
    for _ in [3, 5, 10]:
        print(_, solution.getRowDP(_))
