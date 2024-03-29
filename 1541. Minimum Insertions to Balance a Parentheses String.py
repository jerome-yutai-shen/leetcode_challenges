# -*- coding: utf-8 -*-
"""
Created on Nov 25 17:04:37 2023

@author: Jerome Yutai Shen

本题和 921 Minimum Add to Make Parentheses Valid本质一样。区别只在于一个左括号必须和两个连续的右括号匹配。
我们仍然可以沿用贪心法的思想，用count来记录未被匹配的左括号的数目。变化在于：

我们需要连续两个右括号，才能试图与之前的一个左括号对消。
如果不存在连续的两个右括号，我们必须先手工增加一个右括号，即ret++，然后再试图匹配左括号消减count。
如果最终有剩余未被匹配的左括号，我们需要增加两倍数目的右括号与之对应，即ret+=count*2.

"""

def minInsertions(s: str) -> int:
    """
    O(n), O(1)
    """
    count = 0
    ret = 0
    idx = 0
    while idx < len(s):
        if s[idx] == "(":
            count += 1
        else:
            if idx + 1 < len(s) and s[idx + 1] == ")":
                count -= 1
                idx += 1 # count idx 谁先谁后都行
            else:
                count -= 1
                ret += 1

        if count < 0:
            ret += 1
            count = 0

        idx += 1

    return ret + count * 2


if __name__ == "__main__":
    s = "())))"
    minInsertions(s)