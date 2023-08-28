# -*- coding: utf-8 -*-
"""
Created on Jun 26 03:52:48 2023

@author: Jerome Yutai Shen

"""
from typing import List
from collections import deque


class Solution:
    def isWinner3(self, player1: List[int], player2: List[int]) -> int:

        s1 = s2 = 0
        diff = s1 - s2
        had_ten1 = had_ten2 = int(False)
        char1, char2 = str(had_ten1), str(had_ten2)
        for s1, s2 in zip(player1, player2):
            char1 = char1 + str(int(s1 >= 10))
            char1 = char1[-3:]
            had_ten1 = int(char1, base = 2) >= 2
            s1 = (1 + int(had_ten1)) * s1

            char2 = char2 + str(int(s2 >= 10))
            char2 = char2[-3:]
            had_ten2 = int(char2, base=2) >= 2
            s2 = (1 + int(had_ten2)) * s2

            print(s1, had_ten1, s2, had_ten2)
            diff += (s1 - s2)

        return int(diff != 0) + int(diff < 0)

    def isWinner2(self, player1: List[int], player2: List[int]) -> int:

        s1 = s2 = 0
        diff = s1 - s2
        had_ten1 = had_ten2 = int(False)

        for s1, s2 in zip(player1, player2):
            had_ten1 = (had_ten1 << 1)
            had_ten1 += s1 >= 10
            if had_ten1 > 3:
                had_ten1_str = bin(had_ten1)[-3:]
            else:
                had_ten1_str = bin(had_ten1)[2:]

            s1 = (1 + int(int(had_ten1_str, base = 2) >= 2)) * s1

            had_ten2 = (had_ten2 << 1)
            had_ten2 += s2 >= 10
            if had_ten2 > 3:
                had_ten2_str = bin(had_ten2)[-3:]
            else:
                had_ten2_str = bin(had_ten2)[2:]

            s2 = (1 + int(int(had_ten2_str, base=2) >= 2)) * s2

            print(s1, had_ten1, s2, had_ten2)
            diff += (s1 - s2)

        return int(diff != 0) + int(diff < 0)

    def isWinner4(self, player1: List[int], player2: List[int]) -> int:

        diff = 0
        had_ten1 = deque([])
        had_ten2 = deque([])

        for s1, s2 in zip(player1, player2):
            diff += ((1 + int(True in had_ten1)) * s1 - (1 + int(True in had_ten2)) * s2)

            had_ten1.append(s1 >= 10)
            if len(had_ten1) > 2:
                had_ten1.popleft()

            had_ten2.append(s2 >= 10)
            if len(had_ten2) > 2:
                had_ten2.popleft()


        return int(diff != 0) + int(diff < 0)

    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        diff = 0
        prev1ten1 = prev2ten1 = prev1ten2 = prev2ten2 = False
        for s1, s2 in zip(player1, player2):
            diff += ((1 + int(prev1ten1 | prev2ten1)) * s1 - (1 + int(prev1ten2 | prev2ten2)) * s2)
            prev1ten1, prev2ten1, prev1ten2, prev2ten2 = s1 == 10,  prev1ten1, s2 == 10, prev1ten2

        return int(diff != 0) + int(diff < 0)



if __name__ == "__main__":
    solution = Solution()
    # print(solution.isWinner([4,10,7,9], [6,5,2,3]))
    # print(solution.isWinner([3,5,7,6], [8,10,10,2]))
    print(solution.isWinner([10, 1, 1, 1], [1, 1, 10, 1]))
    #

    # x0 = False
    # _char = str(int(x0))
    # # # whether_ten = [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1]
    # # # for num in whether_ten:
    # # #     x0 = x0 << 1
    # # #     x0 += num
    # # #     print(bin(x0))
    # # #     x0 = x0 & 4
    # # #
    # # #     print(num, x0, x0 >= 2)
    # tens = [10, 1, 1, 1, 1, 1, 10, 1, 10, 10, 1, 1, 10]
    # for x in tens:
    #     _char = _char + str(int(x >= 10))
    #     _char = _char[-3:]
    #     print(x, _char, int(_char, base = 2))
    #
    #
    # for x in tens:
    #     x0 = x0 << 1
    #     x0 += int(x >= 10)
    #     # x0 = x0 & 8
    #     print(x0, bin(x0), bin(x0 & 8))
    # print(check([10, 1, 1, 1], False), check([1, 1, 1, 10], False))
