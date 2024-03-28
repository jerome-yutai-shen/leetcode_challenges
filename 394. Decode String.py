# -*- coding: utf-8 -*-
"""
Created on Jan 03 13:49:20 2024

@author: Jerome Yutai Shen

"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
                continue

            strs = []
            print(f"stack{stack}, strs{strs}")
            while stack and stack[-1] != '[':
                strs.append(stack.pop())
            print(f"stack{stack}, strs{strs}")
            # skip '['
            stack.pop()

            repeats = 0
            base = 1
            while stack and stack[-1].isdigit():
                repeats += (ord(stack.pop()) - ord('0')) * base
                base *= 10
            stack.append(''.join(reversed(strs)) * repeats)

        return ''.join(stack)


def decodeString(s: str) -> str:
    decode_stack = []
    for c in s:
        if c != "]":
            decode_stack.append(c)
            continue

        inner_stack = []
        while decode_stack and decode_stack[-1] != '[':
            inner_stack.append(decode_stack.pop())

        decode_stack.pop() # 此时 decode_stack最后一个字符肯定是'['

        repeats = 0
        base = 1
        while decode_stack and decode_stack[-1].isdigit():
            repeats += (ord(decode_stack.pop()) - ord('0')) * base
            base *= 10
        decode_stack.append(''.join(reversed(inner_stack)) * repeats)

    return ''.join(decode_stack)


if __name__ == "__main__":
    _ = Solution()
    print(_.decodeString("2[a2[c3[dfg2[che]]]]"))