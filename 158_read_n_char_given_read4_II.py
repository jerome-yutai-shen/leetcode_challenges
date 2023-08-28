# -*- coding: utf-8 -*-
"""
Created on Jun 19 23:02:11 2023

@author: Jerome Yutai Shen

"""

class Solution:

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def __init__(self):
        self.buff = [None] * 4
        self.read_pos = self.write_pos = 0

    def read(self, buf, n):
        idx = 0
        while idx < n:
            if self.read_pos == 0:
                self.write_pos = read4(self.buff)
            while self.read_pos < self.write_pos and idx < n:
                buf[idx] = self.buff[self.read_pos]
                idx += 1
                self.read_pos += 1
            if self.read_pos == self.write_pos:
                self.read_pos = 0
            if idx == n or self.write_pos < 4:
                break
        return idx


class Solution1:
    def __init__(self):
        self.buf4, self.i4, self.n4 = [None] * 4, 0, 0

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        i = 0
        while i < n:
            if self.i4 == self.n4:
                self.i4, self.n4 = 0, read4(self.buf4)
                print(self.i4, self.n4)
                if not self.n4:
                    break
            buf[i], i, self.i4 = self.buf4[self.i4], i + 1, self.i4 + 1
        print(f"buf: {buf}")
        return i