# -*- coding: utf-8 -*-
"""
Created on Jun 07 00:18:28 2022

@author: Jerome Yutai Shen

"""


class LongestValidParentheses:

    @classmethod
    def with_stack(cls, s: str) -> int:
        """
        栈
        :param s:
        :return:
        """
        stack = [-1]
        length = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    max_length = max(max_length, length)
        return max_length

    @classmethod
    def by_dp(cls, s: str) -> int:
        n = len(s)
        if not s:
            return n
        dp = [0]*n
        for i in range(1, len(s)):
            # i-dp[i-1]-1是与当前)对称的位置
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if (i - dp[i - 1]) >= 2 else 0) + 2
        return max(dp)

    @classmethod
    def with_no_extra_space(cls, s: str) -> int:
        n, left, right, maxlength = len(s), 0, 0, 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif right > left:
                left = right = 0
        left = right = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * left)
            elif right < left:
                left = right = 0

        return maxlength