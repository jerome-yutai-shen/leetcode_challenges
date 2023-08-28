# -*- coding: utf-8 -*-
"""
Created on May 21 14:38:01 2022

@author: Jerome Yutai Shen

"""


def convert(s: str, numRows: int) -> str:
    import operator
    from functools import reduce
    if numRows == 1 or numRows >= len(s):
        return s

    zigzag = [[] for x in range(numRows)]
    row, step = 0, 1
    for c in s:
        zigzag[row] += c,
        if row == 0:
            step = 1
        elif row == numRows - 1:
            step = -1
        row += step
    return ''.join(reduce(operator.add, zigzag))


def convert1(src_str: str, numRows) -> str:
    if numRows == 1 or numRows >= len(src_str):
        return src_str

    final = [[] for _ in range(numRows)]
    print(f"numRows, len(s): {numRows, len(src_str)}")
    for idx in range(len(src_str)):
        print(f"{idx, idx2rowidx(idx, numRows)}")
        final[idx2rowidx(idx, numRows)].extend(src_str[idx])

    return "".join(["".join(final[i]) for i in range(numRows)])


def idx2rowidx(idx, num_rows):
    distance = num_rows - 1
    return distance - abs(distance - idx % (2 * distance))


if __name__ == "__main__":
    print(convert1("PAYPALISHIRING", 3))