# -*- coding: utf-8 -*-
"""
Created on Apr 17 17:10:09 2023

@author: Jerome Yutai Shen

"""

from string import ascii_lowercase


class RremoveDuplicates:

    def solution1(self, S: str) -> str:
        output = []
        for ch in S:
            if output and ch == output[-1]:
                output.pop()
            else:
                output.append(ch)
        return ''.join(output)

    def solution2(self, S: str) -> str:
        # generate 26 possible duplicates
        duplicates = {2 * ch for ch in ascii_lowercase}

        prev_length = -1
        while prev_length != len(S):
            prev_length = len(S)
            for d in duplicates:
                S = S.replace(d, '')

        return S


if __name__ == "__main__":
    rm_dup = RremoveDuplicates()
    print(rm_dup.solution1("abbaca"))
    print(rm_dup.solution2("abbaca"))
