# -*- coding: utf-8 -*-
"""
Created on May 30 15:07:47 2022

@author: Jerome Yutai Shen

"""


def reverse_words(words: str) -> str:
    """
    fastest, space complexity O(n)
    """
    words_list = words.split(" ")

    for idx in range(len(words_list)):
        word = words_list[idx]
        words_list[idx] = word[::-1]

    return " ".join(words_list)


def reverse_words2(words: str) -> str:
    """
    slowest
    """
    words_list = list(words)
    idx_range = [-1]
    for idx, char in enumerate(words):
        if char == " " and idx < len(words):
            idx_range.append(idx)

    idx_range.append(len(words))

    print(idx_range)
    for idx in range(len(idx_range) - 1):
        p_left, p_right = idx_range[idx] + 1, idx_range[idx + 1] - 1
        print(p_left, p_right)
        while p_left <= p_right:
            words_list[p_right], words_list[p_left] = words_list[p_left], words_list[p_right]
            p_left += 1
            p_right -= 1

    return "".join(words_list)


def reverse_words3(words: str) -> str:
    """
    second slowest
    """
    word = ""
    answer = ""
    for c in words:
        if c == ' ':
            if word != "":
                answer += word[::-1]
            word = ""
            answer += c
        else:
            word += c
    if word != "":
        answer += word[::-1]
    return answer


if __name__ == "__main__":
    words = "Let's take LeetCode contest"
    print(reverse_words(words) == reverse_words2(words))