# -*- coding: utf-8 -*-
"""
Created on May 22 13:28:06 2022

@author: Jerome Yutai Shen

"""


def is_match(text: str, pattern: str):
    """
    text = "aa", p = "a"
    text = "aa", p = "a*"
    text = "ab", p = ".*"
    """
    print(f"text: {text} pattern: {pattern}")
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        next_text = first_match and is_match(text[1:], pattern)
        print(f"next_text {next_text}")
        pattern_from3 = is_match(text, pattern[2:])
        print(f"pattern_from3 {pattern_from3}")
        return next_text or pattern_from3
    else:
        return first_match and is_match(text[1:], pattern[1:])


def is_match_dp_backward(text: str, pattern: str):
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
    dp[-1][-1] = True

    for i in range(len(text), -1, -1):
        for j in range(len(pattern) - 1, -1, -1):
            # print(i, j)
            predecessor_match = i < len(text) and pattern[j] in {text[i], '.'}

            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                print(i, j, pattern[j + 1])
                dp[i][j] = dp[i][j + 2] or predecessor_match and dp[i + 1][j]
            else:
                dp[i][j] = predecessor_match and dp[i + 1][j + 1]

    print(dp[0][0])
    return dp


def is_match_dp_forward(text: str, pattern: str):
    """
    错误，
    text, pattern = "aab", "c*a*b" 应该是True
    """

    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
    dp[0][0] = True

    for idx in range(1, len(dp)):
        if idx <= len(pattern) and pattern[idx - 1] == '*':
            dp[0][idx] = dp[0][idx - 2]

    for idx in range(1, len(dp)):
        for jdx in range(1, len(dp[0])):
            if pattern[jdx - 1] == '.' or pattern[jdx - 1] == text[idx - 1]:
                dp[idx][jdx] = dp[idx - 1][jdx - 1]
            elif pattern[jdx - 1] == '*':
                dp[idx][jdx] = dp[idx][jdx - 2]
                if pattern[jdx - 2] == '.' or pattern[jdx - 2] == text[idx - 1]:
                    dp[idx][jdx] = dp[idx][jdx] or dp[idx - 1][jdx]
                else:
                    dp[idx][jdx] = False

    print(dp[-1][-1])
    return dp


if __name__ == "__main__":
    # text, pattern = "aa"*20+"b", "a*"*20+"b"
    # dp = is_match_dp(text, pattern)
    text, pattern = "aab", "c*a*b"
    dp = is_match_dp_backward(text, pattern)
    dp2 = is_match_dp_forward(text, pattern)

    # text, pattern = "abcdefg", "123456*"
    # dp = is_match_dp_backward(text, pattern)
    # dp2 = is_match_dp_forward(text, pattern)
    #
    # text, pattern = "aa" * 20 + "b", "a*" * 20 + "b"
    # dp = is_match_dp_backward(text, pattern)
    # dp2 = is_match_dp_forward(text, pattern)