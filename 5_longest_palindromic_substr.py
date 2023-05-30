# -*- coding: utf-8 -*-
"""
Created on May 22 15:19:28 2022

@author: Jerome Yutai Shen

"""


def longestPalindrome( src_str: str) -> str:
    if not src_str:
        return src_str

    end_start = (0, 0) # 终止idx在前，起始idx在后，因为下面for循环里用max比较tuple/list，比较逻辑是按照元素顺序依次比较。
    for center_idx in range(len(src_str)):
        end_start = max(end_start, get_index_range(src_str, center_idx, center_idx))
        end_start = max(end_start, get_index_range(src_str, center_idx, center_idx + 1))

    return src_str[end_start[1]: end_start[0] + end_start[1]]


def get_index_range(src_str: str, idx_left: int, idx_right: int) -> tuple:
    while idx_left >= 0 and idx_right < len(src_str) and src_str[idx_left] == src_str[idx_right]:
        idx_left -= 1
        idx_right += 1
    return idx_right - idx_left - 1, idx_left + 1


class Solution2:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # 重点1：任何代码都要进行异常检测
        if not s:
            return ""
        
        # 重点2：用空行区分开异常检测部分，核心代码部分，和返回值部分，属于高端代码风格技巧
        longest = ""
        for middle in range(len(s)):
            # 重点3：子函数化避免重复代码
            sub = self.find_palindrome_from(s, middle, middle)
            # 重点4：通过返回值来避免使用全局变量这种不好的代码风格
            if len(sub) > len(longest):
                longest = sub
            sub = self.find_palindrome_from(s, middle, middle + 1)
            if len(sub) > len(longest):
                longest = sub
                
        # 重点2：用空行区分开异常检测部分，核心代码部分，和返回值部分，属于高端代码风格技巧
        return longest
        
    def find_palindrome_from(self, string, left, right):
        while left >= 0 and right < len(string):
            # 重点5：将复杂判断拆分到 while 循环内部，而不是放在 while 循环中，提高代码可读性
            if string[left] != string[right]:
                break
            left -= 1
            right += 1
            
        return string[left + 1:right]