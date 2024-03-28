# -*- coding: utf-8 -*-
"""
Created on Nov 10 22:25:42 2023

@author: Jerome Yutai Shen

"""


def minRemoveToMakeValid(s: str) -> str:
    indexes_to_remove = set()
    stack = []
    for i, c in enumerate(s):
        if c not in "()":
            continue
        if c == "(":
            stack.append(i)
        elif not stack:
            indexes_to_remove.add(i)
        else:
            stack.pop()

    indexes_to_remove |= set(stack)
    string_builder = []
    for i, c in enumerate(s):
        if i not in indexes_to_remove:
            string_builder.append(c)
    return "".join(string_builder)


def minRemoveToMakeValid2(s: str) -> str:
    # Pass 1: Remove all invalid ")"
    first_pass_chars = []
    balance = 0
    open_seen = 0
    for c in s:
        if c == "(":
            balance += 1
            open_seen += 1
        if c == ")":
            if balance == 0:
                continue
            balance -= 1
        first_pass_chars.append(c)

    # Pass 2: Remove the rightmost "("
    result = []
    open_to_keep = open_seen - balance
    for c in first_pass_chars:
        if c == "(":
            open_to_keep -= 1
            if open_to_keep < 0:
                continue
        result.append(c)

    return "".join(result)


def minRemoveToMakeValid3(s: str) -> str:
    # Pass 1: Remove all invalid ")"
    first_pass_chars = []
    balance = 0
    open_seen = 0
    for c in s:
        if c == "(":
            balance += 1
            open_seen += 1
        if c == ")":
            if balance == 0:
                continue
            balance -= 1
        first_pass_chars.append(c)

    # Pass 2: Remove the rightmost "("
    result = []
    open_to_keep = open_seen - balance
    for c in first_pass_chars:
        if c == "(":
            open_to_keep -= 1
            if open_to_keep < 0:
                continue
        result.append(c)

    return "".join(result)


if __name__ == "__main__":
    s = "L(e)))et((co)d(e"
