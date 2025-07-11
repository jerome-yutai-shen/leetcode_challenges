# -*- coding: utf-8 -*-
"""
Created on Jul 07 08:47:55 2025

@author: Jerome Yutai Shen

这两个递归写法的区别
flatten1每次递归新建自己的 res
需要手动收集res.extend(flatten1(item))

flatten2外层函数定义，共享一个 res

"""

def flatten1(nested_list: list) -> list[int]:
    res = []
    for item in nested_list:
        if isinstance(item, list):
            res.extend(flatten1(item))
        else:
            res.append(item)
    return res


def flatten2(nested_list: list) -> list[int]:
    res = []

    def dfs(lst):
        for item in lst:
            if isinstance(item, list):
                dfs(item)
            else:
                res.append(item)

    dfs(nested_list)
    return res


def flatten3(nested_list: list) -> list[int]:
    """注意入栈方式决定了顺序是反的"""
    stack = nested_list
    res = []

    while stack:
        item = stack.pop()
        if isinstance(item, int):
            res.append(item)
        else:
            stack.extend(item)
    res.reverse() # 所以最后还得反转一次
    return res




nested_list = [[1], 2,3,[4, 5], [[[[[[6]]], 7]]]]
print(flatten1(nested_list))
print(flatten2(nested_list))


def add_exclamation(func):
    def wrapper(*args):
        print(f"{func(*args)}!!!!!")
        return
    return wrapper


@add_exclamation
def name(text):
    return text

name("Jerome")