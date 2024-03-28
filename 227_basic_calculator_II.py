# -*- coding: utf-8 -*-
"""
Created on Nov 11 12:45:37 2023

@author: Jerome Yutai Shen

"""
class Solution:
    def calculate(self, s: str) -> int:
        # 这个表达式字符串只包含 非负 整数
        if not s:
            return 0

        n = len(s)
        stack = []
        preSign = '+'
        num = 0
        for idx, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + ord(char) - ord('0') # int(str(num) + char)
            if idx == n - 1 or char in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num)) # -3/4 => 1 -3//4 等于 -1 所以要用int(-3/4), 用stack解决
                preSign = char
                num = 0
        return sum(stack)


if __name__ == "__main__":
    s = "3+2*2"
    _ = Solution()
    _.calculate(s)