# -*- coding: utf-8 -*-
"""
Created on Jun 07 20:07:21 2022

@author: Jerome Yutai Shen

1081

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        起点指针从左往右推着终点指针
        :param s:
        :return:
        """
        # write your code here
        if not s:
            return 0

        n = len(s)
        max_len = 0
        visited = set()
        end_pntr = 0

        for start_pntr in range(n):
            while end_pntr < n and s[end_pntr] not in visited:
                visited.add(s[end_pntr])
                end_pntr += 1

            max_len = max(max_len, end_pntr - start_pntr)
            visited.remove(s[start_pntr])

        return max_len

    def start_pntr_pushes_end_pntr(self, s: str) -> int:
        """
        起点指针作为发动机
        起点指针从左往右推着终点指针
        :param s:
        :return:
        """
        # write your code here
        if not s:
            return 0

        n = len(s)
        max_len = 0
        visited = set()
        end_pntr = 0

        for start_pntr in range(n):
            while end_pntr < n and s[end_pntr] not in visited:
                visited.add(s[end_pntr])
                end_pntr += 1

            max_len = max(max_len, end_pntr - start_pntr)
            visited.remove(s[start_pntr])

        return max_len

    def end_pntr_pulls_start_pntr(self, s: str) -> int:
        """
        终点指针作为发动机
        终点指针从左往右拉着起点指针
        :param s:
        :return:
        """
        # write your code here
        if not s:
            return 0

        n = len(s)
        max_len = 0
        visited = set()
        start_pntr = 0

        for end_pntr in range(n):
            while start_pntr < end_pntr and s[end_pntr] in visited:
                visited.remove(s[start_pntr])
                start_pntr += 1

            max_len = max(max_len, end_pntr - start_pntr + 1)
            visited.add(s[end_pntr])

        return max_len


def get_max_len(s: str) -> int:
    n = len(s)
    ans = 0
    # mp stores the current index of a character
    mp = { }

    i = 0
    # try to extend the range [i, j]
    for j in range(n):
        if s[j] in mp: # 是再次遇到，那么以第一次的index+1为新的起点，不是以这一次的index+1为新的起点
            i = max(mp[s[j]], i)

        ans = max(ans, j - i + 1)
        mp[s[j]] = j + 1

    return ans


def s_push_e(s: str) -> int:
    """
    起点指针作为发动机
    起点指针从左往右推着终点指针
    :param s:
    :return:
    """
    # write your code here
    if not s:
        return 0

    n = len(s)
    max_len = 0
    visited = set()
    end_pntr = 0

    for start_pntr in range(n):
        while end_pntr < n and s[end_pntr] not in visited:
            visited.add(s[end_pntr])
            end_pntr += 1

        max_len = max(max_len, end_pntr - start_pntr)
        visited.remove(s[start_pntr])

    return max_len


if __name__ == "__main__":
    s = "abcapqke"
    get_max_len(s)
    s = "tmmzuxt"
    get_max_len(s)
    s = " "
    get_max_len(s)